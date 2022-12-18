from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

urlpatterns = [
    path('multiply/', views.MatrixVectorView.as_view(), name='n_matrix'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularAPIView.as_view(), name='home'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),
]
