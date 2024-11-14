from django.contrib import admin
from django.urls import path, include

app_url_patterns = [
    path('shop/', include('shop.urls'))
    
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(app_url_patterns))
]
