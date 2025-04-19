from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from .models import Member


@api_view(["POST"])
@permission_classes([AllowAny]) # IsAuthenticated
def create_member(request):
    try:
        data = request.data
        user_data = data.get("user")
        member_data = data.get("member")

        user = User.objects.create_user(
            id=user_data["id"],
            email=user_data["email"],
            password=user_data["password"],
            name=user_data["name"],
            surname=user_data["surname"],
            user_type="member"
        )

        member = Member.objects.create(
            user=user,
            birth_date=member_data["birth_date"],
            registration_date=member_data["registration_date"],
            active_membership=member_data.get("active_membership", True),
            membership_type=member_data["membership_type"],
            membership_end_date=member_data["membership_end_date"]
        )

        return Response({"message": "Member created", "member_id": member.user.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
