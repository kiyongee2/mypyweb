from django.contrib.auth import views
from django.urls import path

app_name = 'common'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='common/login.html')
          , name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]