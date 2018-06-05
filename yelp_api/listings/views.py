from .models import Listing
from rest_framework import viewsets
from .serializer import YelpSerializer

# copied from a tutorial for reference, likely will all be removed
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
