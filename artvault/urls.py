from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views  # Ensure this says 'from core import views'

urlpatterns = [
    # Admin panel for data management
    path('admin/', admin.site.urls),

    # Home page showing the Artwork Catalogue (UC-02)
    path('', views.artwork_catalogue, name='catalogue'),

    # ADD THIS LINE RIGHT HERE:
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),

    # Checkout routing (UC-05)
    path('checkout/<int:bid_id>/', views.checkout_step, name='checkout_step'),
]

# Essential for displaying Artwork Thumbnails (FR3)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)