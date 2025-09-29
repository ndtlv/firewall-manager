from ipaddress import ip_address, IPv4Address

from marshmallow import ValidationError

ALLOWED_ACTIONS = {'Allow', 'Deny'}


def validate_ip(ip: str):
    if isinstance(ip_address(ip), IPv4Address):
        return True
    else:
        raise ValidationError('Ip address value provided is of incorrect format.')
    
def validate_action(action: str):
    if action in ALLOWED_ACTIONS:
        return True
    else:
        raise ValidationError(f'Incorrect action provided; allowed values: {ALLOWED_ACTIONS}')