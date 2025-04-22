# Employees (app)

The following endpoints are only accessible for users in the group "administrator".

## Employees

### Create an employee

```
POST /employees/create/
```

#### Description

Creates a new employee and assigns them to one or more groups ("administrator", "trainer", or "receptionist").

#### Request body

```json
{
    "user": {
        "id": "string",
        "email": "string",
        "password": "string",
        "name": "string",
        "surname": "string"
    },
    "employee": {
        "hire_date": "YYYY-MM-DD",
        "salary": "decimal"
    },
    "groups": ["administrator" | "trainer" | "receptionist"]
}
```

#### Response

- `201 Created`.

    ```json
    {
        "message": "Empleado creado",
        "employee_id": "string"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Retrieve an employee

```
GET /employees/{employee_id}/
```

#### Description

Retrieves detailed information about a specific employee.

#### Path parameters

- `employee_id`: the unique identifier of the employee (user id).

#### Response

- `200 OK`.
    ```json
    {
        "user": {
            "id": "string",
            "email": "string",
            "name": "string",
            "surname": "string",
            "user_type": "employee"
        },
        "employee": {
            "hire_date": "YYYY-MM-DD",
            "salary": "decimal"
        }
    }
    ```

- `404 Not Found`.
    ```json
    {
        "error": "Empleado no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### List all employees

```
GET /employees/list/
```

#### Description

Retrieves a list of all employees registered in the system.

#### Response

- `200 OK`.

    ```json
    [
        {
            "user": {
                "id": "string",
                "email": "string",
                "name": "string",
                "surname": "string",
                "user_type": "employee"
            },
            "employee": {
                "hire_date": "YYYY-MM-DD",
                "salary": "decimal"
            }
        },
        // ...
    ]
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Update an employee

```
PUT /employees/{employee_id}/update/
```

#### Description

Updates information for an existing employee. All fields are optional (only include the fields you want to update). You can also update the employee's groups.

> If you want to keep the employee's current groups unchanged, you must explicitly provide the current groups in the `groups` field of the request body. Any groups not included will be removed from the employee.

#### Path parameters

- `employee_id`: the unique identifier of the employee (user id).

#### Request body

```json
{
    "user": {
        "email": "string",
        "name": "string",
        "surname": "string",
        "password": "string"
    },
    "employee": {
        "hire_date": "YYYY-MM-DD",
        "salary": "decimal"
    },
    "groups": ["administrator" | "trainer" | "receptionist"]
}
```

#### Response

- `200 OK`.

    ```json
    {
        "message": "Empleado actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Empleado no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Delete an employee

```
DELETE /employees/{employee_id}/delete/
```

#### Description

Permanently removes an employee from the system.

#### Path parameters

- `employee_id`: the unique identifier of the employee (user id).

#### Response

- `200 OK`.

    ```json
    {
        "message": "Empleado eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Empleado no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```
