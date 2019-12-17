from django.contrib import admin
from django.urls import path,include
from basic_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('basic_app/', include('basic_app.urls')),
    path('form_name/',views.Form_Name , name='Form_Name'),
    path('user2/',views.user2 , name='user2'),
    path('allarticle/', views.allarticle , name='allarticle'),
]
# from django.contrib import admin
# from django.urls import path,include
# from basic_app import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('basic_app/', include('basic_app.urls')),
#     # path('logout/', views.user_logout , name='logout'),
#     ]
