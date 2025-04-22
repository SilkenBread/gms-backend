# Authentication

## Login

```
POST /auth/login/
```

### Description (login)

Authenticates a user (employee or member) and returns JWT tokens for authorization.

### Request body (login)

```json
{
    "email": "string",
    "password": "string"
}
```

Example:

```json
{
    "email": "employee@example.com",
    "password": "securepassword123"
}
```

### Response (login)

- `200 OK`

    ```json
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "user": {
            "id": "12345678",
            "email": "employee@example.com",
            "name": "Employee",
            "surname": "Name",
            "user_type": "employee"
        }
    }
    ```

- `401 Unauthorized`.

    ```json
    {
        "error": "Credenciales inválidas"
    }
    ```

    or

    ```json
    {
        "error": "Usuario inactivo"
    }
    ```

- `400 Bad Request`.

    ```json
    {
        "error": "Error message"
    }
    ```

## Refresh token

```
POST /auth/token/refresh/
```

### Description (refresh token)

Generates a new access token using a valid refresh token. Use this endpoint when your access token has expired.

### Request body (refresh token)

```json
{
    "refresh": "string"
}
```

Example:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Response (refresh token)

- `200 OK`.

    ```json
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
    ```

- `401 Unauthorized`.

    ```json
    {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
    }
    ```

## Using JWT authentication

To access protected endpoints, include the access token in the Authorization header:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Token lifetimes

- Access tokens expire after 60 minutes.

- Refresh tokens expire after 1 day.

### Authentication Flow

1. Call the login endpoint to obtain both access and refresh tokens.

2. Include the access token in the authorization header for all protected API requests.

3. When the access token expires, use the refresh token endpoint to get a new access token.

4. If the refresh token expires, the user must log in again.
