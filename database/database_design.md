# DisasterOps AI - Database Design

## Entities

1. Users
   - user_id
   - name
   - email
   - password
   - role

2. SOS Requests
   - request_id
   - user_id
   - disaster_type
   - description
   - latitude
   - longitude
   - priority
   - status
   - created_at

3. Rescue Teams
   - team_id
   - team_name
   - specialization
   - availability

4. Resources
   - resource_id
   - resource_name
   - quantity
   - availability

5. Shelters
   - shelter_id
   - shelter_name
   - capacity
   - current_occupancy
   - location

6. Missions
   - mission_id
   - request_id
   - team_id
   - status
   - assigned_at