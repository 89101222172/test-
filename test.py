from api import Moyklass
from settings import valid_email, valid_password
from settings import val_id, val_name, val_phone,val_email


m = Moyklass()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = m.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_manager(id=val_id, name=val_name, phone=val_phone, email=val_email):
    status, result = m.get_api_managers(id, name, phone, email)
    assert status == 200
    assert isinstance(result, object)
    assert 'api_managers' in result