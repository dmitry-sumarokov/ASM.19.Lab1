class MenuItem:
    id: int = None
    label: str = None
    function: classmethod = None

    def __init__(self, id, label, function):
        self.id = id
        self.label = label
        self.function = function

