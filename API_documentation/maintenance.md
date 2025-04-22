# Maintenance

The following endpoints are only accessible for users in the group "administrator".

## Create maintenance

```
POST /maintenance/create/
```

### Description

Creates a new maintenance record for equipment.

### Request body

```json
{
    "equipment_id": "integer",
    "maintenance_date": "YYYY-MM-DD",
    "description": "string",
    "cost": "decimal"
}
```

### Response

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

## Retrieve maintenance

```
GET /maintenance/{maintenance_id}/
```

### Description

Retrieves detailed information about a specific maintenance record.

### Path parameters

- `maintenance_id`: the unique identifier of the maintenance record.

### Response

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
GET /maintenance/list/
```

### Description

Retrieves a list of all maintenance records in the system.

### Response

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

## Update maintenance

```
PUT /maintenance/{maintenance_id}/update/
```

### Description

Updates information for an existing maintenance record. All fields are optional.

### Path parameters

- `maintenance_id`: the unique identifier of the maintenance record.

### Request body

```json
{
    "equipment_id": "integer",
    "maintenance_date": "YYYY-MM-DD",
    "description": "string",
    "cost": "decimal"
}
```

### Response

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

## Delete maintenance

```
DELETE /maintenance/{maintenance_id}/delete/
```

### Description

Permanently removes a maintenance record from the system.

### Path parameters

- `maintenance_id`: the unique identifier of the maintenance record.

### Response

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