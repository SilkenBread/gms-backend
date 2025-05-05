# API Documentation - Attendance System


## Authentication
Bearer Token (JWT)


---

## 1. Register Attendance
**Endpoint:** `POST /attendance/`

### Request
```http
POST /attendance/
Content-Type: application/json
Authorization: Bearer <your_token>

{
  "member_id": "123456789"
}
```

### Responses
Success (201 Created)
```json
{
  "attendance_id": 15,
  "member": {
    "user_id": "123456789",
    "name": "Juan",
    "surname": "Pérez"
  },
  "entry_time": "2023-11-15T14:30:22.123456Z",
  "registered_by": "María López",
  "days_remaining": 46
}
```

### Error Cases
```json
{
  "error": "Miembro no encontrado",
  "status": 404
}
```
```json
{
  "error": "La membresía ha expirado",
  "membership_end_date": "2023-10-31",
  "status": 400
}
```

