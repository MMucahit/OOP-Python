#
#
#
class Tablet:
    MAX_MEMORY = 1024

    MODELS = {
        "lite": {
            "base_storage": 32,
            "memory": 2
        },
        "pro": {
            "base_storage": 64,
            "memory": 3
        },
        "max": {
            "base_storage": 128,
            "memory": 4
        }
    }

    def __init__(self, model):
        model = model.lower().strip()

        if model not in list(self.MODELS.keys()):
            raise ValueError("Unrecognized model")

        specs = self.MODELS[model]

        self.model = model
        self._base_storage = specs["base_storage"]
        self._memory = specs["memory"]
        self._added_storage = 0

    def add_storage(self, additional_storage):
        if self._base_storage + additional_storage > self.MAX_MEMORY:
            raise ValueError(f"Device memory cannot exceed maximum of {self.MAX_MEMORY}")

        self._added_storage = additional_storage

    @property
    def storage(self):
        return self._base_storage + self._added_storage

    @storage.setter
    def storage(self, memory):
        additional = memory - self._base_storage

        if additional < 0:
            raise ValueError(f"Device memory cannot be lower than the base memory of {self._base_storage}")

        if memory > self.MAX_MEMORY:
            raise ValueError(f"Device memory cannot exceed maximum of {self.MAX_MEMORY}")

        self._added_storage = additional

    @property
    def memory(self):
        return self._memory

    @property
    def base_storage(self):
        return self._base_storage

    def __repr__(self):
        return f"Table(model='{self.model}', base_storage='{self.base_storage}', added_storage='{self._added_storage}', memory='{self.memory}')"
