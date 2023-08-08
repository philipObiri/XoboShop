from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("product.urls")),
    path("account/", include("account.urls")),
    path("admin/", admin.site.urls),
    path("payment/", include("payment.urls")),
]


admin.site.site_header = "Zobo Shop"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Zobo Shop"
