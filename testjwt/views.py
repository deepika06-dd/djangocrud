from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class DashboardAPIView(APIView):
    """Protected dashboard - Requires JWT token"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response('admin dashboard data')