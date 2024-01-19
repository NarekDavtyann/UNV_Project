from lib.api.api_helper import post
from lib.api.api_endpoints import url, candidate_tag, bearer_token_superuser


post(url=(url + candidate_tag), payload={"candidateId": 5000662, "tag": {
    "tableCode": "Test1",
    "code": "tag"
  }
}, token=bearer_token_superuser)

