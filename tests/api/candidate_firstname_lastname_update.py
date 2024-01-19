from lib.api.api_endpoints import bearer_token_superuser, candidate_profile_put, url, candidate_profile_get
from lib.api.request_body import candidate_update_payload
from lib.api.api_helper import get, put
from lib.Helpers.helpers import random_file_name, random_numbers

main_url_put = (url + candidate_profile_put)
user_id = 5000686
main_url_get_candidate = (url + candidate_profile_get + str(user_id))

initial_first_name = ''
initial_last_name = ''
get_candidate = get(url=main_url_get_candidate, token=bearer_token_superuser)
initial_first_name += get_candidate['value']['firstName']
initial_last_name += get_candidate['value']['lastName']
new_first_name = random_file_name()
new_last_name = random_file_name()

candidate_update_payload['firstName'] = new_first_name
candidate_update_payload['lastName'] = new_last_name
update_candidate = put(url=main_url_put, token=bearer_token_superuser, payload=candidate_update_payload)
get_updated_candidate = get(url=main_url_get_candidate, token=bearer_token_superuser)
actual_first_name = get_updated_candidate['value']['firstName']
actual_last_name = get_updated_candidate['value']['lastName']

assert initial_first_name != new_first_name and new_first_name == actual_first_name
assert initial_last_name != new_last_name and new_last_name == actual_last_name

