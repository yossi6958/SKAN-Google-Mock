from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleConfigModel, GoogleTokensModel


def google_leads_get_customer_client(req_data, version, id):
    """
    :param req_data:
    :param version:
    :param id: id can be customer is or customer client id
    :return: response according to given input
     """
    if not version == '15':
        abort(400, message="wrong version")
    token_data = GoogleTokensModel.query.filter_by(access_token=req_data['Authorization'].split(" ")[1]).first()
    if "Login-Customer-Id" in list(req_data.keys()):
        fix_path = "{}.{}.{}.{}".format(token_data.app_id, token_data.network_user_id, req_data['Login-Customer-Id'],
                                        id)
    else:
        fix_path = "{}.{}.{}".format(token_data.app_id, token_data.network_user_id, id)

        # print(req_data)
    # print(fix_path)
    data = GoogleConfigModel.query.filter_by(google_path=fix_path).all()

    if "Login-Customer-Id" in list(req_data.keys()):

        results = []
        for item in data:
            all_path = fix_path + ".{}".format(json.loads(item.value))
            campaign_data = GoogleConfigModel.query.filter_by(google_path=all_path).first()
            campaign_data_dict = json.loads(campaign_data.value)

            dict_all_params = {
                "campaign_id": "UNAVAILABLE",
                "name": "UNAVAILABLE",
                "skAdNetworkAdEventType": "UNAVAILABLE",
                "skAdNetworkAttributionCredit": "UNAVAILABLE",
                "skAdNetworkInstalls": "UNAVAILABLE",
                "skAdNetworkPostbackSequenceIndex": "UNAVAILABLE",
                "skAdNetworkSourceType": "UNAVAILABLE",
                "skAdNetworkTotalConversions": "UNAVAILABLE",
                "skAdNetworkUserType": "UNAVAILABLE"
            }
            if type(campaign_data_dict) == dict:
                dict_all_params |= campaign_data_dict

            final_data = {"segments": {
                "skAdNetworkAttributionCredit": dict_all_params['skAdNetworkAttributionCredit'],
                "skAdNetworkAdEventType": dict_all_params['skAdNetworkAdEventType'],
                "skAdNetworkPostbackSequenceIndex": dict_all_params['skAdNetworkPostbackSequenceIndex'],
                "skAdNetworkSourceType": dict_all_params['skAdNetworkSourceType'],
                "skAdNetworkUserType": dict_all_params['skAdNetworkUserType']
            },
                "campaign": {
                    "appCampaignSetting": {"appId": token_data.app_id},
                    "name": dict_all_params["name"],
                    "resourceName": f"customers/{id}/campaigns/{json.loads(item.value)}",
                    "id": json.loads(item.value)
                },
                "metrics": {
                    "skAdNetworkTotalConversions": dict_all_params['skAdNetworkTotalConversions'],
                    "skAdNetworkInstalls": dict_all_params['skAdNetworkInstalls']
                }
            }
            results.append(final_data)
        return_data = {'results': results}


    else:
        return_data = [{"customerClient": {
            "clientCustomer": f"customers/{id}",
            "resourceName": f"customers/{id}/customerClients/{json.loads(item.value)}"
        }} for item in data]

    return return_data
