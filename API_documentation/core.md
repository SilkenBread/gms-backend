# Core (app)

## Permissions

- administrator (for all endpoints).

## Services

### Create a service

```
POST /services/
```

#### Description (create a service)

Creates a new service.

#### Request body (create a service)

```json
{
    "name": "string",
    "description": "string",
    "is_active": true
}
```

#### Response (create a service)

- `201 Created`.

    ```json
    {
        "service_id": 1,
        "name": "string",
        "description": "string",
        "is_active": true
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Retrieve a service

```
GET /services/{service_id}/
```

#### Description (retrieve a service)

Retrieves details of a specific service.

#### Path parameters (retrieve a service)

- `service_id`: the unique identifier of the service.

#### Response (retrieve a service)

- `200 OK`.

    ```json
    {
        "service_id": 1,
        "name": "string",
        "description": "string",
        "is_active": true
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Servicio no encontrado"
    }
    ```

### List all services

```
GET /services/
```

#### Description (list all services)

Retrieves a list of all services.

#### Response (list all services)

- `200 OK`.

    ```json
    [
        {
            "service_id": 1,
            "name": "string",
            "description": "string",
            "is_active": true
        },
        // ...
    ]
    ```

### Update a service

```
PUT /services/{service_id}/
```

#### Description (update a service)

Updates an existing service. All fields are optional.

#### Path parameters (update a service)

- `service_id`: the unique identifier of the service.

#### Request body (update a service)

```json
{
    "name": "string",
    "description": "string",
    "is_active": true
}
```

#### Response (update a service)

- `200 OK`.

    ```json
    {
        "message": "Servicio actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Servicio no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Delete a service

```
DELETE /services/{service_id}/
```

#### Description (delete a service)

Deletes a service.

#### Path parameters (delete a service)

- `service_id`: the unique identifier of the service.

#### Response (delete a service)

- `200 OK`.

    ```json
    {
        "message": "Servicio eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Servicio no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Schedules

### Create a schedule

```
POST /schedules/
```

#### Description (create a schedule)

Creates a new schedule.

#### Request body (create a schedule)

```json
{
    "start_time": "HH:MM:SS",
    "end_time": "HH:MM:SS",
    "day": "monday | tuesday | wednesday | thursday | friday | saturday | sunday",
    "day_category": "morning | afternoon | evening"
}
```

#### Response (create a schedule)

- `201 Created`.

    ```json
    {
        "schedule_id": 1,
        "start_time": "08:00:00",
        "end_time": "12:00:00",
        "day": "monday",
        "day_category": "morning"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Retrieve a schedule

```
GET /schedules/{schedule_id}/
```

#### Description (retrieve a schedule)

Retrieves details of a specific schedule.

#### Path parameters (retrieve a schedule)

- `schedule_id`: the unique identifier of the schedule.

#### Response (retrieve a schedule)

- `200 OK`.

    ```json
    {
        "schedule_id": 1,
        "start_time": "08:00:00",
        "end_time": "12:00:00",
        "day": "monday",
        "day_category": "morning"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Horario no encontrado"
    }
    ```

### List all schedules

```
GET /schedules/
```

#### Description (list all schedules)

Retrieves a list of all schedules.

#### Response (list all schedules)

- `200 OK`.

    ```json
    [
        {
            "schedule_id": 1,
            "start_time": "08:00:00",
            "end_time": "12:00:00",
            "day": "monday",
            "day_category": "morning"
        },
        // ...
    ]
    ```

### Update a schedule

```
PUT /schedules/{schedule_id}/
```

#### Description (update a schedule)

Updates an existing schedule. All fields are optional.

#### Path parameters (update a schedule)

- `schedule_id`: the unique identifier of the schedule.

#### Request body (update a schedule)

```json
{
    "start_time": "HH:MM:SS",
    "end_time": "HH:MM:SS",
    "day": "monday | tuesday | wednesday | thursday | friday | saturday | sunday",
    "day_category": "morning | afternoon | evening"
}
```

#### Response (update a schedule)

- `200 OK`.

    ```json
    {
        "message": "Horario actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Horario no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

### Delete a schedule

```
DELETE /schedules/{schedule_id}/
```

#### Description (delete a schedule)

Deletes a schedule.

#### Path parameters (delete a schedule)

- `schedule_id`: the unique identifier of the schedule.

#### Response (delete a schedule)

- `200 OK`.

    ```json
    {
        "message": "Horario eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Horario no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```
