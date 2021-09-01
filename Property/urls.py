from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# <<<<<<< HEAD
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChangeForm
# =======
# >>>>>>> aakash
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('profile',views.profile,name="profile"),
    # path('changepassword',views.Changepassword,name="changepassword"),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='user_page/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    # path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='user_page/password_change_done.html'), name="passwordchangedone"),


    path('category/<int:id>',views.category,name="category"),
    path('p_lists/<int:id>',views.p_lists,name="p_lists"),
    path('p_single',views.p_single,name="p_single"),
    path('addAgency',views.addAgency,name="addAgency"),
    path('Update',views.Update,name="Update"),
    path('agency',views.agency,name="agency"),
    path('broker',views.broker,name="broker"),
    path('addproperty',views.addProperty,name="addproperty"),
    path('about-us',views.about,name="about-us"),
    path('services',views.services,name="services"),
    path('pricing',views.pricing,name="pricing"),
    path('faq',views.faq,name="faq"),
    path('invoice',views.invoice,name="invoice"),
    path('error404',views.error404,name="error404"),
    path('register',views.register,name="register"),
    path('features',views.features,name="features"),
  

    # path('logout', views.logoutUser, name='logout'),
    # path('category', views.categoryData, name='header'),
]

# for image require default setting and also set media url in setting file
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)