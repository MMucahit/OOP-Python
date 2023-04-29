class Contact:
    def __init__(self, name, lastName, phone='', email='', display_mode = 'masked') -> None:
        self.name = name
        self.lastName = lastName
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        if self.display_mode == 'masked':
            return f'{class_name}({self._obfuscate(self.name)!r}, {self._obfuscate(self.lastName)!r}, {self._obfuscate(self.phone)!r}, {self._obfuscate(self.email)!r}, {self.display_mode!r})'
    
        return f'{class_name}({self.name!r}, {self.lastName!r}, {self.phone!r}, {self.email!r}, {self.display_mode!r})'
    
    def __str__(self) -> str:
        return f'{self.lastName[0]}{self.name[0]}'
    
    """If name and lastName are same those objects same. 
       Or Email and phone are not empty and same those objects are same.
    """
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Contact):
            return False

        if self.name == __value.name and self.lastName == __value.lastName:
            return True
        else:
            if self.email != '' and self.phone != '' and __value.email != '' and __value.phone != '':
                if self.email == __value.email and self.phone == __value.phone:
                    return True
            return False
    
    def __hash__(self) -> int:
        return hash((self.name, self.lastName, self.phone, self.email))

    def __format__(self, __format_spec: str) -> str:
        class_name = type(self).__name__
        if __format_spec != 'masked':
            return f'{class_name}({self.name!r}, {self.lastName!r}, {self.phone!r}, {self.email!r}, {self.display_mode!r})'
        else:
            return repr(self)
    
    @staticmethod
    def _obfuscate(text):
        half_lenght = len(text) // 2
        return text[:half_lenght] + '*' *(half_lenght + 1)