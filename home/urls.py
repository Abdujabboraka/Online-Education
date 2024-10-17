from django.urls import path
from .views import homepage, enrollment, detail, user_register, user_login, user_logout
urlpatterns = [
    path('', homepage, name='homepage'),
    path('enrollment/', enrollment, name='enrollment'),
    path('detail/<int:course_id>', detail, name='detail'),
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),

]