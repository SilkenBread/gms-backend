# Members

## Create a member

```
POST /members/create/
```

### Description (create a member)

### Request body (create a member)

```json
{
    "user": {
        "id": "string",
        "email": "string",
        "password": "string",
        "name": "string",
        "surname": "string"
    },
        "member": {
        "birth_date": "YYYY-MM-DD",
        "registration_date": "YYYY-MM-DD",
        "active_membership": true,
        "membership_type": "monthly | annual",
        "membership_end_date": "YYYY-MM-DD"
    }
}
```

```json
{
  "user": {
    "id": "12345678",
    "email": "jane.doe@example.com",
    "password": "securepassword123",
    "name": "Jane",
    "surname": "Doe"
  },
  "member": {
    "birth_date": "1995-06-15",
    "registration_date": "2025-04-19",
    "active_membership": true,
    "membership_type": "monthly",
    "membership_end_date": "2025-05-19"
  }
}
```

### Response (create a member)

- `201 Created`.

    ```json
    {
        "message": "Member created",
        "member_id": "string"
    }
    ```

- `400 Bad Request`

    ```json
    {
        "error": "Error message"
    }
    ```
