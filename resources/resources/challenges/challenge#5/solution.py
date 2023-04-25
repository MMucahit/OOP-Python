class DNABase:
    def __init__(self, nucleotide):
        self.base = nucleotide

    @staticmethod
    def _validate_and_standardize(base):
        allowed = [('a', 'adenine'), ('c', 'cytosine'), ('g', 'guanine'), ('t', 'thymine')]

        for b in allowed:
            if base.lower().strip() in b:
                return b[1]

        return False

    def set_base(self, base):
        valid_base = self._validate_and_standardize(base)

        if valid_base:
            self._base = valid_base
        else:
            raise ValueError(f"{base} is not a recognized DNA nucleotide")

    def get_base(self):
        return self._base

    base = property(fget=get_base, fset=set_base)

    def __repr__(self):
        return f"{type(self).__name__}(nucleotide='{self.base}')"
