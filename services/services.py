from uuid import uuid4
from models import MockHistoryModel
from db import db
import json


# contain some utils

# for checking query params validation
def is_valid_dict(dictionary, key_tuple):
    invalid_key = None
    for key in dictionary:
        if key not in key_tuple:
            invalid_key = key
            break
    return invalid_key is None, invalid_key


# for generating short-live-token
def generate_slt(llt, length):
    return llt[0] + uuid4().hex[:length - 1]


def save_history(request, request_url, response, status, srn='dummy_srn'):
    save = {
        'srn': srn,
        'request': request if isinstance(request, str) else json.dumps(request),
        # IF THE REQUEST IS STRING, LEAVES IT AS IS, IF NOT, CONVERTS TO STRING.
        'request_url': request_url,
        'response': response if isinstance(response, str) else json.dumps(response),  # SAME AS REQUEST
        'status': status
    }

    data = MockHistoryModel(**save)
    db.session.add(data)
    db.session.commit()
