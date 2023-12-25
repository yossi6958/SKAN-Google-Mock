from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_leads import *
from flask import request
from schemas import Oauth2SchemaPost

blp = Blueprint('google', __name__, description='google MOCK related controllers')
""" 
request - response routes
"""


@blp.route("/oauth2.googleapis.com/token")
class Oauth2(MethodView):
    @blp.arguments(Oauth2SchemaPost)
    def post(self, body_data):
        return oauth2_post(dict(body_data))


@blp.route("/googleads.googleapis.com/<version>/customers")
class GoogleLeads(MethodView):
    def get(self, version):
        req_data = dict(request.headers)
        return google_leads_get_customer_id(req_data, version)


@blp.route("/googleads.googleapis.com/<version>/customers/<id>/googleAds")
class GoogleLeadsId(MethodView):
    def post(self, version, id):
        req_data = dict(request.headers)
        return google_leads_get_customer_client(req_data, version, id)
