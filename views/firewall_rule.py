from typing import Optional

from flask_apispec import doc, use_kwargs, marshal_with, MethodResource

from db import db_manager, FirewallRule
from schemas import FWRuleIdSchema, FWRuleIdOptionalSchema, FWRuleCreateSchema, FWRuleResponseSchema


class FirewallRuleAPI(MethodResource):
    @doc(description='List all existing firewall rules or get a specific one.', tags=['Firewall Rules'])
    @use_kwargs(FWRuleIdOptionalSchema, location='query')
    @marshal_with(FWRuleResponseSchema(many=True), code=200)
    def get(self, rule_id: Optional[str] = None):
        fw_rule = db_manager.get_rows(FirewallRule, row_id=rule_id)
        return fw_rule, 200

    @doc(description='Create a new firewall rule.', tags=['Firewall Rules'])
    @use_kwargs(FWRuleCreateSchema, location='json')
    @marshal_with(FWRuleResponseSchema, code=201)
    def post(self, **request_body):
        fw_rule = db_manager.create_row(FirewallRule, request_body)
        return fw_rule, 201

    @doc(description='Delete an existing firewall rule.', tags=['Firewall Rules'], responses={'204': 'No Content'})
    @use_kwargs(FWRuleIdSchema, location='query')
    def delete(self, rule_id: str):
        db_manager.delete_row(FirewallRule, rule_id)
        return None, 204

    @doc(description='Update an existing firewall rule.', tags=['Firewall Rules'])
    @use_kwargs(FWRuleIdSchema, location='query')
    @use_kwargs(FWRuleCreateSchema, location='json')
    @marshal_with(FWRuleResponseSchema, code=200)
    def put(self, rule_id: str, **request_body):
        fw_rule = db_manager.update_row(FirewallRule, rule_id, request_body)
        return fw_rule, 200
