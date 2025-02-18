from marshmallow import Schema, fields, ValidateError

class UserSchema(Schema):
    name= fields.Str(
        required=True,
        validate=lambda x :len (x)> 0,
        error_messages={
            "required":"El nombre es requerido"
        }
    )
    password= fields.Str(
        required=True,
        validate=lambda x :len (x)> 0,
        error_messages={
            "required":"La conytraseña es requerida"
        }
    )
    email=fields.Str(
        required=True,
        validate=lambda x :"@utma.edu.mx" in x,
        error_messages={
            "required":"El nombre es requerido"
        }
    )