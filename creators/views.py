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
    
    def post(self, request):

      serializer = CreatorSerializer(
        data=request.data,
        context={"request": request}
    )

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

      return Response(serializer.errors, status=400)
    
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