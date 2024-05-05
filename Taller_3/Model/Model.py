import requests
import json

url = "https://www.datos.gov.co/resource/ynam-yc42.json?$query=SELECT%20cole_nombre_establecimiento%2C%20punt_global%2C%20punt_lectura_critica%2C%20punt_matematicas%2C%20punt_c_naturales%2C%20punt_sociales_ciudadanas%2C%20punt_ingles%20LIMIT%20200"

response = requests.get(url)

data = response.json()

print(json.dumps(data, indent=4))