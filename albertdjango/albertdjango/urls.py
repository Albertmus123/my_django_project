from django.contrib import admin
from django.urls import path, include
# from django.views.static import server
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('albertapp.urls')),
   

   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
