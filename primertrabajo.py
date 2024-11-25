import requests

URL = "https://jsonplaceholder.typicode.com/posts/1&quot;"
response = requests.get(URL)

if response.status_code == 200:
     data = response.json()

     print('Solicitud exitosa')
     print('Data:', data)
else:
     print('Error en la solicitud, detalles:', response.text)