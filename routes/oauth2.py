from flask.views import MethodView
from routes.blueprints import skan_blp as blp
from schemas import Oauth2SchemaPost
from controllers.googleapis import oauth2_post


@blp.route("/oauth2.googleapis.com/token")
class Oauth2(MethodView):
    """
    implementation of first request(auth)
    get network_user_id(client_id) + long live token create short live token and
    enter it to db for all records with token(implement by add record with mapping between short live token and
    network_user_id + app_id)
    return short live token
    """
    @blp.arguments(Oauth2SchemaPost)
    def post(self, body_data):
        return oauth2_post(dict(body_data))
