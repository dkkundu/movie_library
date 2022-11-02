
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]