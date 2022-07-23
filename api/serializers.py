from rest_framework import serializers

from courier.models import CourierDetail
from delivery.models import DeliveryArea


class CourierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourierDetail
        fields = ('id', 'name', 'surname', 'phone')


class DeliveryAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryArea
        fields = ('id', 'name', 'of', 'to')
