from marshmallow import Schema, fields, validate

class FavoritePokemonSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre del Pokémon favorito es requerido"
        }
    )
    type = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El tipo de Pokémon favorito es requerido"
        }
    )
    favorite_move = fields.Str(
        required=False,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El movimiento favorito del Pokémon es requerido"
        }
    )
    is_legendary = fields.Bool(
        required=False,
        default=False,
        error_messages={
            "required": "La información sobre si es legendario es requerida"
        }
    )