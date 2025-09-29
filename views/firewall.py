from typing import Optional

from flask_apispec import doc, use_kwargs, marshal_with, MethodResource

from db import db_manager, Firewall
from schemas import FWCreateSchema, FWResponseSchema, FWIdSchema, FWIdOptionalSchema


class FirewallAPI(MethodResource):
    @doc(description='List all existing firewalls or get a specific one.', tags=['Firewalls'])
    @use_kwargs(FWIdOptionalSchema, location='query')
    @marshal_with(FWResponseSchema(many=True), code=200)
    def get(self, firewall_id: Optional[str] = None):
        firewall = db_manager.get_rows(Firewall, row_id=firewall_id)
        return firewall, 200

    @doc(description='Create a new firewall.', tags=['Firewalls'])
    @use_kwargs(FWCreateSchema, location='json')
    @marshal_with(FWResponseSchema, code=201)
    def post(self, **request_body):
        firewall = db_manager.create_row(Firewall, request_body)
        return firewall, 201

    @doc(
        description='Delete an existing firewall.',
        tags=['Firewalls'],
        responses={'204': {'description':'No Content'}}
    )
    @use_kwargs(FWIdSchema, location='query')
    def delete(self, firewall_id: str):
        db_manager.delete_row(Firewall, firewall_id)
        return None, 204

    @doc(description='Update an existing firewall.', tags=['Firewalls'])
    @use_kwargs(FWIdSchema, location='query')
    @use_kwargs(FWCreateSchema, location='json')
    @marshal_with(FWResponseSchema, code=200)
    def put(self, firewall_id: str, **request_body):
        firewall = db_manager.update_row(Firewall, firewall_id, request_body)
        return firewall, 200
