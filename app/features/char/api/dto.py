from flask_restplus import Namespace, fields
from marshmallow import Schema
from marshmallow import field as ma_fields
from marshmallow import post_load

from .models import Char


class CharDto:
    api = Namespace(
        'character', description='Ações relacionadas ao personagem')

    new_char = api.model('New Character',
                         {'name': fields.String(required=True)})
