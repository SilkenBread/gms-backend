# Database model

```mermaid
erDiagram
    USER {
        VARCHAR id PK "cédula"
        VARCHAR name
        VARCHAR surname
        VARCHAR email
        VARCHAR phone
        VARCHAR user_type "ENUM('employee', 'member')"
    }

    EMPLOYEE {
        VARCHAR id PK, FK
        VARCHAR position "e.g., trainer, receptionist"
        DATE hire_date
        DECIMAL salary
    }

    MEMBER {
        VARCHAR user_id PK,FK
        DATE birth_date
        DATE registration_date
        BOOLEAN active_membership
        VARCHAR membership_type "e.g., monthly, annual"
        DATE membership_end_date
    }

    PAYMENT {
        INT payment_id PK
        VARCHAR member_id FK
        DECIMAL amount
        DATE payment_date
        VARCHAR payment_method "e.g., cash, card"
        VARCHAR period "e.g., monthly, annual"
    }

    ATTENDANCE {
        INT attendance_id PK
        VARCHAR member_id FK
        TIMESTAMP entry_time
    }

    PHYSICAL_EVALUATION {
        INT evaluation_id PK
        VARCHAR member_id FK
        DATE evaluation_date
        DECIMAL weight
        DECIMAL height
        VARCHAR notes
    }

    EQUIPMENT {
        INT equipment_id PK
        VARCHAR name
        DATE purchase_date
        VARCHAR status "e.g., operational, under maintenance"
        DATE last_maintenance_date
    }

    MAINTENANCE {
        INT maintenance_id PK
        INT equipment_id FK
        DATE maintenance_date
        VARCHAR description
        DECIMAL cost
    }

    USER ||--|| EMPLOYEE : "is a"
    USER ||--|| MEMBER : "is a"
    MEMBER ||--o{ PAYMENT : "makes"
    MEMBER ||--o{ ATTENDANCE : "logs"
    MEMBER ||--o{ PHYSICAL_EVALUATION : "has"
    EQUIPMENT ||--o{ MAINTENANCE : "requires"
```
