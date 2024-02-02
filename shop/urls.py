from rest_framework import routers
from shop.views import CategoryViewSet, ProductViewSet

#  6. CREATE AND ADD URLS

# sets up a Django REST framework DefaultRouter and registers the created viewsets with the router.

# Create a DefaultRouter instance
router = routers.DefaultRouter()

# Register the viewsets with the router
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

# Get the generated URLs from the router, and then adds them to the urlpatterns

urlpatterns = [] + router.urls
