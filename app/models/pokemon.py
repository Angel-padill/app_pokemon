from app import mongo
from app.models.super_clase import SuperClass

class Pokemon(SuperClass):
    def __init__(self):
        super().__init__("pokemons")

    def create(self, data):
        raise NotImplementedError("Los pokemones no se pueden crear")
    
    def delete(self, object_id):
        raise NotImplementedError("Los pokemones no se pueden eliminar")
    
    def update(self, data, object_id):
        raise NotImplementedError("Los pokemones no se pueden actualizar")
    
