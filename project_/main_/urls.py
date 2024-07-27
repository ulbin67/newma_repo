from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("single_page.urls")),
    path("applymain/", include("manage_apply.urls")),
    path('', include('qna.urls')),
]

