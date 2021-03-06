# from werkzeug.datastructures import FileStorage

from marshmallow import Schema, fields, post_load

from zeus.models import Artifact

from .fields import FileField


class ArtifactSchema(Schema):
    id = fields.UUID(dump_only=True)
    # name can be inferred from file
    name = fields.Str(required=False)
    type = fields.Str(required=False)
    # XXX(dcramer): cant find a way to get marshmallow to handle request.files
    file = FileField(required=False)
    created_at = fields.DateTime(attribute="date_created", dump_only=True)

    @post_load
    def build_instance(self, data):
        return Artifact(**data)
