from app import mongo 

class user:
    collection = mongo.db.users

    @staticmethod
    def find_all():
        users = users.collection.find()
        return list(users)
    
    @staticmethod
    def find_by_id(users_id):
        users= users.collection.fin_one({
            "_id": users_id
        })
        return users
    


    @staticmethod
    def create(data):
        users = users.collection.insert_one(data)
        return users.inserted_id
    


    @staticmethod
    def update(users_id, data):
        users = users.collection.update_one({
            "_id": users_id
        },{
            "$set": data
        })
        return users

       
       
    @staticmethod
    def delete(users_id):
        return user.collection.delete_one({"_id": users_id})

















































