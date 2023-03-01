

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include("auctions.urls"))
]

handler404 = "auctions.views.handle_not_found"