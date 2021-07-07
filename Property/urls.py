from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('profile',views.profile,name="profile"),
    path('category',views.category,name="category"),
    path('p_single',views.p_single,name="p_single"),
    path('p_lists',views.p_lists,name="p_lists"),
    path('agency',views.agency,name="agency"),
    path('broker',views.broker,name="broker"),
    path('about-us',views.about,name="about-us"),
    path('services',views.services,name="services"),
    path('pricing',views.pricing,name="pricing"),
    path('faq',views.faq,name="faq"),
    path('invoice',views.invoice,name="invoice"),
    path('error404',views.error404,name="error404"),


    
    path('register',views.register,name="register"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)