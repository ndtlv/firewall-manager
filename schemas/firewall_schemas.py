from marshmallow import Schema, fields

from .utils import validate_ip


class FWCreateSchema(Schema):
    name = fields.String(required=True, metadata={'example': 'test-firewall'})
    ip_address = fields.String(
        required=True, metadata={'example': '192.168.1.1'}, validate=validate_ip)
    location = fields.String(metadata={'example': 'Office-1'})

class FWResponseSchema(Schema):
    id = fields.String(required=True, metadata={'example': '1'})
    name = fields.String(required=True, metadata={'example': 'test-firewall'})
    ip_address = fields.String(
        required=True, metadata={'example': '192.168.1.1'}, validate=validate_ip)
    location = fields.String(metadata={'example': 'Office-1'})

class FWIdSchema(Schema):
    firewall_id = fields.String(required=True)

class FWIdOptionalSchema(Schema):
    firewall_id = fields.String()
