from django.shortcuts import render
from django.http import JsonResponse
from .serializers import RestaurantSerializer
from django.views.decorators.csrf import csrf_exempt

from .models import Restaurant

# Create your views here.
def index(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request, 'food/index.html', context)

# Restframework
@csrf_exempt
def get_rest_list(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    serializer = RestaurantSerializer(rest_list, many=True)
    return JsonResponse(serializer.data, safe=False)
