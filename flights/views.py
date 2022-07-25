from datetime import datetime, timedelta

from pytz import timezone
from flights.serializers import BookingSerializer, FLightSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView

class FlightList(ListAPIView):
    queryset=Flight.objects.all()
    serializer_class = FLightSerializer 

class BookingList(ListAPIView):
    queryset=Booking.objects.all().filter(date__gte = datetime.today())
    serializer_class = BookingSerializer

