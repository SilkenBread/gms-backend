from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response

from .models import Schedule, Service
from .serializers import ScheduleSerializer, ServiceSerializer


class IsAdministrator(BasePermission):
    """
    Allows access only to users in the "administrator" group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_superuser or
                request.user.groups.filter(name="administrator").exists()
            )
        )

class ServiceViewSet(viewsets.ViewSet):
    permission_classes = [IsAdministrator]

    def list(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Servicio creado", "service_id": serializer.data["service_id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Servicio actualizado correctamente"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response({"message": "Servicio eliminado correctamente"})
        except Service.DoesNotExist:
            return Response({"error": "Servicio no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = [IsAdministrator]

    def list(self, request):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        self.permission_classes = [AllowAny]
        self.check_permissions(request)
        try:
            schedule = Schedule.objects.get(pk=pk)
            serializer = ScheduleSerializer(schedule)
            return Response(serializer.data)
        except Schedule.DoesNotExist:
            return Response({"error": "Horario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Horario creado", "schedule_id": serializer.data["schedule_id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            schedule = Schedule.objects.get(pk=pk)
            serializer = ScheduleSerializer(schedule, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Horario actualizado correctamente"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Schedule.DoesNotExist:
            return Response({"error": "Horario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            schedule = Schedule.objects.get(pk=pk)
            schedule.delete()
            return Response({"message": "Horario eliminado correctamente"})
        except Schedule.DoesNotExist:
            return Response({"error": "Horario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
