from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleTokensModel
from uuid import uuid4


def generate_slt(llt, length):
    return llt[0] + uuid4().hex[:length - 1]


def oauth2_post(body_data):
    """
    logic imp of second request:
    get network_user_id and token and return short_live_token
    :param body_data:
    :return:
    """
    try:
        relevant_data = {'network_user_id': body_data['client_id'], 'access_token': body_data['refresh_token']}

        check = GoogleTokensModel.query.filter_by(**relevant_data).first()
        if not check:
            abort(404, message="No matching key found")

        short_live_token = generate_slt(relevant_data['access_token'], 10)
        relevant_data['access_token'] = short_live_token
        relevant_data['app_id'] = check.app_id

        data = GoogleTokensModel(**relevant_data)
        db.session.add(data)
        db.session.commit()

    except SQLAlchemyError:
        abort(400, message="An error occurred while getting token")

    return {'access_token': short_live_token}
