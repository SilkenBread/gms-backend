# Equipment

## Permissions

- administrator.

## Create equipment

```
POST /equipment/
```

### Description (create equipment)

Creates a new equipment record.

### Request body (create equipment)

```json
{
    "name": "string",
    "purchase_date": "YYYY-MM-DD",
    "status": "operational | under_maintenance",
    "last_maintenance_date": "YYYY-MM-DD"
}
```

### Response (create equipment)

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

### Description (retrieve equipment)

Retrieves detailed information about a specific equipment item.

### Path parameters (retrieve equipment)

- `equipment_id`: the unique identifier of the equipment.

### Response (retrieve equipment)

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
GET /equipment/
```

### Description (list all equipment)

Retrieves a list of all equipment in the gym.

### Response (list all equipment)

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
PUT /equipment/{equipment_id}/
```

### Description (update equipment)

Updates information for an existing equipment item. All fields are optional.

### Path parameters (update equipment)

- `equipment_id`: the unique identifier of the equipment.

### Request body (update equipment)

```json
{
    "name": "string",
    "purchase_date": "YYYY-MM-DD",
    "status": "operational | under_maintenance",
    "last_maintenance_date": "YYYY-MM-DD"
}
```

### Response (update equipment)

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
DELETE /equipment/{equipment_id}/
```

### Description (delete equipment)

Removes an equipment item from the gym.

### Path parameters (delete equipment)

- `equipment_id`: the unique identifier of the equipment.

### Response (delete equipment)

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
