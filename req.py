import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"temperatura":{temp}}, "humedad":"{hum}}"}'.encode()

response = requests.post('http://localhost/add', headers=headers, data=data)
