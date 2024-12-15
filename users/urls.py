from django.urls import path  
from django.contrib.auth import views as auth_views  



from users import views  

app_name = 'user_app'  
urlpatterns = [
    
    path('login/', views.UserLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
]