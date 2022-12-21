from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('suv', SuvViewSet, basename='suv')
router.register('mijoz', MijozViewSet, basename='mijoz')
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path('adminlar/<int:a>/', AdminView.as_view()),
    path('adminlar/', AdminView.as_view()),
    path("haydovchilar/", HaydovchiView.as_view()),
    path("haydovchilar/<int:a>/", HaydovchiView.as_view()),
    path('buyurtmalar/', BuyurtmaView.as_view()),
    path('buyurtmalar/<int:a>/', BuyurtmaView.as_view()),
]
