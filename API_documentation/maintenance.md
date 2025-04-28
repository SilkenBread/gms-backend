# Maintenance

## Permissions

- administrator.

## Create a maintenance

```
POST /maintenance/
```

### Description (create a maintenance)

Creates a new maintenance record for equipment.

### Request body (create a maintenance)

```json
{
    "equipment_id": "integer",
    "maintenance_date": "YYYY-MM-DD",
    "description": "string",
    "cost": "decimal"
}
```

### Response (create a maintenance)

- `201 Created`.

    ```json
    {
        "message": "Mantenimiento creado",
        "maintenance_id": "integer"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Retrieve a maintenance

```
GET /maintenance/{maintenance_id}/
```

### Description (retrieve a maintenance)

Retrieves detailed information about a specific maintenance record.

### Path parameters (retrieve a maintenance)

- `maintenance_id`: the unique identifier of the maintenance record.

### Response (retrieve a maintenance)

- `200 OK`.

    ```json
    {
        "maintenance_id": "integer",
        "equipment_id": "integer",
        "equipment_name": "string",
        "maintenance_date": "YYYY-MM-DD",
        "description": "string",
        "cost": "decimal"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Mantenimiento no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## List all maintenance

```
GET /maintenance/
```

### Description (list all maintenance)

Retrieves a list of all maintenance records in the gym.

### Response (list all maintenance)

- `200 OK`.

    ```json
    [
        {
            "maintenance_id": "integer",
            "equipment_id": "integer",
            "equipment_name": "string",
            "maintenance_date": "YYYY-MM-DD",
            "description": "string",
            "cost": "decimal"
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

## Update a maintenance

```
PUT /maintenance/{maintenance_id}/
```

### Description (update a maintenance)

Updates information for an existing maintenance record. All fields are optional.

### Path parameters (update a maintenance)

- `maintenance_id`: the unique identifier of the maintenance record.

### Request body (update a maintenance)

```json
{
    "maintenance_id": "integer",
    "equipment_id": "integer",
    "maintenance_date": "YYYY-MM-DD",
    "description": "string",
    "cost": "decimal"
}
```

### Response (Update a maintenance)

- `200 OK`.

    ```json
    {
        "message": "Mantenimiento actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Mantenimiento no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Delete a maintenance

```
DELETE /maintenance/{maintenance_id}/
```

### Description (delete a maintenance)

Removes a maintenance record from the gym.

### Path parameters (delete a maintenance)

- `maintenance_id`: the unique identifier of the maintenance record.

### Response (delete a maintenance)

- `200 OK`.

    ```json
    {
        "message": "Mantenimiento eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Mantenimiento no encontrado"
    }
    ```

- `400 Bad Request`.
    ```json
    {
        "error": "Error message"
    }
    ```