from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.loginUser,name="login"),
    path('register',views.register,name="register"),
    path('logout', views.logoutUser, name='logout'),
    # path('category', views.categoryData, name='header'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)