import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"temperatura":"26.3", "humedad":"61"}\xa0'.encode()

response = requests.post('http://localhost/add', headers=headers, data=data)
