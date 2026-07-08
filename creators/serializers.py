from rest_framework import serializers
from .models import Creator, AgencyLink


class AgencyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyLink
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    agency_links = serializers.SerializerMethodField()

    class Meta:
        model = Creator
        fields = "__all__"

    def get_agency_links(self, obj):
        request = self.context.get("request")

        links = obj.agency_links.filter(
            agency=request.user.agency
        )

        return AgencyLinkSerializer(links, many=True).data