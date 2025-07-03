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
    classes = FitnessClass.objects.filter(datetime__gte=localtime()).order_by('datetime')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    """
    Book a fitness class.
    Expects JSON data with 'class_id', 'client_name', and 'client_email'.
    """
    data = request.data
    try:
        class_id = data['class_id']
        name = data['client_name']
        email = data['client_email']
    except KeyError:
        return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)

    if fitness_class.available_slots <= 0:
        return Response({"error": "No slots available"}, status=status.HTTP_400_BAD_REQUEST)

    if Booking.objects.filter(fitness_class=fitness_class, client_email=email).exists():
        return Response({"error": "You have already booked this class"}, status=status.HTTP_400_BAD_REQUEST)

    # Create booking
    Booking.objects.create(
        fitness_class=fitness_class,
        client_name=name,
        client_email=email
    )

    # Decrease available slots
    fitness_class.available_slots -= 1
    fitness_class.save()

    return Response({"message": "Booking successful"}, status=status.HTTP_201_CREATED)


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