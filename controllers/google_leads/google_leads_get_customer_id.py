from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleConfigModel, GoogleTokensModel


def google_leads_get_customer_id(req_data, version):
    """
    logic imp of second request:
    get network_user_id + app_id and return list of customers in format customers/<id>
    :param req_data:
    :param version:
    :return:
    """
    if not version == '15':
        abort(400, message="wrong version")
    token_data = GoogleTokensModel.query.filter_by(access_token=req_data['Authorization'].split(" ")[1]).first()
    fix_path = "{}.{}".format(token_data.app_id, token_data.network_user_id)
    data = GoogleConfigModel.query.filter_by(google_path=fix_path).all()

    all_data = [f"customers/{json.loads(item.value)}" for item in data]

    return all_data
