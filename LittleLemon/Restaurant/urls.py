#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns =[
path('', views.index, name='index'),
    
#add following lines to urlpatterns list 
#path('menu/', views.MenuItemView),
#path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
path('api-token-auth/', obtain_auth_token),
]

