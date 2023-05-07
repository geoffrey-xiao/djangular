from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


import views

router = routers.DefaultRouter()

router.register(r'question', views.QuestionViewSet)

urlpatterns = [
    path('/api/v1/', include(router.urls)),
    path('admin/', admin.site.urls)
]