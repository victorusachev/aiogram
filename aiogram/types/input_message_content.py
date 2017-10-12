import typing

from . import base
from . import fields


class InputMessageContent(base.TelegramObject):
    """
    This object represents the content of a message to be sent as a result of an inline query.

    Telegram clients currently support the following 4 types

    https://core.telegram.org/bots/api#inputmessagecontent
    """
    pass


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    phone_number: base.String = fields.Field()
    first_name: base.String = fields.Field()
    last_name: base.String = fields.Field()

    def __init__(self, phone_number: base.String,
                 first_name: typing.Optional[base.String] = None,
                 last_name: typing.Optional[base.String] = None):
        super(InputContactMessageContent, self).__init__(phone_number=phone_number, first_name=first_name,
                                                         last_name=last_name)


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    latitude: base.Float = fields.Field()
    longitude: base.Float = fields.Field()

    def __init__(self, latitude: base.Float,
                 longitude: base.Float):
        super(InputLocationMessageContent, self).__init__(latitude=latitude, longitude=longitude)


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    message_text: base.String = fields.Field()
    parse_mode: base.String = fields.Field()
    disable_web_page_preview: base.Boolean = fields.Field()

    def __init__(self, message_text: typing.Optional[base.String] = None,
                 parse_mode: typing.Optional[base.String] = None,
                 disable_web_page_preview: typing.Optional[base.Boolean] = None):
        super(InputTextMessageContent, self).__init__(message_text=message_text, parse_mode=parse_mode,
                                                      disable_web_page_preview=disable_web_page_preview)


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Note: This will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    latitude: base.Float = fields.Field()
    longitude: base.Float = fields.Field()
    title: base.String = fields.Field()
    address: base.String = fields.Field()
    foursquare_id: base.String = fields.Field()

    def __init__(self, latitude: typing.Optional[base.Float] = None,
                 longitude: typing.Optional[base.Float] = None,
                 title: typing.Optional[base.String] = None,
                 address: typing.Optional[base.String] = None,
                 foursquare_id: typing.Optional[base.String] = None):
        super(InputVenueMessageContent, self).__init__(latitude=latitude, longitude=longitude, title=title,
                                                       address=address, foursquare_id=foursquare_id)