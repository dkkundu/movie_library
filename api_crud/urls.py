
from django.contrib import admin
from django.urls import include, path
from authentication.web_view import Home

# urls
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
