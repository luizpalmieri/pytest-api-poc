import json

LAMBDA_URL = "TBD"

class LambdaPayload:
    def __init__(self, mensagem, num_destinatario):
        self.mensagem = mensagem
        self.num_destinario = num_destinatario
        self.body = self.construir_body()
        self.header = self.construir_header()

    def construir_body(self):
        return {"mensagem": self.mensagem, "num_destinatario": self.num_destinario}


    def construir_header(self):
        return {'Content-Type': 'application/json'}
