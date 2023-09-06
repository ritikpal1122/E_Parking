from django.contrib import admin
from django.urls import path,include
from carpark import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('viewparking/', views.viewparking),
    path('parkbyloc/', views.parkbyloc),
    path('parkbyloc1/', views.parkbyloc1),
    path('viewspace/', views.viewspace),
    path('viewspace1/', views.viewspace1),
    path('bookspace/<int:bid>', views.bookspace),
    path('booknow/', views.booknow),
    path('mybooking/', views.mybooking),
    path('myuser/', include("signup.urls")),
  
    
]
