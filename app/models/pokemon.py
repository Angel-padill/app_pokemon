from app import mongo 

class pokemon:
    collection = mongo.db.pokemons

    @staticmethod
    def find_all():
        pokemons = pokemon.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = pokemon.collection.fin_one({
            "_id": pokemon_id
        })
        return pokemon
    


    @staticmethod
    def create(data):
        pokemon = pokemon.collection.insert_one(data)
        return pokemon.inserted_id
    


    @staticmethod
    def update(pokemon_id, data):
        pokemon = pokemon.collection.update_one({
            "_id": pokemon_id
        },{
            "$set": data
        })
        return pokemon

       
       
    @staticmethod
    def delete(pokemon_id):
        return pokemon.collection.delete_one({"_id": pokemon_id})
