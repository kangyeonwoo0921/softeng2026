"""
URL configuration for doitdjango_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include # include가 꼭 있어야 해요! [cite: 173]ㄴ

urlpatterns = [
    path('admin/', admin.site.urls), # [cite: 176]
    path('', include('single_pages.urls')), # 이 줄이 있어야 우리가 만든 앱으로 연결됩니다! [cite: 177]
]