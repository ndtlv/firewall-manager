import logging

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec

from db import db_manager
from error_handlers import error_handlers
from views import FirewallRuleAPI, FirewallAPI, FilteringPolicyAPI, FilteringPolicyFirewallAPI, FilteringPolicyFWRuleAPI


######### Logger config

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(name)s: %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)

######### API server initialisation

app = Flask(__name__)
error_handlers(app)

methods = ['GET', 'POST', 'PUT', 'DELETE']

app.add_url_rule('/firewalls', view_func=FirewallAPI.as_view('firewalls'), methods=methods)
app.add_url_rule('/firewall_rules', view_func=FirewallRuleAPI.as_view('firewall_rules'), methods=methods)
app.add_url_rule('/filtering_policies', view_func=FilteringPolicyAPI.as_view('filtering_policies'), methods=methods)

app.add_url_rule(
    '/filtering_policies/<string:policy_id>/firewall',
    view_func=FilteringPolicyFirewallAPI.as_view('filtering_policies_firewall'), methods=['GET'])
app.add_url_rule(
    '/filtering_policies/<string:policy_id>/firewall_rule',
    view_func=FilteringPolicyFWRuleAPI.as_view('filtering_policies_fw_rule'), methods=['GET'])

######### Swagger configuration

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Firewall Manager API',
        version='v1',
        openapi_version='2.0.0',
        plugins=[MarshmallowPlugin()]
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/docs/'
})

docs = FlaskApiSpec(app)

docs.register(FirewallAPI, endpoint='firewalls')
docs.register(FirewallRuleAPI, endpoint='firewall_rules')
docs.register(FilteringPolicyAPI, endpoint='filtering_policies')
docs.register(FilteringPolicyFirewallAPI, endpoint='filtering_policies_firewall')
docs.register(FilteringPolicyFWRuleAPI, endpoint='filtering_policies_fw_rule')

######### Database connection - setup and teardown

with app.app_context():
    db_manager.init()

@app.teardown_appcontext
def teardown(exception):
    db_manager.close()

######### App start

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)