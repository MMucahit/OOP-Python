class Tablet:
    MAX_MEMORY = 1024

    MODEL = {
        'lite':{
            'base_storage': 32,
            'memory': 2
        },
        
        'pro':{
            'base_storage': 64,
            'memory': 3
        },
        
        'max':{
            'base_storage': 128,
            'memory': 4
        }
    }

    def __init__(self, model) -> None:
        self.model = model
        self._base_storage = __class__.MODEL[model]['base_storage'] ## self.MODEL
        self._memory = __class__.MODEL[model]['memory'] ## self.MODEL
        self._added_storage = 0

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.model!r}, {self._base_storage!r}, {self._memory!r}, {self._added_storage!r})'

    def added_storage(self, value):
        if (self._base_storage + value > self.MAX_MEMORY):
            raise ValueError('Total storage should not greater than 1024!')
        
        self._added_storage += value
    
    @property
    def memory(self):
        return self._memory
    
    @property
    def base_storage(self):
        return self._base_storage
    
    @property
    def storage(self):
        return self._base_storage + self._added_storage

    @storage.setter
    def storage(self, memory):
        additional = memory - self._base_storage

        if additional < 0:
            raise ValueError(f'Device memory cannot be lower than the base memory of {self._base_storage}')

        else:
            if memory > self.MAX_MEMORY:
                raise ValueError('Total storage should not greater than 1024!')

            self._added_storage = additional