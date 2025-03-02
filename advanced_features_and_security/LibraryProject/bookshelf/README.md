# Django Role-Based Permissions

## Groups and Permissions
- **Viewers:** Can only view books (`can_view`).
- **Editors:** Can view and edit books (`can_view`, `can_create`, `can_edit`).
- **Admins:** Can perform all actions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Setting Up Groups
Run the command:
```sh
python manage.py setup_groups
