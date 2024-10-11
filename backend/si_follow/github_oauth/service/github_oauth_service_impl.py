from github_oauth.service.github_oauth_service import GithubOauthService
import requests
from si_follow import settings


class GithubOauthServiceImpl(GithubOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.loginUrl = settings.GITHUB['LOGIN_URL']
            cls.__instance.clientId = settings.GITHUB['CLIENT_ID']
            cls.__instance.clientSecret = settings.GITHUB['CLIENT_SECRET']
            cls.__instance.redirectUri = settings.GITHUB['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.GITHUB['TOKEN_REQUEST_URI']
            cls.__instance.userinfoRequestUri = settings.GITHUB['USERINFO_REQUEST_URI']
            cls.__instance.userinfoEmailRequestUri = settings.GITHUB['USERINFO_EMAIL_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # GitHub 로그인 URL 생성
    def githubLoginAddress(self):
        print("githubLoginAddress()")
        return (f"{self.loginUrl}?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&scope=user:email")

    # Access Token 요청
    def requestAccessToken(self, githubAuthCode):
        print("requestAccessToken()")
        accessTokenRequestForm = {
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': githubAuthCode,
            'redirect_uri': self.redirectUri
        }

        print(f"client_id: {self.clientId}")
        print(f"client_secret: {self.clientSecret}")
        print(f"code: {githubAuthCode}")
        print(f"tokenRequestUri: {self.tokenRequestUri}")

        headers = {'Accept': 'application/json'}
        response = requests.post(self.tokenRequestUri, headers=headers, data=accessTokenRequestForm)

        # 상태 코드와 응답 내용 출력
        print(f"response status code: {response.status_code}")
        print(f"response content: {response.content}")

        return response.json().get('access_token')

    # 사용자 정보 요청
    def requestUserInfo(self, accessToken):
        headers = {'Authorization': f'token {accessToken}'}

        # 1. 사용자 기본 정보 요청
        response = requests.get(self.userinfoRequestUri, headers=headers)

        # 여기서 user_info는 딕셔너리여야 함. 리스트가 아닌지 확인
        if isinstance(response.json(), dict):
            user_info = response.json()
        else:
            # 만약 user_info가 리스트라면 (이메일 정보 등), 첫 번째 딕셔너리를 가져오도록 처리
            user_info = {}
            print("Expected dictionary but got a list, skipping user_info extraction.")

        print(f"user_info: {user_info}")

        # 2. 사용자 기본 정보에 이메일이 없는 경우, 이메일 정보 요청
        email = user_info.get('email') if isinstance(user_info, dict) else None
        if not email:
            print("No email found in user info, fetching emails...")
            email_response = requests.get(self.userinfoEmailRequestUri, headers=headers)
            emails = email_response.json()

            # emails는 리스트로 반환되므로, 리스트에서 primary 이메일을 찾아야 함
            print(f"emails: {emails}")
            email = next(
                (email_data['email'] for email_data in emails if email_data['primary'] and email_data['verified']),
                None)

            if email:
                print(f"Primary email found: {email}")
                # 이메일을 user_info에 추가
                user_info['email'] = email
            else:
                print("No verified primary email found.")

        # 3. 최종 사용자 정보 반환 (이메일 포함)
        return user_info

