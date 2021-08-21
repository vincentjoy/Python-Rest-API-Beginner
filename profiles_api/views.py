from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your applicatiopn logic',
            'Is mapped manually to your URLs'
        ]

        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview
        })
