from django.contrib.auth.models import Group
from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from apps.employees.models import Employee
from apps.users.models import User

from .models import Equipment, Maintenance


class IsAdministrator(BasePermission):
    """
    Allows access only to users in the "administrator" group.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="administrator").exists()
        )


class EmployeeViewSet(viewsets.ViewSet):
    permission_classes = [IsAdministrator]

    def list(self, request):
        try:
            employees = Employee.objects.all()
            employees_data = []
            for emp in employees:
                user = emp.user
                groups = list(user.groups.values_list("name", flat=True))
                emp_data = {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "surname": user.surname,
                        "user_type": user.user_type
                    },
                    "employee": {
                        "hire_date": emp.hire_date,
                        "salary": emp.salary,
                        "groups": groups
                    }
                }
                employees_data.append(emp_data)
            return Response(employees_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            emp = Employee.objects.get(user_id=pk)
            user = emp.user
            groups = list(user.groups.values_list("name", flat=True))
            emp_data = {
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "surname": user.surname,
                    "user_type": user.user_type
                },
                "employee": {
                    "hire_date": emp.hire_date,
                    "salary": emp.salary,
                    "groups": groups
                }
            }
            return Response(emp_data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Empleado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            data = request.data
            user_data = data.get("user")
            emp_data = data.get("employee")

            groups = data.get("groups", [])
            allowed_groups = ["trainer", "administrator", "receptionist"]
            if any(g not in allowed_groups for g in groups):
                return Response({"error": "Solo se permiten los grupos: 'trainer', 'administrator', 'receptionist'"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                id=user_data["id"],
                email=user_data["email"],
                password=user_data["password"],
                name=user_data["name"],
                surname=user_data["surname"],
                user_type="employee"
            )
            emp = Employee.objects.create(
                user=user,
                hire_date=emp_data["hire_date"],
                salary=emp_data["salary"]
            )
            # Assign groups
            for group_name in groups:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            return Response({"message": "Empleado creado", "employee_id": emp.user.id}, status=status.HTTP_201_CREATED)
        except Group.DoesNotExist:
            return Response({"error": "Uno o más grupos no existen. Por favor, crea los grupos requeridos en el sistema."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            emp = Employee.objects.get(user_id=pk)
            user = emp.user
            data = request.data
            user_data = data.get("user", {})
            emp_data = data.get("employee", {})

            allowed_groups = ["trainer", "administrator", "receptionist"]
            groups = data.get("groups", [])
            if any(g not in allowed_groups for g in groups):
                return Response({"error": "Solo se permiten los grupos: 'trainer', 'administrator', 'receptionist'"}, status=status.HTTP_400_BAD_REQUEST)

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
            if emp_data:
                if "hire_date" in emp_data:
                    emp.hire_date = emp_data["hire_date"]
                if "salary" in emp_data:
                    emp.salary = emp_data["salary"]
                emp.save()

            # Remove user from all allowed groups
            for group_name in allowed_groups:
                group = Group.objects.get(name=group_name)
                user.groups.remove(group)

            # Add user to specified groups
            for group_name in groups:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            return Response({"message": "Empleado actualizado correctamente"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Empleado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            emp = Employee.objects.get(user_id=pk)
            user = emp.user
            user.delete()
            return Response({"message": "Empleado eliminado correctamente"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Empleado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EquipmentViewSet(viewsets.ViewSet):
    permission_classes = [IsAdministrator]

    def list(self, request):
        try:
            equipment = Equipment.objects.all()
            equipment_data = []
            for eq in equipment:
                equipment_data.append({
                    "equipment_id": eq.equipment_id,
                    "name": eq.name,
                    "purchase_date": eq.purchase_date,
                    "status": eq.status,
                    "last_maintenance_date": eq.last_maintenance_date
                })
            return Response(equipment_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            eq = Equipment.objects.get(equipment_id=pk)
            eq_data = {
                "equipment_id": eq.equipment_id,
                "name": eq.name,
                "purchase_date": eq.purchase_date,
                "status": eq.status,
                "last_maintenance_date": eq.last_maintenance_date
            }
            return Response(eq_data, status=status.HTTP_200_OK)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            data = request.data
            eq = Equipment.objects.create(
                name=data["name"],
                purchase_date=data["purchase_date"],
                status=data["status"],
                last_maintenance_date=data["last_maintenance_date"]
            )
            return Response({"message": "Equipo creado", "equipment_id": eq.equipment_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            eq = Equipment.objects.get(equipment_id=pk)
            data = request.data
            if "name" in data:
                eq.name = data["name"]
            if "purchase_date" in data:
                eq.purchase_date = data["purchase_date"]
            if "status" in data:
                eq.status = data["status"]
            if "last_maintenance_date" in data:
                eq.last_maintenance_date = data["last_maintenance_date"]
            eq.save()
            return Response({"message": "Equipo actualizado correctamente"}, status=status.HTTP_200_OK)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            eq = Equipment.objects.get(equipment_id=pk)
            eq.delete()
            return Response({"message": "Equipo eliminado correctamente"}, status=status.HTTP_200_OK)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MaintenanceViewSet(viewsets.ViewSet):
    permission_classes = [IsAdministrator]

    def list(self, request):
        try:
            maintenances = Maintenance.objects.all()
            maint_data = []
            for m in maintenances:
                maint_data.append({
                    "maintenance_id": m.maintenance_id,
                    "equipment_id": m.equipment.equipment_id,
                    "equipment_name": m.equipment.name,
                    "maintenance_date": m.maintenance_date,
                    "description": m.description,
                    "cost": m.cost
                })
            return Response(maint_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            m = Maintenance.objects.get(maintenance_id=pk)
            m_data = {
                "maintenance_id": m.maintenance_id,
                "equipment_id": m.equipment.equipment_id,
                "equipment_name": m.equipment.name,
                "maintenance_date": m.maintenance_date,
                "description": m.description,
                "cost": m.cost
            }
            return Response(m_data, status=status.HTTP_200_OK)
        except Maintenance.DoesNotExist:
            return Response({"error": "Mantenimiento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            data = request.data
            equipment = Equipment.objects.get(equipment_id=data["equipment_id"])
            m = Maintenance.objects.create(
                equipment=equipment,
                maintenance_date=data["maintenance_date"],
                description=data["description"],
                cost=data["cost"]
            )
            return Response({"message": "Mantenimiento creado", "maintenance_id": m.maintenance_id}, status=status.HTTP_201_CREATED)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            m = Maintenance.objects.get(maintenance_id=pk)
            data = request.data
            if "equipment_id" in data:
                equipment = Equipment.objects.get(equipment_id=data["equipment_id"])
                m.equipment = equipment
            if "maintenance_date" in data:
                m.maintenance_date = data["maintenance_date"]
            if "description" in data:
                m.description = data["description"]
            if "cost" in data:
                m.cost = data["cost"]
            m.save()
            return Response({"message": "Mantenimiento actualizado correctamente"}, status=status.HTTP_200_OK)
        except Maintenance.DoesNotExist:
            return Response({"error": "Mantenimiento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            m = Maintenance.objects.get(maintenance_id=pk)
            m.delete()
            return Response({"message": "Mantenimiento eliminado correctamente"}, status=status.HTTP_200_OK)
        except Maintenance.DoesNotExist:
            return Response({"error": "Mantenimiento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
