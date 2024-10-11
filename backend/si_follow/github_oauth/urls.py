from django.urls import path, include
from rest_framework.routers import DefaultRouter

from github_oauth.controller.views import GithubOauthView

router = DefaultRouter()
router.register(r'github_oauth', GithubOauthView, basename='github_oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('github', GithubOauthView.as_view({'get': 'githubOauthURI'}), name='get-github-oauth-uri'),
    path('github/access-token', GithubOauthView.as_view({'post': 'githubAccessTokenURI'}), name='get-github-access-token-uri'),
    # path('github/user-info', GithubOauthView.as_view({'post': 'githubUserInfoURI'}), name='get-github-user-info-uri'),
    path('logout', GithubOauthView.as_view({'post': 'dropRedisTokenForLogout'}), name='drop-redis_service-token-for-logout')
]