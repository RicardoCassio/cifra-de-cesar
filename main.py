import json
import requests
import hashlib

r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=MEU-TOKEN-CODENATION')

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if r.status_code == 200:
    codenation_data = json.loads(r.content)

    ncasas = codenation_data['numero_casas']
    texto_decifrado = ''
    texto_cifrado = codenation_data['cifrado']

    for ch in texto_cifrado:
        if ch not in alfabeto:
            texto_decifrado += ch
        if ch in alfabeto:
            idx = alfabeto.find(ch) - ncasas
            texto_decifrado += alfabeto[idx]

    hash_texto_decifrado = hashlib.sha1(str(texto_decifrado).encode('utf-8')).hexdigest()
    
    
    
    codenation_data['decifrado'] = texto_decifrado
    codenation_data['resumo_criptografico'] = hash_texto_decifrado

    with open('answer.json', 'w') as j:
        json.dump(codenation_data, j)

answer = {'answer': open('answer.json','rb')}
submit = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=MEU-TOKEN-CODENATION', files=answer)
print(submit.status_code, submit.reason)
    
    