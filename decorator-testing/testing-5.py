# Authorization/Access Control decorator

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def has_role(self, role):
        return self.role == role

def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.has_role('admin'):
            raise Exception(f"This user {user.name} does not have the rights to run this function.")
        return func(user, *args, **kwargs)
    return wrapper

@admin_required
def delete_all_users(user):
    print("Deleted all users")

admin_user = User('Admin', 'admin')
regular_user = User('Regular', 'regular')

delete_all_users(admin_user)  # Outputs: Deleted all users
delete_all_users(regular_user)  # Raises Exception: This user Regular does not have the rights to run this function.
