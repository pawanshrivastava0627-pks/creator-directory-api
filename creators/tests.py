from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import Agency, User
from creators.models import Creator, AgencyLink


class CreatorAPITest(TestCase):

    def setUp(self):

        self.client = APIClient()

        # Agency
        self.agency = Agency.objects.create(
            id="a1",
            name="Nova Agency",
            plan="pro"
        )

        # Owner
        self.user = User.objects.create(
            id="u1",
            agency=self.agency,
            email="owner@nova.com",
            role="owner"
        )

        # Creator
        self.creator = Creator.objects.create(
            id="c1",
            name="Priya Sharma",
            niche="beauty",
            follower_count=50000,
            engagement_rate=4.2,
            email="priya@example.com"
        )

        AgencyLink.objects.create(
            agency=self.agency,
            creator=self.creator,
            notes="Test"
        )

        self.client.credentials(
            HTTP_X_USER_ID="u1"
        )

    def test_get_creators(self):

        response = self.client.get("/api/creators/")

        self.assertEqual(response.status_code, 200)

    def test_get_creator_detail(self):

        response = self.client.get(
            "/api/creators/c1/"
        )

        self.assertEqual(response.status_code, 200)

    def test_create_creator(self):

        payload = {
            "id": "c2",
            "name": "Rahul",
            "niche": "fitness",
            "follower_count": 10000,
            "engagement_rate": 5.0,
            "email": "rahul@example.com",
            "notes": "New creator"
        }

        response = self.client.post(
            "/api/creators/",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, 201)

    def test_delete_creator(self):

        response = self.client.delete(
            "/api/creators/c1/"
        )

        self.assertEqual(response.status_code, 200)