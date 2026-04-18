"""
URL configuration for vaidya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from vaidya_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', register),
    path('register/signupNGO/', signupNGO),
    path('register/signupCDA/', signupCDA),
    path('register/signinADMIN/', signinADMIN),
    path('register/signupDOCTORS/', signupDOCTORS),
    path('loginCDA/', loginCDA),
    path('loginDOCTORS/', loginDOCTORS),
    path('loginNGO/', loginNGO),
    path('loginADMIN/', loginADMIN),
    path('citizen_dashboard/', citizen_dashboard),
    path('ngo/', ngo),
    path('doctors/', doctors),
    path('logout/', logout),
    path('citizen_dashboard/telemedicine/', telemedicine),
    path('citizen_dashboard/campaign/', campaign),
    path('citizen_dashboard/reportcrisis/', reportcrisis),
    path('citizen_dashboard/track/', track),
    path('doctors/appointments/', appointments),
    path('doctors/reportcrisis/', reportcrisis),
    path('ngo/createcampaign/', createcampaign),
    path('ngo/overview/', overview),
    path('ngo/ngoMonitor/', ngoMonitor),
    path('vaidya_admin/', VaidyaAdmin),
    path('vaidya_admin/usermanagement/', usermanagement),
    path('vaidya_admin/adminappoint/', adminappoint),
    path('vaidya_admin/admincampaign/', admincampaign),
    path('vaidya_admin/complain/', admincomplain),
    path('vaidya_admin/adminUser/', adminUser),
]
