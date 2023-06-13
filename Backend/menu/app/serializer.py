from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import *


class ReceiptSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class FoodSerializer(ModelSerializer):
    category = StringRelatedField(many=False)

    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'photo',
            'slug',
            'description',
            'ingredients',
            'category',
            'category_id'
        ]
        