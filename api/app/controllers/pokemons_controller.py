from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required

bp = Blueprint("pokemon", __name__, url_prefix="/pokemons")
RM = ResponseManager
POKEMON_MODEL = ModelFactory.get_models("pokemon")

@bp.route("/", methods=["POST"])
@jwt_required()
def create_pokemon():
    try:
        data = request.json
        pokemon_id = POKEMON_MODEL.create(data)
        return RM.success({"_id": pokemon_id})
    except Exception as err:
        print(err)
        return RM.error("Error al crear el Pokémon")

@bp.route("/<string:pokemon_id>", methods=["DELETE"])
@jwt_required()
def delete_pokemon(pokemon_id):
    try:
        POKEMON_MODEL.delete(ObjectId(pokemon_id))
        return RM.success("Pokémon eliminado con éxito")
    except Exception as err:
        print(err)
        return RM.error("Error al eliminar el Pokémon")

@bp.route("/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    try:
        pokemon = POKEMON_MODEL.find_by_id(ObjectId(pokemon_id))
        if pokemon:
            return RM.success(pokemon)
        else:
            return RM.error("Pokémon no encontrado", 404)
    except Exception as err:
        print(err)
        return RM.error("Error al obtener el Pokémon")

@bp.route("/user/<string:user_id>", methods=["GET"])
@jwt_required()
def get_user_pokemons(user_id):
    try:
        pokemons = POKEMON_MODEL.find_all_by_user(user_id)
        return RM.success(pokemons)
    except Exception as err:
        print(err)
        return RM.error("Error al obtener los Pokémon del usuario")