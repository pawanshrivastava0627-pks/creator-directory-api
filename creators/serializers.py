from rest_framework import serializers
from .models import Creator, AgencyLink


class AgencyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyLink
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    agency_links = serializers.SerializerMethodField()
    notes = serializers.CharField(write_only=True, required=False)


    class Meta:
     model = Creator
     fields = [
        "id",
        "name",
        "niche",
        "follower_count",
        "engagement_rate",
        "email",
        "created_at",
        "agency_links",
        "notes",
    ]
     read_only_fields = ["created_at", "agency_links"]

    def get_agency_links(self, obj):
        request = self.context.get("request")

        links = obj.agency_links.filter(
            agency=request.user.agency
        )

        return AgencyLinkSerializer(links, many=True).data
    
    def create(self, validated_data):
      request = self.context["request"]

      notes = validated_data.pop("notes", "")

      creator = Creator.objects.create(**validated_data)

      AgencyLink.objects.create(
        agency=request.user.agency,
        creator=creator,
        notes=notes
    )

      return creator
    
    def update(self, instance, validated_data):

      request = self.context["request"]

      notes = validated_data.pop("notes", None)

    # Shared fields update
      for attr, value in validated_data.items():
        setattr(instance, attr, value)

      instance.save()

    # Update only current agency's notes
      if notes is not None:
        AgencyLink.objects.filter(
            agency=request.user.agency,
            creator=instance
        ).update(notes=notes)

      return instance

class CreatorLinkSerializer(serializers.Serializer):
    notes = serializers.CharField(required=False, allow_blank=True)
