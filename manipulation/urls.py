from django.urls import path, include
from rest_framework.routers import DefaultRouter
from manipulation import views

router = DefaultRouter()
router.register('detail', views.DetailViewSet,)
router.register('transaction', views.TransactionViewSet,)

urlpatterns = [
    path('',include(router.urls)),
]