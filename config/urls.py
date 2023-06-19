"""
URL configuration for config project.

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
from django.urls import path, include 
from django.conf import settings  # new
from django.conf.urls.static import static  # new



urlpatterns = [

    path('anything-but-admin/', admin.site.urls),  # Django admin
# User management
    # path('accounts/', include('django.contrib.auth.urls')),были созданы исключительно для нашей рукописной страницы регистрации и
# больше не используются.
    path('accounts/', include('allauth.urls')), # new
# Local apps
    # path('accounts/', include('accounts.urls')), # new
    path('', include('pages.urls')),
    path('books/', include('books.urls')), # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new
if settings.DEBUG:  # new
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
