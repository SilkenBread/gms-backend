# Members

The following endpoints are only accessible for employees.

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
GET /members/list/
```

### Description (list all members)

Retrieves a list of all members registered in the system.

### Response (list all members)

- `200 OK`

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

- `400 Bad Request`

    ```json
    {
        "error": "Error message"
    }
    ```

## Update a member

```
PUT /members/{member_id}/update/
```

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
POST /members/{member_id}/attendance/register/
```

### Description (register attendance)

Registers a new attendance entry for a specific member.

### Path parameters (register attendance)

- `member_id`: the unique identifier of the member checking in.

### Request body (register attendance)

```json
{
    "user": {
        "name": "string",
        "surname": "string"
    }
}
```

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