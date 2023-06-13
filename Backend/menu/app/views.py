from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.

class ReceiptsWiewSet(ReadOnlyModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = ReceiptSerializer

class FoodWieSet(ReadOnlyModelViewSet):
    model = Food
    serializer_class = FoodSerializer

    def get_queryset(self):
        cat_id = self.kwargs['category_id']
        category = Category.objects.get(id=cat_id)
        foods = Food.objects.filter(category = category)
        return foods

