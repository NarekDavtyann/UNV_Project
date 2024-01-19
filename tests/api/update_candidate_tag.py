from lib.api.api_helper import put
from lib.api.api_endpoints import url, candidate_tag, bearer_token_superuser

main_url = (url + candidate_tag)
payload = {"candidateId": 5000662, "tag": {
    "tableCode": "Test1",
    "code": "tag"}
  }

put(url=main_url, payload=payload, token=bearer_token_superuser)

