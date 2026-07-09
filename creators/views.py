from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrAdmin
from .models import Creator
from .serializers import CreatorSerializer
from rest_framework import status
from .models import Creator, AgencyLink
from .serializers import CreatorSerializer, CreatorLinkSerializer

class CreatorListView(APIView):
    permission_classes = [IsOwnerOrAdmin]

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
    permission_classes = [IsOwnerOrAdmin]

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
    
    def patch(self, request, pk):

       creator = get_object_or_404(
        Creator.objects.filter(
            agency_links__agency=request.user.agency
        ).distinct(),
        pk=pk
    )

       serializer = CreatorSerializer(
        creator,
        data=request.data,
        partial=True,
        context={"request": request}
    )

       if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

       return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):

     creator = get_object_or_404(
        Creator.objects.filter(
            agency_links__agency=request.user.agency
        ).distinct(),
        pk=pk
    )

    # Current agency ka link
     link = AgencyLink.objects.get(
        agency=request.user.agency,
        creator=creator
    )

    # Link remove karo
     link.delete()

    # Agar koi link nahi bacha to creator bhi delete
     if not creator.agency_links.exists():
        creator.delete()
        return Response(
            {"message": "Creator deleted successfully."},
            status=status.HTTP_200_OK
        )

     return Response(
        {"message": "Creator unlinked successfully."},
        status=status.HTTP_200_OK
    )
    
class CreatorLinkView(APIView):
    permission_classes = [IsOwnerOrAdmin]

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