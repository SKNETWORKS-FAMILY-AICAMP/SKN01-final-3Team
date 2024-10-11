from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service_impl import AccountServiceImpl
from github_oauth.serializer.github_oauth_url_serializer import GithubOauthUrlSerializer
from github_oauth.service.github_oauth_service_impl import GithubOauthServiceImpl
from redis_service.redis_service_impl import RedisServiceImpl


class GithubOauthView(viewsets.ViewSet):
    githubOauthService = GithubOauthServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    profileRepository = ProfileRepositoryImpl.getInstance()

    # GitHub 로그인 URL 생성
    def githubOauthURI(self, request):
        try:
            url = self.githubOauthService.githubLoginAddress()
            print(f"url: {url}")
            serializer = GithubOauthUrlSerializer(data={'url': url})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error generating GitHub OAuth URL: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Access Token 요청 및 사용자 정보 처리
    def githubAccessTokenURI(self, request):
        print("githubAccessTokenURI()")

        # POST 요청에서 'code' 값 가져오기
        code = request.data.get('code')

        if not code:
            return JsonResponse({'error': 'Code is missing'}, status=400)

        print(f"Received code: {code}")

        try:
            # 1. Access Token 요청
            accessToken = self.githubOauthService.requestAccessToken(code)
            print(f"Access token: {accessToken}")

            # 2. Access Token을 사용하여 사용자 정보 가져오기
            user_info = self.githubUserInfo(accessToken)
            return JsonResponse(user_info, status=200)

        except Exception as e:
            print(f"Error during GitHub OAuth flow: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

    # Access Token으로 사용자 정보 가져오기 및 Redis에 토큰 저장
    def githubUserInfo(self, accessToken):
        print("githubUserInfo()")

        try:
            # 1. Access Token을 사용하여 GitHub 사용자 정보 가져오기
            user_info = self.githubOauthService.requestUserInfo(accessToken)
            email = user_info.get('email')

            if not email:
                return {'error': 'Email not found in user info'}, status.HTTP_400_BAD_REQUEST

            # 2. 사용자 정보 DB에서 조회
            account = self.profileRepository.findByEmail(email)

            if not account:
                # 최초 로그인 - 새로운 사용자 등록
                print("New user detected. Saving user info to DB.")
                self.accountService.registerAccount(
                    loginType='GITHUB',
                    roleType='NORMAL',
                    email=email,
                )

            # 3. Redis에 Access Token 저장 및 발급
            redis_token_response = self.redisAccessToken(email)
            if redis_token_response.status_code != 200:
                return {'error': 'Failed to store token in Redis'}, redis_token_response.status_code

            # 4. Redis에서 발급된 토큰 가져오기
            user_token = redis_token_response.data.get('userToken')

            # 5. 사용자 정보와 Redis 토큰 반환
            return {
                'user_info': user_info,
                'token': user_token  # Redis에서 발급된 토큰 포함
            }

        except KeyError as e:
            print(f"KeyError: {str(e)}")
            return {'error': 'Invalid data received'}, status.HTTP_400_BAD_REQUEST
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return {'error': 'Server error'}, status.HTTP_500_INTERNAL_SERVER_ERROR

    # Redis에 Access Token 저장 (별도의 메서드로 분리)
    def redisAccessToken(self, email):
        try:
            return self.redisService.generate_and_store_access_token(self.profileRepository, email)
        except Exception as e:
            print(f"Error generating/storing access token in Redis: {e}")
            return JsonResponse({'error': 'Failed to store access token'}, status=500)

    # Redis에서 토큰 삭제 (로그아웃 처리)
    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            redis_response = self.redisService.delete_access_token(userToken)
            return redis_response
        except Exception as e:
            print(f"Error during Redis token deletion: {str(e)}")
            return JsonResponse({'error': str(e)}, status=400)
