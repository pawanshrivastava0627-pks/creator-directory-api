from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


class UserListView(APIView):

    def get(self, request):

        users = User.objects.filter(
            agency=request.user.agency
        )

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):

    # Sirf owner aur admin user create kar sakte hain
     if request.user.role not in ["owner", "admin"]:
        return Response(
            {"error": "Permission denied."},
            status=status.HTTP_403_FORBIDDEN
        )

     serializer = UserSerializer(data=request.data)

     if serializer.is_valid():

        # Admin owner create nahi kar sakta
        if (
            request.user.role == "admin"
            and serializer.validated_data["role"] == "owner"
        ):
            return Response(
                {
                    "error": "Admin cannot create owner users."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer.save(
            agency=request.user.agency
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

     return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )