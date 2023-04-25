#
#
#
from enum import auto, Flag


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXEC = auto()


class BaseUser:
    USER_ROLES = {
        "admin": Permission.READ | Permission.WRITE | Permission.EXEC,
        "user": Permission.READ,
        "manager": Permission.READ | Permission.WRITE,
        "support": Permission.EXEC,
    }

    def _infer_permission(self):
        permissions = Permission.READ  # base default
        role = self.user_role

        if role in self.USER_ROLES:
            permissions = self.USER_ROLES.get(role)
        elif type(role) == int: # if role is specified as an int, e.g. 6 -> EXEC (2**2) and WRITE (2**1)
            try:
                Permission(role)
            except ValueError:
                pass
            else:
                permissions = role

        return Permission(permissions)

    def _validate_permission(self, permssion):
        if permssion not in self.permissions:
            raise PermissionError(f"User does not have {permssion.name} permission.")

    def read(self, file="script.py"):
        self._validate_permission(Permission.READ)

        with open(file) as f:
            return f.read()

    def write(self, file="script.py", content=""):
        self._validate_permission(Permission.WRITE)

        with open(file, "w") as f:
            f.write(content)
            print(f"Wrote '{content}' to {file}.")

    def execute(self, file="script.py"):
        self._validate_permission(Permission.EXEC)

        exec(open(file).read())

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', user_role='{self.user_role}')"


class User(BaseUser):
    def __init__(self, name, user_role):
        self.name = name
        self.user_role = user_role

        self.permissions = self._infer_permission()
