from rest_framework.routers import DefaultRouter

from apps.project.views import (EstablishmentsViewSet, 
                                CategoryViewSet, 
                                QAViewSet
                                )

router = DefaultRouter()

router.register(r'establishments', EstablishmentsViewSet, basename='establishments')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'qa', QAViewSet, basename='qa')


urlpatterns = router.urls