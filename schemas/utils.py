from ipaddress import ip_address, IPv4Address

from marshmallow import ValidationError

ALLOWED_ACTIONS = {'Allow', 'Deny'}


def validate_ip(ip):
    # return True
    if isinstance(ip_address(ip), IPv4Address):
        return True
    else:
        raise ValidationError('Ip port value provided is of incorrect format.')
    
def validate_action(action):
    if action in ALLOWED_ACTIONS:
        return True
    else:
        raise ValidationError(f'Incorrect action provided; allowed values: {ALLOWED_ACTIONS}')