from .models import Listing
from rest_framework import viewsets
from .serializer import YelpSerializer

# copied from a tutorial for reference, likely will all be removed
class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = YelpSerializer
