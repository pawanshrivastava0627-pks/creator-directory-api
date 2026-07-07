from django.core.management.base import BaseCommand

from accounts.models import Agency, User
from creators.models import Creator, AgencyLink


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        # -------------------------
        # Agencies
        # -------------------------
        a1, _ = Agency.objects.get_or_create(
            id="a1",
            defaults={
                "name": "Nova Talent",
                "plan": "free",
            },
        )

        a2, _ = Agency.objects.get_or_create(
            id="a2",
            defaults={
                "name": "Bright Star Agency",
                "plan": "pro",
            },
        )

        a3, _ = Agency.objects.get_or_create(
            id="a3",
            defaults={
                "name": "Solo Creators Co",
                "plan": "free",
            },
        )

        # -------------------------
        # Users
        # -------------------------
        User.objects.get_or_create(
            id="u1",
            defaults={
                "agency": a1,
                "email": "owner@nova.com",
                "role": "owner",
            },
        )

        User.objects.get_or_create(
            id="u2",
            defaults={
                "agency": a1,
                "email": "admin@nova.com",
                "role": "admin",
            },
        )

        User.objects.get_or_create(
            id="u3",
            defaults={
                "agency": a2,
                "email": "owner@brightstar.com",
                "role": "owner",
            },
        )

        User.objects.get_or_create(
            id="u4",
            defaults={
                "agency": a3,
                "email": "owner@solo.com",
                "role": "owner",
            },
        )

        # -------------------------
        # Creators
        # -------------------------
        c1, _ = Creator.objects.get_or_create(
            id="c1",
            defaults={
                "name": "Priya Sharma",
                "niche": "beauty",
                "follower_count": 45000,
                "engagement_rate": 3.8,
                "email": "priya@example.com",
            },
        )

        c2, _ = Creator.objects.get_or_create(
            id="c2",
            defaults={
                "name": "Rahul Verma",
                "niche": "fitness",
                "follower_count": 120000,
                "engagement_rate": 2.1,
                "email": "rahul@example.com",
            },
        )

        c3, _ = Creator.objects.get_or_create(
            id="c3",
            defaults={
                "name": "Ananya Iyer",
                "niche": "travel",
                "follower_count": 8000,
                "engagement_rate": 6.4,
                "email": "ananya@example.com",
            },
        )

        # -------------------------
        # Agency Links
        # -------------------------
        AgencyLink.objects.get_or_create(
            agency=a1,
            creator=c1,
            defaults={
                "notes": "Great for skincare campaigns",
            },
        )

        AgencyLink.objects.get_or_create(
            agency=a2,
            creator=c1,
            defaults={
                "notes": "Booked for Q1 shoot",
            },
        )

        AgencyLink.objects.get_or_create(
            agency=a2,
            creator=c2,
            defaults={
                "notes": "High reach, slower replies",
            },
        )

        AgencyLink.objects.get_or_create(
            agency=a1,
            creator=c3,
            defaults={
                "notes": "Micro-influencer, very responsive",
            },
        )

        self.stdout.write(
            self.style.SUCCESS("Database seeded successfully!")
        )