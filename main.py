import os
from dotenv import load_dotenv
import requests

WEIGHT_KG = 63.5
HEIGHT_CM = 167.64
AGE = 31
load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('Tell me which exercise you did:')
parameters = {
    'query': exercise_text,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age':AGE
}
request_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=request_headers)
result = response.json()
print(result)