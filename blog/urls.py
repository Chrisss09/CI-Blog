from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='posts')),
    path('posts/', include('posts.urls')),
    path('media/<int:path_id>', serve, {'document_root': MEDIA_ROOT}),
]
