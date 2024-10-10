from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root_route(request):
    return Response(
        {
            'message': 'Welcome to SpellMaster API!',
            'status': 'API is up and running',
            'version': '1.0',
        },
        status=status.HTTP_200_OK,
    )
