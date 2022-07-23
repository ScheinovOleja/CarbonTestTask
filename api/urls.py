from django.urls import include, path
from rest_framework import routers

from .views import DeliveryApiView, CourierApiView, OrderApiView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('courier/<int:pk>', CourierApiView.as_view()),
    path('create_courier/', CourierApiView.as_view()),
    path('create_order/', OrderApiView.as_view()),
    path('create_delivery', DeliveryApiView.as_view())
]
