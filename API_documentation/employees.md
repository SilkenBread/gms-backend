# Employees (app)

## Permissions

- administrator.

## Employees

### Create an employee

```
POST /employees/
```

#### Description (create an employee)

Creates a new employee and assigns them to one or more groups ("administrator", "trainer", or "receptionist").

#### Request body (create an employee)

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

#### Response (create an employee)

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

#### Description (retrieve an employee)

Retrieves detailed information about a specific employee.

#### Path parameters (retrieve an employee)

- `employee_id`: the unique identifier of the employee (user id).

#### Response (retrieve an employee)

- `200 OK`.

    ```json
    {
        "user": {
            "id": "string",
            "email": "string",
            "name": "string",
            "surname": "string",
            "user_type": "employee",
        },
        "employee": {
            "hire_date": "YYYY-MM-DD",
            "salary": "decimal",
            "groups": "employee groups"
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
GET /employees/
```

#### Description (list all employees)

Retrieves a list of all employees registered in the gym.

#### Response (list all employees)

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
                "salary": "decimal",
                "groups": "employee groups"
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
PUT /employees/{employee_id}/
```

#### Description (update an employee)

Updates information for an existing employee. All fields are optional (only include the fields you want to update). You can also update the employee's groups.

> If you want to keep the employee's current groups unchanged, you must explicitly provide the current groups in the `groups` field of the request body. Any groups not included will be removed from the employee.

#### Path parameters (update an employee)

- `employee_id`: the unique identifier of the employee (user id).

#### Request body (update an employee)

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

#### Response (update an employee)

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
DELETE /employees/{employee_id}/
```

#### Description (delete an employee)

Removes an employee from the gym.

#### Path parameters (delete an employee)

- `employee_id`: the unique identifier of the employee (user id).

#### Response (delete an employee)

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
