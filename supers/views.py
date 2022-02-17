from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET'])
def supers_list(request):


    return Response('ok')