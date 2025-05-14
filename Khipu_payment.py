import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("No se encontró la API_KEY en las variables de entorno")

payload = {
    "amount": 10000,
    "currency": "CLP",
    "subject": "Cobro para Brandom"
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

url = "https://payment-api.khipu.com/v3/payments"

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Error en la petición: {e}")
    if response is not None:
        print(f"Código de estado: {response.status_code}")
        try:
            error_data = response.json()
            print(f"Mensaje de error: {error_data}")
        except json.JSONDecodeError:
            print(f"Cuerpo de la respuesta de error: {response.text}")