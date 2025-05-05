from django.contrib import admin
from .models import MembershipPlan, Member, Payment
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_display', 'is_active')
    list_filter = ('is_active', 'duration_unit')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description', 'is_active')
        }),
        ('Precio y Duración', {
            'fields': ('price', 'duration', 'duration_unit', 'validity')
        }),
    )

    def duration_display(self, obj):
        return f"{obj.duration} {obj.get_duration_unit_display()}"
    duration_display.short_description = 'Duración'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'membership_status', 'membership_plan', 'start_end_date')
    list_filter = ('active_membership', 'membership_plan')
    search_fields = ('user__email', 'user__name', 'user__surname')
    raw_id_fields = ('user',)
    readonly_fields = ('registration_date', 'payment_history_link')
    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'birth_date', 'registration_date')
        }),
        ('Membresía', {
            'fields': (
                'active_membership', 
                'membership_plan', 
                'membership_start_date', 
                'membership_end_date',
                'payment_history_link'
            )
        }),
    )

    def user_info(self, obj):
        return f"{obj.user.get_full_name()} ({obj.user.email})"
    user_info.short_description = 'Miembro'

    def membership_status(self, obj):
        color = 'green' if obj.active_membership else 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            "Activa" if obj.active_membership else "Inactiva"
        )
    membership_status.short_description = 'Estado'

    def start_end_date(self, obj):
        if obj.membership_start_date and obj.membership_end_date:
            return f"{obj.membership_start_date} a {obj.membership_end_date}"
        return "-"
    start_end_date.short_description = 'Vigencia'

    def payment_history_link(self, obj):
        url = reverse('admin:payments_payment_changelist') + f'?member__id__exact={obj.user.id}'
        return mark_safe(f'<a href="{url}">Ver historial de pagos</a>')
    payment_history_link.short_description = 'Historial'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'member_info',
        'plan_info',
        'amount',
        'payment_date',
        'payment_method_display',
        'created_by_info'
    )
    list_filter = ('payment_method', 'payment_date', 'membership_plan')
    search_fields = (
        'member__user__email',
        'member__user__name',
        'member__user__surname',
        'payment_id'
    )
    raw_id_fields = ('member', 'created_by')
    date_hierarchy = 'payment_date'
    list_select_related = ('member__user', 'membership_plan', 'created_by')

    fieldsets = [
        ('Información Básica', {
            'fields': (
                'payment_id',
                'created_at',
                'created_by'
            )
        }),
        ('Información del Miembro', {
            'fields': (
                'member',
                'membership_plan',
                'amount',
                'payment_date'
            )
        }
        ),
        ('Método de Pago', {
            'fields': (
                'payment_method',
            )
        })
    ]


    def member_info(self, obj):
        return obj.member.user.get_full_name()
    member_info.short_description = 'Miembro'
    member_info.admin_order_field = 'member__user__name'

    def plan_info(self, obj):
        return obj.membership_plan.name
    plan_info.short_description = 'Plan'
    plan_info.admin_order_field = 'membership_plan__name'

    def payment_method_display(self, obj):
        return dict(Payment.PAYMENT_METHOD_CHOICES).get(obj.payment_method)
    payment_method_display.short_description = 'Método'

    def created_by_info(self, obj):
        return obj.created_by.get_full_name() if obj.created_by else '-'
    created_by_info.short_description = 'Registrado por'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Para no superusuarios, mostrar solo pagos que ellos registraron
            return qs.filter(created_by=request.user)
        return qs
