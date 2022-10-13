from django.urls import path,include
from .views import *

from rest_framework import routers
# router=routers.DefaultRouter()

# router.register('input',InputViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns =[
    #path('',include(router.urls)),
    path("",InputViewSet.as_view(), name="Input"),
    path("auth/",include("rest_framework.urls", namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

