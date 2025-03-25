from marshmallow import Schema, fields, validates, ValidationError

class PokemonSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre del Pokémon es requerido"
        }
    )
    type = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El tipo del Pokémon es requerido"
        }
    )
    abilities = fields.List(
        fields.Str(),
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "Las habilidades del Pokémon son requeridas"
        }
    )