from flask_smorest import abort
from models import GoogleTokensModel


def google_tokens_get(params_data):

    data = GoogleTokensModel.query.filter_by(**params_data).all()  # same as: filter_by(app_id=body_data['app_id'], ...)
    if not data:
        abort(404, message="No matching key found")

    result_list = [{'app_id': item.app_id, 'network_user_id': item.network_user_id, 'access_token': item.access_token} for item in data]
    return result_list
