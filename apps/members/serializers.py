from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers

from .models import Attendance, Member, MembershipPlan, Payment

User = get_user_model()

class MemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    surname = serializers.CharField(source='user.surname')
    email = serializers.CharField(source='user.email')
    user_id = serializers.CharField(source='user.id')

    class Meta:
        model = Member
        fields = ['user_id', 'name', 'surname', 'email', 'birth_date', 
                 'registration_date', 'active_membership', 'membership_type', 
                 'membership_end_date']

class AttendanceSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    registered_by = serializers.SerializerMethodField()
    days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['attendance_id', 'member', 'entry_time', 'registered_by', 'days_remaining']
        read_only_fields = ['attendance_id', 'entry_time']

    def get_registered_by(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return f"{request.user.name} {request.user.surname}"
        return None

    def get_days_remaining(self, obj):
        return (obj.member.membership_end_date - timezone.now().date()).days

class CreateAttendanceSerializer(serializers.ModelSerializer):
    member_id = serializers.CharField(write_only=True)

    class Meta:
        model = Attendance
        fields = ['member_id']
    
    def validate_member_id(self, value):
        try:
            member = Member.objects.get(user_id=value)
            if member.user.user_type != 'member':
                raise serializers.ValidationError("Solo miembros pueden registrar asistencia")
            
            if not member.active_membership:
                raise serializers.ValidationError("La membresía no está activa")
            
            today = timezone.now().date()
            if member.membership_end_date < today:
                member.active_membership = False
                member.save()
                raise serializers.ValidationError("La membresía ha expirado")
            
            return value
        except Member.DoesNotExist:
            raise serializers.ValidationError("Miembro no encontrado")

    def validate(self, data):
        member = Member.objects.get(user_id=data['member_id'])
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        
        if Attendance.objects.filter(
            member=member,
            entry_time__range=(today_start, today_end)
        ).exists():
            raise serializers.ValidationError("El miembro ya registró asistencia hoy")
        
        return data

    def create(self, validated_data):
        member = Member.objects.get(user_id=validated_data['member_id'])
        attendance = Attendance.objects.create(
            member=member,
            entry_time=timezone.now()
        )
        return attendance

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    membership_plan = MembershipPlanSerializer(read_only=True)
    
    class Meta:
        model = Member
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    membership_plan = MembershipPlanSerializer(read_only=True)
    created_by = serializers.StringRelatedField()
    
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['payment_id', 'created_at', 'created_by']

class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['member', 'membership_plan', 'amount', 'payment_date', 'payment_method']
    
    def validate(self, data):
        # Validar que el plan esté activo
        if not data['membership_plan'].is_active:
            raise serializers.ValidationError("Este plan de membresía no está disponible")
        
        # Validar que el monto sea correcto
        if data['amount'] != data['membership_plan'].price:
            raise serializers.ValidationError(
                f"El monto debe ser {data['membership_plan'].price} para este plan"
            )
        
        return data
