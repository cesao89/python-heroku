import base64

USERNAME = 'neotalk_web'
PASSWORD = '1234567890'

def valid_request(request, requiredFields):
        headers = request.headers.get('Authorization')
        authorizationHeader = base64.b64encode(f'{USERNAME}:{PASSWORD}'.encode('utf-8'))
        authorizationHeader = f"Basic {authorizationHeader.decode('utf-8')}"

        re = { 'status': False, 'message': 'Invalid Request', 'code': 400 }
        if headers != authorizationHeader:
            re.update({'message': 'Invalid authorization', 'code': 401})
            return re

        bodyJson = request.get_json()
        if not bodyJson:
            re.update({'message': 'Body not informed.'})
            return re

        for fields in requiredFields:
            if not bodyJson.get(fields):
                re.update({'message': f'Parameter "{fields}" not informed.'})
                return re
        return { 'status': True }

class Chatbot:
    def send_message(self, request):
        required = ['chatSession', 'chatMessage', 'userEmail', 'userMatricula', 'userEmpresa']
        v = valid_request(request, required)
        if not v.get('status'):
            return v, v.get('code')
        
        return {
            "intent": "Intent Mocked",
            "messages": [
                "Oi! tudo bem?", 
                "Você está utilizando a API Mockada!",
                "Aqui você pode testar a renderização de emoji 😊",
                "link [clicando aqui|http://neotalk.net.br]",
                "e [download de arquivo|https://warm-hamlet-47743.herokuapp.com/download/dummy.pdf]"
            ],
            "buttons": ["👍 Curti", "Botão 2", "Botão 3"]
        }, 200


class User:
    def recovery_password(self, request):
        required = ['userEmail']
        v = valid_request(request, required)
        if not v.get('status'):
            return v, v.get('code')
        
        return {
            "status": True,
            "message": "Um e-mail foi enviado para usuário."
        }, 200