from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Creator
from .serializers import CreatorSerializer


class CreatorListView(APIView):
    

    def get(self, request):

        creators = Creator.objects.filter(
            agency_links__agency=request.user.agency
        ).distinct()

        serializer = CreatorSerializer(
            creators,
            many=True,
            context={"request": request}
        )

        return Response(serializer.data)
    
class CreatorDetailView(APIView):

    def get(self, request, pk):

        creator = get_object_or_404(
            Creator.objects.filter(
                agency_links__agency=request.user.agency
            ).distinct(),
            pk=pk
        )

        serializer = CreatorSerializer(
            creator,
            context={"request": request}
        )

        return Response(serializer.data)