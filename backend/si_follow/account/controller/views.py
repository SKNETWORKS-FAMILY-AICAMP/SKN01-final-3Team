from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.profile import Profile
from account.serilaizers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from redis_service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.accountService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재' \
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def registerAccount(self, email):
        try:
            account = self.accountService.registerAccount(
                loginType='KAKAO',
                roleType='NORMAL',
                email=email,
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def getUserEmailFromToken(self, request):
        try:
            user_token = request.data.get('user_token')

            if not user_token:
                return JsonResponse({'error': 'User token is missing'}, status=400)

            # Redis에서 user_token으로 사용자 ID 조회
            user_id = self.redisService.get_value_by_key(user_token)

            if not user_id:
                return JsonResponse({'error': 'User not found'}, status=404)

            # 사용자 ID로 바로 Profile에서 조회
            profile = Profile.objects.filter(account_id=user_id).first()

            if not profile:
                return JsonResponse({'error': 'Profile not found'}, status=404)

            # 이메일 반환
            return JsonResponse({'email': profile.email}, status=200)

        except Exception as e:
            print(f"Error retrieving email from token: {str(e)}")
            return JsonResponse({'error': 'Server error'}, status=500)

