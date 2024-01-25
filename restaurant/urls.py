from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="home"),
    path("menu/", views.MenuView.as_view()),
    path("menu/<int:pk>", views.SingleMenuView.as_view()),
    path("booking/", include(router.urls)),
]
