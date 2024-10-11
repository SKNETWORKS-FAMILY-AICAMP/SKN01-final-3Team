from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service_impl import AccountServiceImpl
from kakao_oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakao_oauth.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
from redis_service.redis_service_impl import RedisServiceImpl


class OauthView(viewsets.ViewSet):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    profileRepository = ProfileRepositoryImpl.getInstance()

    def kakaoOauthURI(self, request):
            url = self.kakaoOauthService.kakaoLoginAddress()
            print(f"url:", url)
            serializer = KakaoOauthUrlSerializer(data={ 'url': url })
            serializer.is_valid(raise_exception=True)
            print(f"validated_data: {serializer.validated_data}")
            return Response(serializer.validated_data)

    def kakaoAccessTokenURI(self, request):
        print("kakaoAccessTokenURI()")

        # POST 요청으로 요청 본문에서 'code' 값 가져오기
        code = request.data.get('code')

        if not code:
            return JsonResponse({'error': 'Code is missing'}, status=400)

        print(f"Received code: {code}")

        try:
            # 1. Access Token 요청
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            print(f"Access token: {accessToken}")

            # 2. Access Token을 사용하여 사용자 정보 가져오기
            user_info = self.kakaoUserInfoURI(accessToken['access_token'])
            print(f"user_info: {user_info}")
            return JsonResponse(user_info, status=200)

        except Exception as e:
            print(f"Error during Kakao OAuth flow: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    def kakaoUserInfoURI(self, accessToken):
        print("kakaoUserInfoURI()")
        # accessToken = request.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            # 1. 카카오 사용자 정보 가져오기
            user_info = self.kakaoOauthService.requestUserInfo(accessToken)
            email = user_info.get('kakao_account', {}).get('email')
            print(f"Email: {email}")

            if not email:
                return JsonResponse({'error': 'Email not found in user info'}, status=400)

            # 2. 사용자 정보 DB에서 조회 (최초 로그인 여부 확인)
            account = self.profileRepository.findByEmail(email)

            if not account:
                # 최초 로그인 - 새로운 사용자 등록
                print("New user detected. Saving user info to DB.")
                self.accountService.registerAccount(
                    loginType='KAKAO',  # 이 부분은 GitHub일 경우 'GITHUB'로 바꿀 수 있음
                    roleType='NORMAL',
                    email=email,
                )

            # 3. Redis에 액세스 토큰 저장 및 발급
            redis_token_response = self.redisAccessToken(email)
            if redis_token_response.status_code != 200:
                return JsonResponse({'error': 'Failed to store token in Redis'},
                                    status=redis_token_response.status_code)

            # 4. Redis에서 발급된 토큰 가져오기
            user_token = redis_token_response.data.get('userToken')

            # 5. 사용자 정보와 Redis 토큰 반환
            return {
                'user_info': user_info,
                'token': user_token  # Redis에서 발급된 토큰 포함
            }

        except KeyError as e:
            print(f"KeyError: {str(e)}")
            return JsonResponse({'error': 'Invalid data received'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': 'Server error'}, status=500)

    def redisAccessToken(self, email):
        try:
            return self.redisService.generate_and_store_access_token(self.profileRepository, email)
        except Exception as e:
            print(f"Error generating/storing access token in Redis: {e}")
            return JsonResponse({'error': 'Failed to store access token'}, status=500)

    # Redis에서 토큰 삭제 (로그아웃 처리)
    def dropRedisTokenForLogout(self, request):
        userToken = request.data.get('userToken')
        return self.redisService.delete_access_token(userToken)