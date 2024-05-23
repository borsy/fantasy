from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

@api_view(['GET'])
def getAllItems(request):
    items = Item.objects.all()
    ser = ItemSerializer(items, many = True)
    return Response(ser.data)