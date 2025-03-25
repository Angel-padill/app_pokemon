from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.schemas.pokemonsfav_schema import PokemonFavoritoSchema 
from bson import ObjectId
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from app.models.factory import FP_MODEL 
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token


bp = Blueprint("favorite_pokemon",__name__, url_prefix="/favorite-pokemons")
RM = ResponseManager
FP_MODEL = ModelFactory.get_models("po0kemon_favorites")
FP_SCHEMA = PokemonFavoritoSchema()

@bp.route("/", method=["POST"])
@jwt_required()
def create():
    try:
        data =request.json
        data= FP_SCHEMA.validate(data)
        fp= FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print (err)
        return RM.error("Es necesario enviar todos los parametros")

@bp.route("/<string:user_id>",methods=["DELETE"])
@jwt_required()
def delete (id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")

@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = FP_MODEL.find_all(user_id)
    return ResponseManager.success(data)



















































