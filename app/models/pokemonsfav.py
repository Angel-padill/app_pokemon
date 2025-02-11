from app import mongo 

class pokemonsfav:
    collection = mongo.db.pokemonsfav

    @staticmethod
    def find_all():
        pokemonsfav = pokemonsfav.collection.find()
        return list(pokemonsfav)
    
    @staticmethod
    def find_by_id(pokemonsfav_id):
        pokemonsfav = pokemonsfav.collection.fin_one({
            "_id": pokemonsfav_id
        })
        return pokemonsfav
    


    @staticmethod
    def create(data):
        pokemonsfav = pokemonsfav.collection.insert_one(data)
        return pokemonsfav.inserted_id
    


    @staticmethod
    def update(pokemonsfav_id, data):
        pokemonsfav = pokemonsfav.collection.update_one({
            "_id": pokemonsfav_id
        },{
            "$set": data
        })
        return pokemonsfav

       
       
    @staticmethod
    def delete(pokemonsfav_id):
        return pokemonsfav.collection.delete_one({"_id": pokemonsfav_id})

















































