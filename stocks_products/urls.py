from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('logistic.urls')),
    re_path(r'^$', RedirectView.as_view(url='/admin/', permanent=False)),
]