"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view),
    path('signuptosignin',views.signuptosignin),
    path('signintosignup', views.signintosignup),
    path('signin',views.signin),
    path('signup',views.signup),
    path('bookstore',views.bookstore),
    path('changepassword',views.changepassword),
    path('passview',views.passview),
    path('signout',views.signout),
    path('librarian',views.librarian),
    path('addbookview',views.addbookview),
    path('addbook',views.addbook),
    path('editbooksuccess',views.editbooksuccess),
    path('editprofilesuccess',views.editprofilesuccess),
    path('editprofile',views.editprofile),
    path('editprofileview',views.editprofileview),
    path('editbook/<int:id>',views.editbook, name='editbook'),
    path('deletebook/<int:id>', views.deletebook, name='deletebook'),
    path('getbook', views.getbook),
    path('returnbook/<int:id>', views.returnbook, name='returnbook'),
    path('alreadyissued', views.alreadyissued),
    path('userrenthistoryview', views.userrenthistoryview)



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)