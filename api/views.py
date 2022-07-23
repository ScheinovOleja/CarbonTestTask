from django.db.models import Q
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CourierSerializer, DeliveryAreaSerializer
from courier.models import CourierDetail
from delivery.models import DeliveryArea


class CourierApiView(APIView):

    def post(self, request):
        serializer_courier = CourierSerializer(data=request.data)
        if serializer_courier.is_valid():
            areas = serializer_courier.initial_data['areas']
            courier = serializer_courier.save()
            for area in areas:
                courier.area.add(DeliveryArea.objects.get(id=area['id']))
            return Response(serializer_courier.data, status=status.HTTP_201_CREATED)
        return Response(serializer_courier.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            detail = CourierDetail.objects.get(pk=pk)
        except CourierDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        all_area = [area for area in detail.area.all()[:]]
        serializer_courier = CourierSerializer(detail)
        data_area = []
        for area in all_area:
            data_area.append(DeliveryAreaSerializer(area).data)
        result = serializer_courier.data
        result['areas'] = data_area
        return Response(result)


class OrderApiView(APIView):

    def get(self, request):
        x = float(request.data['delivery'].split(', ')[0])
        y = float(request.data['delivery'].split(', ')[1])
        try:
            query_x_1, query_x_2 = Q(of__x__lt=x), Q(to__x__gt=x)
            query_y_1, query_y_2 = Q(of__y__lt=y), Q(to__y__gt=y)
            area = DeliveryArea.objects.get(query_x_1 and query_x_2 and query_y_1 and query_y_2)
        except DeliveryArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        courier = area.courierdetail_set.first()
        result = {
            "name_courier": courier.name,
            "surname_courier": courier.surname,
            "phone_courier": courier.phone,
            "id_area_courier": area.id
        }
        return Response(result)


class DeliveryApiView(APIView):

    def post(self, request):
        serializer_delivery = DeliveryAreaSerializer(data=request.data)
        if serializer_delivery.is_valid():
            serializer_delivery.save()
            return Response(serializer_delivery.data, status=status.HTTP_201_CREATED)
        return Response(serializer_delivery.errors, status=status.HTTP_400_BAD_REQUEST)
