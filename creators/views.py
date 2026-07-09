from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Creator
from .serializers import CreatorSerializer
from rest_framework import status
from .models import Creator, AgencyLink
from .serializers import CreatorSerializer, CreatorLinkSerializer

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

      agency = request.user.agency

      if agency.plan == "free":

       creator_count = agency.creator_links.count()

       if creator_count >= 5:
        return Response(
            {
                "error": "Free plan can link only 5 creators."
            },
            status=402
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
    
class CreatorLinkView(APIView):

    def post(self, request, pk):

        agency = request.user.agency

        # Free plan check
        if agency.plan == "free":
            if agency.creator_links.count() >= 5:
                return Response(
                    {"error": "Free plan can link only 5 creators."},
                    status=status.HTTP_402_PAYMENT_REQUIRED
                )

        creator = get_object_or_404(Creator, pk=pk)

        if AgencyLink.objects.filter(
            agency=agency,
            creator=creator
        ).exists():

            return Response(
                {"error": "Creator already linked."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CreatorLinkSerializer(data=request.data)

        if serializer.is_valid():

            AgencyLink.objects.create(
                agency=agency,
                creator=creator,
                notes=serializer.validated_data.get("notes", "")
            )

            return Response(
                {"message": "Creator linked successfully."},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )