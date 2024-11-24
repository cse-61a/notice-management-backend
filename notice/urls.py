from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'notices', NoticeViewSet, basename='notice')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = router.urls
