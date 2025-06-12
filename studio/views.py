from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

# Create your views here.
@api_view(['GET'])
def get_classes(request):
    """
    Retrieve all fitness classes.
    """
    classes = FitnessClass.objects.filter(date__gte=localtime().date()).order_by('datetime')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    """
    Book a fitness class.
    """
    class_id = request.data.get('class_id')
    name = request.data.get('name')
    email = request.data.get('email')
    if not all([class_id, name, email]):
        return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Fitness class not found"}, status=status.HTTP_404_NOT_FOUND)
    if fitness_class.available_slots <1:
        return Response({"error": "No available slots for this class"}, status=status.HTTP_400_BAD_REQUEST)
    booking = Booking.objects.create(fitness_class=fitness_class, name=name, email=email)
    fitness_class.available_slots -= 1
    fitness_class.save()
    return Response({"message": "Booking successful", "booking_id": booking.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_bookings(request):
    """
    Retrieve all bookings.
    """
    email = request.GET.get('email')
    if not email:
        return Response({"error": "Email parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)