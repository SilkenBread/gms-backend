from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from .models import Member, Attendance
from datetime import datetime


class IsEmployee(BasePermission):
    """
    Custom permission to only allow employees to access the view.
    """
    message = "Solo los empleados pueden registrar asistencia."

    def has_permission(self, request, view):
        # Check if user is authenticated and is an employee
        return request.user and request.user.is_authenticated and request.user.user_type == "employee"


@api_view(["POST"])
@permission_classes([AllowAny]) # IsEmployee
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

        return Response({"message": "Miembro creado", "member_id": member.user.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny]) # IsEmployee
def retrieve_member(request, member_id):
    try:
        member = Member.objects.get(user_id=member_id)
        user = member.user

        member_data = {
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "surname": user.surname,
                "user_type": user.user_type
            },
            "member": {
                "birth_date": member.birth_date,
                "registration_date": member.registration_date,
                "active_membership": member.active_membership,
                "membership_type": member.membership_type,
                "membership_end_date": member.membership_end_date
            }
        }

        return Response(member_data, status=status.HTTP_200_OK)
    except Member.DoesNotExist:
        return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny]) # IsEmployee
def list_members(request):
    try:
        members = Member.objects.all()
        members_data = []

        for member in members:
            user = member.user
            member_data = {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "surname": user.surname,
                    "user_type": user.user_type
                },
                "member": {
                    "birth_date": member.birth_date,
                    "registration_date": member.registration_date,
                    "active_membership": member.active_membership,
                    "membership_type": member.membership_type,
                    "membership_end_date": member.membership_end_date
                }
            }
            members_data.append(member_data)

        return Response(members_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([AllowAny]) # IsEmployee
def update_member(request, member_id):
    try:
        member = Member.objects.get(user_id=member_id)
        user = member.user

        data = request.data
        user_data = data.get("user", {})
        member_data = data.get("member", {})

        # Update user data if provided
        if user_data:
            if "email" in user_data:
                user.email = user_data["email"]
            if "name" in user_data:
                user.name = user_data["name"]
            if "surname" in user_data:
                user.surname = user_data["surname"]
            if "password" in user_data:
                user.set_password(user_data["password"])
            user.save()

        # Update member data if provided
        if member_data:
            if "birth_date" in member_data:
                member.birth_date = member_data["birth_date"]
            if "registration_date" in member_data:
                member.registration_date = member_data["registration_date"]
            if "active_membership" in member_data:
                member.active_membership = member_data["active_membership"]
            if "membership_type" in member_data:
                member.membership_type = member_data["membership_type"]
            if "membership_end_date" in member_data:
                member.membership_end_date = member_data["membership_end_date"]
            member.save()

        return Response({"message": "Miembro actualizado correctamente"}, status=status.HTTP_200_OK)
    except Member.DoesNotExist:
        return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([AllowAny]) # IsEmployee
def delete_member(request, member_id):
    try:
        member = Member.objects.get(user_id=member_id)
        user = member.user

        # Delete user (will cascade delete the member due to OneToOneField)
        user.delete()

        return Response({"message": "Miembro eliminado correctamente"}, status=status.HTTP_200_OK)
    except Member.DoesNotExist:
        return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny]) # IsEmployee
def register_attendance(request, member_id):
    try:
        # Check if member exists
        member = Member.objects.get(user_id=member_id)

        # Get the employee who is registering the attendance
        employee = request.user

        # Check if member has active membership
        if not member.active_membership:
            return Response(
                {"error": "La membresía del usuario no está activa"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create attendance record with current datetime
        attendance = Attendance.objects.create(
            member=member,
            entry_time=datetime.now()
        )

        return Response({
            "message": "Asistencia registrada correctamente",
            "attendance_id": attendance.attendance_id,
            "entry_time": attendance.entry_time,
            "member_name": f"{member.user.name} {member.user.surname}",
            "registered_by": f"{employee.name} {employee.surname}"
        }, status=status.HTTP_201_CREATED)

    except Member.DoesNotExist:
        return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny]) # IsEmployee
def list_member_attendance(request, member_id):
    try:
        # Check if member exists
        member = Member.objects.get(user_id=member_id)

        # Get all attendance records for this member
        attendance_records = Attendance.objects.filter(member=member).order_by('-entry_time')

        # Format the response
        attendance_data = []
        for record in attendance_records:
            attendance_data.append({
                "attendance_id": record.attendance_id,
                "entry_time": record.entry_time,
            })

        return Response({
            "member_id": member_id,
            "member_name": f"{member.user.name} {member.user.surname}",
            "attendance_records": attendance_data
        }, status=status.HTTP_200_OK)

    except Member.DoesNotExist:
        return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
