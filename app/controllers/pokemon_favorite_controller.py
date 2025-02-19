#crea
#elimina
#get one
#modificar la clase dde modelo y evitar que se usen metodos indevidoss

from flask import Blueprint, request, jsonify
from app.schemas.pokemonsfav_schema import PokemonFavoritoSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons_favoritos", __name__, url_prefix="/pokemons_favoritos")
pokemon_favorito_schema = PokemonFavoritoSchema()
pokemon_favorito_model = ModelFactory.get_models("pokemon_favorito")

@bp.route("/create", methods=["POST"])
def create_pokemon_favorito():
    try:
        data = pokemon_favorito_schema.load(request.json)
        pokemon_id = pokemon_favorito_model.create(data)
        return jsonify({"pokemon_favorito_id": str(pokemon_id)}, 200)
    except ValidationError as err:
        return jsonify({"error": "Los parámetros enviados son incorrectos", "details": err.messages}, 400)


@bp.route("/delete/<string:pokemon_favorito_id>", methods=["DELETE"])
def delete_pokemon_favorito(pokemon_favorito_id):
    try:
        pokemon_favorito_model.delete(ObjectId(pokemon_favorito_id))
        return jsonify("Pokemon favorito eliminado con éxito", 200)
    except Exception as e:
        return jsonify({"error": f"Hubo un error al eliminar: {str(e)}"}, 400)


@bp.route("/get/<string:pokemon_favorito_id>", methods=["GET"])
def get_pokemon_favorito(pokemon_favorito_id):
    try:
        pokemon_favorito = pokemon_favorito_model.find_by_id(ObjectId(pokemon_favorito_id))
        if not pokemon_favorito:
            return jsonify({"error": "Pokemon favorito no encontrado"}), 404
        return jsonify(pokemon_favorito, 200)
    except Exception as e:
        return jsonify({"error": f"Hubo un error al obtener el pokemon favorito: {str(e)}"}, 400)





















































