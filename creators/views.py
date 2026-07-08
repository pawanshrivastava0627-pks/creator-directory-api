from rest_framework.views import APIView
from rest_framework.response import Response

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