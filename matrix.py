from functools import total_ordering
from math import sqrt, pow

@total_ordering
class Matrix:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __abs__(self) -> float:
        return sqrt(sum([pow(self.x, 2), pow(self.y, 2), pow(self.z, 2)]))

    def __eq__(self, __value) -> bool:
        if isinstance(__value, Matrix):
            if (self.x == __value.x) and (self.y == __value.y) and (self.z == __value.z):
                return True
            
        return False

    def __gt__(self, __value) -> bool:
        if abs(self) > abs(__value):
            return True
    
        return False

    def __mul__(self, __value):
        if isinstance(__value, int) or isinstance(__value, float):
            x = self.x * __value
            y = self.y * __value
            z = self.z * __value
            
            return Matrix(x, y, z)

    def __rmul__(self, __value):
        return self * __value

    def __add__(self, __value):
        if isinstance(__value, Matrix):
            x = self.x + __value.x
            y = self.y + __value.y
            z = self.z + __value.z
            
            return Matrix(x, y, z)
        
        return TypeError("Only Matrix object could be accepted")
    
    def __getitem__(self, __value):
        if isinstance(__value, str) and __value.lower() in ['x', 'y', 'z']:
            return eval(f'self.{__value.lower()}')
        
        return NotImplemented

    def __repr__(self) -> str:
        return f'Matrix({self.x!r}, {self.y!r}, {self.z!r})'
    
    def __len__(self) -> float:
        return self.x + self.y + self.z
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))