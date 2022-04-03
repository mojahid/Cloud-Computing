from django.contrib import admin
from django.urls import include, path
from home.views import index

urlpatterns = [
    path('',index,name='index'),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),

]
