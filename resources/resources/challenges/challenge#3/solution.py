class Contact:
    def __init__(self, name, last_name, phone=None, email=None, display_mode="masked"):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False

        if (self.email is not None and self.email == other.email) or \
                (self.phone is not None and self.phone == other.phone):
            return True

        return self.name == other.name and self.last_name == other.last_name

    def __hash__(self):
        return hash((self.name, self.last_name, self.phone, self.email))

    def __repr__(self):
        if self.display_mode == "masked":
            return f"Contact(name='{self._obfuscate(self.name)}', last_name='{self._obfuscate(self.last_name)}')"

        return f"Contact(name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', email='{self.email}')"

    def __str__(self):
        return f"{self.last_name[0]}{self.name[0]}"

    def __format__(self, format_spec):
        if format_spec != "masked":
            return f"Contact(name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', email='{self.email}')"

        return repr(self)

    @staticmethod
    def _obfuscate(text):
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)
