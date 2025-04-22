# Equipment

The following endpoints are only accessible for users in the group "administrator".

## Create equipment

```
POST /equipment/create/
```

### Description

Creates a new equipment record.

### Request body

```json
{
    "name": "string",
    "purchase_date": "YYYY-MM-DD",
    "status": "operational | under_maintenance",
    "last_maintenance_date": "YYYY-MM-DD"
}
```

### Response

- `201 Created`.

    ```json
    {
        "message": "Equipo creado",
        "equipment_id": "integer"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Retrieve equipment

```
GET /equipment/{equipment_id}/
```

### Description

Retrieves detailed information about a specific equipment item.

### Path parameters

- `equipment_id`: the unique identifier of the equipment.

### Response

- `200 OK`.

    ```json
    {
        "equipment_id": "integer",
        "name": "string",
        "purchase_date": "YYYY-MM-DD",
        "status": "operational | under_maintenance",
        "last_maintenance_date": "YYYY-MM-DD"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Equipo no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## List all equipment

```
GET /equipment/list/
```

### Description

Retrieves a list of all equipment in the system.

### Response

- `200 OK`.

    ```json
    [
        {
            "equipment_id": "integer",
            "name": "string",
            "purchase_date": "YYYY-MM-DD",
            "status": "operational | under_maintenance",
            "last_maintenance_date": "YYYY-MM-DD"
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

## Update equipment

```
PUT /equipment/{equipment_id}/update/
```

### Description

Updates information for an existing equipment item. All fields are optional.

### Path parameters

- `equipment_id`: the unique identifier of the equipment.

### Request body

```json
{
    "name": "string",
    "purchase_date": "YYYY-MM-DD",
    "status": "operational | under_maintenance",
    "last_maintenance_date": "YYYY-MM-DD"
}
```

### Response

- `200 OK`.

    ```json
    {
        "message": "Equipo actualizado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Equipo no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Delete equipment

```
DELETE /equipment/{equipment_id}/delete/
```

### Description

Permanently removes an equipment item from the system.

### Path parameters

- `equipment_id`: the unique identifier of the equipment.

### Response

- `200 OK`.

    ```json
    {
        "message": "Equipo eliminado correctamente"
    }
    ```

- `404 Not Found`.

    ```json
    {
        "error": "Equipo no encontrado"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```
