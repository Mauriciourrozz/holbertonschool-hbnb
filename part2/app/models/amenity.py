from basicmodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__
        if type(name) is str and len(name) <= 50:
            self.name = name

