from django.http import JsonResponse

from django.http import JsonResponse
from .models import Books
from .models import Customer

#MainPage View

def index(req):
    return JsonResponse('hello', safe=False)

#Books View
def books(request):
    books = Books.objects.all().values('bookname', 'writer', 'date')
    return JsonResponse(list(books), safe=False)

#Customer View

def customers(request):
    customers = Customer.objects.all().values('name', 'city', 'age')
    return JsonResponse(list(customers), safe=False)
