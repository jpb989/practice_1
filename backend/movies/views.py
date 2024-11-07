from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Create your views here.

class MovieListView(APIView):
    def get(self, request):
        
        return Response(data = {"": ""}, status=HTTP_200_OK)