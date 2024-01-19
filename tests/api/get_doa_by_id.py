from lib.api.api_helper import get
from lib.api.api_endpoints import url, doa_get, bearer_token_superuser


doa_id = 1744658588051712
main_url = (url + doa_get + str(doa_id))
is_success_expected = True


response = get(url=main_url, token=bearer_token_superuser)

for key, value in response.items():
    if key == 'isSuccess':
        assert value == is_success_expected
        break

doa_actual = response['value']['assignmentsList'][0]['doaId']
is_success_actual = response['isSuccess']

assert is_success_expected == is_success_actual
assert doa_id == doa_actual


