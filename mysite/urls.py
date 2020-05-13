from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('member_checkin/', include('member_checkin.urls')),
    path('admin/', admin.site.urls),
]