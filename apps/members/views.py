from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AttendanceSerializer, CreateAttendanceSerializer
from apps.users.models import User

from .models import Attendance, Member


class IsTrainer(BasePermission):
    """
    Allows access only to users in the "trainer" group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="trainer").exists()
        )

class IsReceptionistTrainerOrAdministrator(BasePermission):
    """
    Allows access only to users in the "administrator", "receptionist" or "trainer" groups.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="administrator").exists() or
                request.user.groups.filter(name="receptionist").exists() or
                request.user.groups.filter(name="trainer").exists()
            )
        )

class IsReceptionistOrAdministrator(BasePermission):
    """
    Allows access only to users in the "receptionist" or "trainer" groups.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="administrator").exists() or
                request.user.groups.filter(name="receptionist").exists()
            )
        )

class MemberViewSet(viewsets.ViewSet):
    permission_classes = [IsReceptionistOrAdministrator]

    def list(self, request):
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

    def retrieve(self, request, pk=None):
        self.permission_classes = [IsReceptionistTrainerOrAdministrator]
        self.check_permissions(request)
        try:
            member = Member.objects.get(user_id=pk)
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

    def create(self, request):
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

    def update(self, request, pk=None):
        try:
            member = Member.objects.get(user_id=pk)
            user = member.user
            data = request.data
            user_data = data.get("user", {})
            member_data = data.get("member", {})
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

    def destroy(self, request, pk=None):
        try:
            member = Member.objects.get(user_id=pk)
            user = member.user
            user.delete()
            return Response({"message": "Miembro eliminado correctamente"}, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get", "post"], url_path="attendance")
    def attendance(self, request, pk=None):
        if request.method == "GET":
            try:
                member = Member.objects.get(user_id=pk)
                attendance_records = Attendance.objects.filter(member=member).order_by('-entry_time')
                attendance_data = []
                for record in attendance_records:
                    attendance_data.append({
                        "attendance_id": record.attendance_id,
                        "entry_time": record.entry_time,
                    })
                return Response({
                    "member_id": pk,
                    "member_name": f"{member.user.name} {member.user.surname}",
                    "attendance_records": attendance_data
                }, status=status.HTTP_200_OK)
            except Member.DoesNotExist:
                return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "POST":
            try:
                member = Member.objects.get(user_id=pk)
                employee = request.user
                if not member.active_membership:
                    return Response({"error": "La membresía del usuario no está activa"}, status=status.HTTP_400_BAD_REQUEST)
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

    # @action(detail=True, methods=["get", "post"], url_path="evaluation")
    # def physical_evaluation(self, request, pk=None):
    #     self.permission_classes = [IsTrainer]
    #     self.check_permissions(request)
    #     if request.method == "GET":
    #         try:
    #             member = Member.objects.get(user_id=pk)
    #             evaluations = PhysicalEvaluation.objects.filter(member=member).order_by('-evaluation_date')
    #             evaluation_data = []
    #             for eval in evaluations:
    #                 evaluation_data.append({
    #                     "evaluation_id": eval.evaluation_id,
    #                     "evaluation_date": eval.evaluation_date,
    #                     "weight": eval.weight,
    #                     "height": eval.height,
    #                     "notes": eval.notes
    #                 })
    #             return Response({
    #                 "member_id": pk,
    #                 "member_name": f"{member.user.name} {member.user.surname}",
    #                 "evaluations": evaluation_data
    #             }, status=status.HTTP_200_OK)
    #         except Member.DoesNotExist:
    #             return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    #         except Exception as e:
    #             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    #     elif request.method == "POST":
    #         try:
    #             member = Member.objects.get(user_id=pk)
    #             data = request.data

    #             evaluation = PhysicalEvaluation.objects.create(
    #                 member=member,
    #                 evaluation_date=data.get("evaluation_date", datetime.now().date()),
    #                 weight=data["weight"],
    #                 height=data["height"],
    #                 notes=data.get("notes", "")
    #             )

    #             return Response({
    #                 "message": "Evaluación física registrada correctamente",
    #                 "evaluation_id": evaluation.evaluation_id,
    #                 "member_name": f"{member.user.name} {member.user.surname}"
    #             }, status=status.HTTP_201_CREATED)
    #         except Member.DoesNotExist:
    #             return Response({"error": "Miembro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    #         except Exception as e:
    #             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-entry_time')
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsReceptionistOrAdministrator]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAttendanceSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        member_id = self.request.query_params.get('member_id')
        
        if member_id:
            queryset = queryset.filter(member__user_id=member_id)
        
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance = serializer.save()
        
        # Serialize the response with additional data
        response_serializer = AttendanceSerializer(
            attendance, 
            context={'request': request}
        )
        
        headers = self.get_success_headers(response_serializer.data)
        return Response(
            response_serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

    @action(detail=False, methods=['get'], url_path='today')
    def today_attendance(self, request):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        
        attendances = self.get_queryset().filter(
            entry_time__range=(today_start, today_end)
        )
        
        page = self.paginate_queryset(attendances)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(attendances, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='member/(?P<member_id>[^/.]+)')
    def member_attendance(self, request, member_id=None):
        try:
            member = Member.objects.get(user_id=member_id)
            attendances = self.get_queryset().filter(member=member)
            
            page = self.paginate_queryset(attendances)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            
            serializer = self.get_serializer(attendances, many=True)
            return Response(serializer.data)
        except Member.DoesNotExist:
            return Response(
                {"error": "Miembro no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
