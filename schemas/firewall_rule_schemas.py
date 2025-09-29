from marshmallow import Schema, fields

from .utils import validate_ip, validate_action

ALLOWED_ACTIONS = {'Allow', 'Deny'}


class FWRuleCreateSchema(Schema):
    name = fields.String(required=True, metadata={'example': 'test-firewall'})
    protocol = fields.String(required=True, metadata={'example': 'tcp'})
    action = fields.String(required=True, metadata={'example': 'Allow'}, validate=validate_action)
    source_ip = fields.String(
        required=True, metadata={'example': '192.168.1.2'}, validate=validate_ip)
    source_port = fields.String(required=True, metadata={'example': '5000'})
    destination_ip = fields.String(
        required=True, metadata={'example': '192.168.1.3'}, validate=validate_ip)
    destination_port = fields.String(required=True, metadata={'example': '3000'})

class FWRuleResponseSchema(Schema):
    id = fields.String(required=True, metadata={'example': '1'})
    name = fields.String(required=True, metadata={'example': 'test-firewall'})
    protocol = fields.String(required=True, metadata={'example': 'tcp'})
    action = fields.String(required=True, metadata={'example': 'Allow'}, validate=validate_action)
    source_ip = fields.String(
        required=True, metadata={'example': '192.168.1.2'}, validate=validate_ip)
    source_port = fields.String(required=True, metadata={'example': '5000'})
    destination_ip = fields.String(
        required=True, metadata={'example': '192.168.1.3'}, validate=validate_ip)
    destination_port = fields.String(required=True, metadata={'example': '3000'})

class FWRuleIdSchema(Schema):
    rule_id = fields.String(required=True)

class FWRuleIdOptionalSchema(Schema):
    rule_id = fields.String()
