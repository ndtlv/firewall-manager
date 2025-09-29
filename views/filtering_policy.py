from typing import Optional

from flask_apispec import doc, use_kwargs, marshal_with, MethodResource

from db import db_manager, FilteringPolicy
from schemas import (
    PolicyCreateSchema, PolicyResponseSchema, PolicyIdSchema, PolicyIdOptionalSchema,
    FWResponseSchema, FWRuleResponseSchema)


class FilteringPolicyAPI(MethodResource):
    @doc(description='List all existing filtering policies or get a specific one.', tags=['Filtering Policies'])
    @use_kwargs(PolicyIdOptionalSchema, location='query')
    @marshal_with(PolicyResponseSchema(many=True), code=200)
    def get(self, policy_id: Optional[str] = None):
        policy = db_manager.get_rows(FilteringPolicy, row_id=policy_id)
        return policy, 200

    @doc(description='Create a new filtering policy.', tags=['Filtering Policies'])
    @use_kwargs(PolicyCreateSchema, location='json')
    @marshal_with(PolicyResponseSchema, code=201)
    def post(self, **request_body):
        policy = db_manager.create_row(FilteringPolicy, request_body)
        return policy, 201

    @doc(
        description='Delete an existing filtering policy.',
        tags=['Filtering Policies'],
        responses={'204': 'No Content'}
    )
    @use_kwargs(PolicyIdSchema, location='query')
    def delete(self, policy_id: str):
        db_manager.delete_row(FilteringPolicy, policy_id)
        return None, 204

    @doc(
        description='Update an existing filtering policy.',
        tags=['Filtering Policies'],
    )
    @use_kwargs(PolicyIdSchema, location='query')
    @use_kwargs(PolicyCreateSchema, location='json')
    @marshal_with(PolicyResponseSchema, code=200)
    def put(self, policy_id: str, **request_body):
        policy = db_manager.update_row(FilteringPolicy, policy_id, request_body)
        return policy, 200


class FilteringPolicyFirewallAPI(MethodResource):
    @doc(description='Get a firewall associated with certain policy', tags=['Filtering Policies'])
    @marshal_with(FWResponseSchema, code=200)
    def get(self, policy_id: str):
        firewall = db_manager.get_row(FilteringPolicy, row_id=policy_id, return_field='firewall_id')
        return firewall, 200


class FilteringPolicyFWRuleAPI(MethodResource):
    @doc(description='Get a firewall rule associated with certain policy', tags=['Filtering Policies'])
    @marshal_with(FWRuleResponseSchema, code=200)
    def get(self, policy_id: str):
        rule = db_manager.get_row(FilteringPolicy, row_id=policy_id, return_field='rule_id')
        return rule, 200