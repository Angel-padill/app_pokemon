#crea
#elimina
#get one
#modificar la clase dde modelo y evitar que se usen metodos indevidos

from flask import Blueprint, request, jsonify
from app.schemas.pokemons_schema import PokemonSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemon_schema = PokemonSchema()
pokemon_model = ModelFactory.get_models("pokemon")

@bp.route("/create", methods=["POST"])
def create_pokemon():
    try:
        data = pokemon_schema.load(request.json)
        pokemon_id = pokemon_model.create(data)
        return jsonify({"pokemon_id": str(pokemon_id)}, 200)
    except ValidationError as err:
        return jsonify("Los parámetros enviados son incorrectos", 400)


@bp.route("/delete/<string:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    pokemon_model.delete(ObjectId(pokemon_id))
    return jsonify("Pokémon eliminado con éxito", 200)


@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    if not pokemon:
        return jsonify("Pokémon no encontrado", 404)
    return jsonify(pokemon, 200)






















































