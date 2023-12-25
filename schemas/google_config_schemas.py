from marshmallow import Schema, fields


class ValuesSchema(Schema):
    skAdNetworkAttributionCredit = fields.Str(required=False)
    skAdNetworkUserType = fields.Str(required=False)
    skAdNetworkPostbackSequenceIndex = fields.Str(required=False)
    skAdNetworkSourceType = fields.Str(required=False)
    skAdNetworkAdEventType = fields.Str(required=False)
    name = fields.Str(required=False)
    skAdNetworkTotalConversions = fields.Str(required=False)
    skAdNetworkInstalls = fields.Str(required=False)
    


class GoogleConfigSchemaGet(Schema):
    app_id = fields.Str(required=False)
    network_user_id = fields.Str(required=False)
    customer_id = fields.Str(required=False)
    customer_client = fields.Str(required=False)
    campaign_id = fields.Str(required=False)


class GoogleConfigSchemaPost(ValuesSchema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=False)
    customer_id = fields.Str(required=False)
    customer_client = fields.Str(required=False)
    campaign_id = fields.Str(required=False)


class GoogleConfigSchemaPut(ValuesSchema):
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    customer_id = fields.Str(required=True)
    customer_client = fields.Str(required=True)
    campaign_id = fields.Str(required=True)


class GoogleConfigSchemaDelete(Schema):
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    customer_id = fields.Str(required=True)
    customer_client = fields.Str(required=True)
    campaign_id = fields.Str(required=True)
