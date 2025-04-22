# Members

## Create a member

```
POST /members/
```

### Permissions (create a member)

- administrator.

- receptionist.

### Description (create a member)

Registers a new member with user and membership details.

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

Example:

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
        "message": "Miembro creado",
        "member_id": "string"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Retrieve a member

```
GET /members/{member_id}/
```

### Permissions (retrieve a member)

- administrator.

- receptionist.

- trainer.

### Description (retrieve a member)

Retrieves detailed information about a specific member.

### Path parameters (retrieve a member)

- `member_id`: the unique identifier of the member.

### Response (retrieve a member)

- `200 OK`.

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

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## List all members

```
GET /members/
```

### Permissions (list all members)

- administrator.

- receptionist.

### Description (list all members)

Retrieves a list of all members registered in the system.

### Response (list all members)

- `200 OK`.

    ```json
    [
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
        },
        //...
    ]
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Update a member

```
PUT /members/{member_id}/
```

### Permissions (update a member)

- administrator.

- receptionist.

### Description (update a member)

Updates information for an existing member. All fields are optional (only include the fields you want to update).

### Path parameters (update a member)

- `member_id`: the unique identifier of the member.

### Request body (update a member)

```json
{
    "user": {
        "email": "string",
        "name": "string",
        "surname": "string",
        "password": "string"
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

Example:

```json
{
    "user": {
        "email": "new.email@example.com",
        "name": "Updated Name"
    },
    "member": {
        "active_membership": false
    }
}
```

### Response (update a member)

- `200 OK`.

    ```json
    {
        "message": "Miembro actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Delete a member

```
DELETE /members/{member_id}/delete/
```

### Permissions (update a member)

- administrator.

- receptionist.

### Description (delete a member)

Permanently removes a member from the system.

### Path parameters (delete a member)

- `member_id`: the unique identifier of the member.

### Response (delete a member)

- `200 OK`.

    ```json
    {
        "message": "Miembro eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Register attendance

```
POST /members/{member_id}/attendance/
```

### Permissions (update a member)

- administrator.

- receptionist.

### Description (register attendance)

Registers a new attendance entry for a specific member.

### Path parameters (register attendance)

- `member_id`: the unique identifier of the member checking in.

### Response (register attendance)

- `201 Created`.

    ```json
    {
        "message": "string",
        "attendance_id": "integer",
        "entry_time": "YYYY-MM-DDTHH:MM:SS",
        "member_name": "string",
        "registered_by": "string"
    }
    ```
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "La membresía del usuario no está activa"
    }
    ```

    or

    ```json
    {
        "error": "Error message"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

## List member attendance

```
GET /members/{member_id}/attendance/
```

### Permissions (update a member)

- administrator.

- receptionist.

### Description (list member attendance)

Retrieves the attendance history for a specific member.

### Path parameters (list member attendance)

- `member_id`: the unique identifier of the member.

### Response (list member attendance)

- `200 OK`.

    ```json
    {
        "member_id": "string",
        "member_name": "string",
        "attendance_records": [
            {
                "attendance_id": "integer",
                "entry_time": "YYYY-MM-DDTHH:MM:SS"
            }
            // ...
        ]
    }
    ```
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Create physical evaluation

```
POST /members/{member_id}/evaluation/
```

### Permissions (create physical evaluation)

- trainer.

### Description (create physical evaluation)

Creates a new physical evaluation record for a specific member.

### Path parameters (create physical evaluation)

- `member_id`: the unique identifier of the member being evaluated.

### Request body (create physical evaluation)

```json
{
    "evaluation_date": "YYYY-MM-DD",
    "weight": "decimal",
    "height": "decimal",
    "notes": "string"
}
```

Example:

```json
{
    "weight": 75.5,
    "height": 180.0,
    "notes": "Initial evaluation. Member is in good condition."
}
```

> Note: If `evaluation_date` is not provided, the current date will be used.

### Response (create physical evaluation)

- `201 Created`.

    ```json
    {
        "message": "Evaluación física registrada correctamente",
        "evaluation_id": "integer",
        "member_name": "string"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## List member physical evaluations

```
GET /members/{member_id}/evaluation/
```

### Permissions (list member physical evaluations)

- trainer.

### Description (list member physical evaluations)

Retrieves the physical evaluation history for a specific member.

### Path parameters (list member physical evaluations)

- `member_id`: the unique identifier of the member.

### Response (list member physical evaluations)

- `200 OK`.

    ```json
    {
        "member_id": "string",
        "member_name": "string",
        "evaluations": [
            {
                "evaluation_id": "integer",
                "evaluation_date": "YYYY-MM-DD",
                "weight": "decimal",
                "height": "decimal",
                "notes": "string"
            }
            // ...
        ]
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Miembro no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```
