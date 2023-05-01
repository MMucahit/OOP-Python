class DNABase:
    def __init__(self, nucleotide) -> None:
        self.base = nucleotide
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(nucleotide={self.base!r})'

    @staticmethod
    def _validate_and_standarize(base):
        allowed = [('a', 'adenine'), ('c', 'cytosine'), ('g', 'guanine'), ('t', 'thymine')]

        for b in allowed:
            if base.lower().strip() in b:
                return b[1]
        
        return False
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        valid_base = self._validate_and_standarize(base)

        if valid_base:
            self._base = valid_base

        else:
            raise ValueError(f'{base} is not a recognized DNA nucleotide')            