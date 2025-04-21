from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_member),
    path('list/', views.list_members),
    path('<int:member_id>/', views.retrieve_member),
    path('<int:member_id>/update/', views.update_member),
    path('<int:member_id>/delete/', views.delete_member),
    path('<int:member_id>/attendance/register/', views.register_attendance),
    path('<int:member_id>/attendance/', views.list_member_attendance),
]
