import uuid
from django.db import models


class Agency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    PLAN_CHOICES = [
        ("free", "Free"),
        ("pro", "Pro"),
    ]

    name = models.CharField(max_length=255)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default="free")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("admin", "Admin"),
        ("member", "Member"),
    ]

    agency = models.ForeignKey(
        Agency,
        on_delete=models.CASCADE,
        related_name="users"
    )

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="member"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email