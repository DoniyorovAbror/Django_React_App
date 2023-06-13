from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'receipt', ReceiptsWiewSet)

foodRouter = routers.SimpleRouter()
foodRouter.register(r'foods', FoodWieSet, basename='foods')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/receipt/<int:category_id>/", include(foodRouter.urls)),
]
