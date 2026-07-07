import uuid
from django.db import models
from accounts.models import Agency


class Creator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)
    niche = models.CharField(max_length=100)
    follower_count = models.IntegerField()
    engagement_rate = models.FloatField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AgencyLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    agency = models.ForeignKey(
        Agency,
        on_delete=models.CASCADE,
        related_name="creator_links"
    )

    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        related_name="agency_links"
    )

    notes = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("agency", "creator")

    def __str__(self):
        return f"{self.agency.name} - {self.creator.name}"