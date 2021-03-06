from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions, response, views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from orders.views import payment_success


schema_view = get_schema_view(
    openapi.Info(
        title="PhotoSphere API",
        default_version='v1',
        description="Version 1.0, PhotoSphere API",
        public=False,
    ),
    permission_classes=(permissions.AllowAny,), # todo: make admin only
)

class PingView(views.APIView):

    @swagger_auto_schema(
        operation_id='ping',
        operation_description='Ping the server!',
        responses={
            '200': "{'message': 'Hello from PhotoSphere!'}",
        }
    )
    def get(self, request, *args, **kwargs):
        return response.Response(data={'message': 'Hello from PhotoSphere!'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ping/', PingView.as_view(), name='ping'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('user/', include('user.urls')),
    path('photo/', include('photos.urls')),
    path('album/', include('albums.urls')),
    path('organization/', include('organizations.urls')),
    path('exhibition/', include('exhibitions.urls')),
    path('order/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
