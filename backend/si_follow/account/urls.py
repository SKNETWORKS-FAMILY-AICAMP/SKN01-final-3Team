from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.views import AccountView

router = DefaultRouter()
router.register(r'account', AccountView, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check',
         AccountView.as_view({'post': 'checkEmailDuplication'}),
         name='account-email-duplication-check'),
    path('register',
         AccountView.as_view({'post': 'registerAccount'}),
         name='register-account'),
    path('get-user-email', AccountView.as_view({'post': 'getUserEmailFromToken'}), name='get-user-email'),
]
