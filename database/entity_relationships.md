# DisasterOps AI - Entity Relationships

## Relationships

1 User
    |
    | submits
    v
Many SOS Requests

1 SOS Request
    |
    | assigned to
    v
1 Mission

1 Mission
    |
    | handled by
    v
1 Rescue Team

1 Mission
    |
    | uses
    v
Many Resources

Many Users
    |
    | stay in
    v
1 Shelter