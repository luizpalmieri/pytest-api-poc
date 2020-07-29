import requests
from test_utils import *


class TestsPositivos:

    def test_payload_valido(self):
        payload = LambdaPayload("olar", "41984266848")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 200)
        assert(response_data["statusCode"] == 200)
        assert(response_data["body"] == '"Mensagem enviada com sucesso"')

        pretty_print_request(response.request)
        pretty_print_response(response)


