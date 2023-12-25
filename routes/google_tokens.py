from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_tokens import *
from services import save_history

blp = Blueprint('token_mapping', __name__, description='Google token related controllers')

""" 
token mapping(get/post) routes
"""


@blp.route("/google_data/token_mapping")
class GoogleToken(MethodView):
    def get(self):
        """
        get tokens according to input(none get all tokens/app_id get all related tokens...)
        """
        params_data = dict(request.args)
        return google_tokens_get(params_data)

    @blp.arguments(GoogleTokensSchemaPost)
    def post(self, body_data):
        """
        add long live token
        """
        return google_tokens_post(body_data)


@blp.after_request
def save_log(response):
    request_data = request.get_json() if request.get_data() else request.args if request.args else None  # SETS THE
    # VARIABLE TO THE DATA OF REQUEST BODY IF THERE IS, OR REQUEST PARAMS IF THERE ARE.
    save_history(request=request_data,
                 request_url=request.url,
                 response=response.get_json(),
                 status=response.status_code)
    return response
