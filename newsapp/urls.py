from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('users.urls')),
    path('', include('news.api.urls'))
]
