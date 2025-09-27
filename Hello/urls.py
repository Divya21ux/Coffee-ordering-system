from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Cafforina Admin"  
admin.site.site_title = "Cafforina Admin Portal"  
admin.site.index_title = "Welcome to Cafforina cafe" 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
]


