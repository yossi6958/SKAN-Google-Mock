from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_config import *

blp = Blueprint('google data', __name__, description='Google DATA related controllers')
"""
configure app routes:
add/edit/delete app+network_user+id json data that contain 1 bucket 
implementation of logic is in controller module
"""


@blp.route("/google_data/data")
class GoogleConfig(MethodView):

    @blp.arguments(GoogleConfigSchemaPost)
    def post(self, body_data):
        return google_config_post(body_data)

    @blp.arguments(GoogleConfigSchemaPut)
    def put(self, body_data):
        return google_config_put(body_data)

    @blp.arguments(GoogleConfigSchemaDelete)
    def delete(self, body_data):
        return google_config_delete(body_data)


@blp.route("/google_data/data/<s>")
class GoogleConfigParams(MethodView):
    def get(self, s):
        return google_config_get(s)
