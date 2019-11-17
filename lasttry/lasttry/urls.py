
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import  include, url
from django.contrib import admin
admin.autodiscover()
import sampleapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getuser_details/<str:tname>/',sampleapp.views.getuser_details),
    path('dashboard/',sampleapp.views.dashboard),
    path('',sampleapp.views.dashboard),
    path('register/',sampleapp.views.user_create),
    path('login/',sampleapp.views.login),
    path('search/',sampleapp.views.user_search),
    path('logout/',sampleapp.views.logout),
    path('showpost/',sampleapp.views.showpost),
    path('chatroom/', sampleapp.views.chatroom),
    path('update/',sampleapp.views.user_update),
    path('find/',sampleapp.views.file_search),
]



from django.conf import settings
if settings.DEBUG:
    from  django.conf.urls.static import static

    urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)