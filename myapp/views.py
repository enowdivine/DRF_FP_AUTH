from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer


@api_view(["GET"])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def getItem(request, id):
    # GET ITEM FROM DATABASE
    try:
        item = Item.objects.get(id=id)
    except:
        return Response(
            {
                "error": "Book does not exist",
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    # GET SINGLE ITEM
    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    # UPDATE ITEM
    if request.method == "PUT":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE ITEM
    if request.method == "DELETE":
        item.delete()
        return Response({"message": "Item Deleted"}, status=status.HTTP_204_NO_CONTENT)
