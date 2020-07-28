import requests
import json
from test_utils import LambdaPayload
from test_utils import LAMBDA_URL


class TestsPositivos:

    def test_payload_valido(self):
        payload = LambdaPayload("olar", "41984266848")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = json.loads(response.content)

        assert(response.status_code == 200)
        assert(response_data["statusCode"] == 200)
        assert(response_data["body"] == '"Mensagem enviada com sucesso"')