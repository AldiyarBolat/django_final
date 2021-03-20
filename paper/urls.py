from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('journals', views.JournalViewSet, basename='journals')

urlpatterns = router.urls
