from marshmallow import Schema, fields


class PolicyCreateSchema(Schema):
    name = fields.String(required=True, metadata={'example': 'test-policy'})
    firewall_id = fields.String(required=True, metadata={'example': '1'})
    rule_id = fields.String(required=True, metadata={'example': '1'})

class PolicyResponseSchema(Schema):
    id = fields.String(required=True, metadata={'example': '1'})
    name = fields.String(required=True, metadata={'example': 'test-policy'})
    firewall_id = fields.String(required=True, metadata={'example': '1'})
    rule_id = fields.String(required=True, metadata={'example': '1'})

class PolicyIdSchema(Schema):
    policy_id = fields.String(required=True)

class PolicyIdOptionalSchema(Schema):
    policy_id = fields.String()
