from flask import Blueprint, request, jsonify
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

RM = ResponseManager()
bp = Blueprint("users",__name__, url_prefix="/users")
user_schema = UserSchema()
user_model = ModelFactory.get_models("user")

@bp.route("/login", methods=["POST"])
def login ():
    data = request.json
    email = data.get ("email",None)
    password= data.get ("password",None)
    if not email or not password:
        return RM.error ("Es necesario enviar todas las credenciales")
    user =user_model.get_by_email_password(email,password)
    if not user:
        return RM.error ("No se encontro un usuario")
    return RM.success(({"user":user, "token":create_access_token(user)["_id"]}))

@bp.route("/register",methods= ["POST"])
def register():
    try:
        data =user_schema.load(request.json)
        user_id =user_model.create(data)
        return RM.success ({"user_id":str(user_id), "token": create_access_token(srt(user_id))})
    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrecto")
    
@bp.record("/update",methods= ["PUT"])
@jwt_required()
def update(user_id):
    user_id =get_jwt_identity()
    try:
        data =user_schema.load (request)
        user= user_model.update()
        return RM.success({"data": user})
    except ValidationError as err:
        return RM.error ("Los pAarametros enviados son incorrectos")
    
@bp.route("/delate/<string:user_id>",methods= ["DELATE"])
@jwt_required()
def delate (user_id):
    user_id =get_jwt_identity()
    user_model.delate(ObjectId(user_id))
    return RM.success("Usuario eliminado con exito")

@bp.record("/get",methods= ["GET"])
@jwt_required()
def get_user (user_id):
    user_id =get_jwt_identity()
    user =user_model.find_by_id(ObjectId(user_id))
    return RM.success(user)












