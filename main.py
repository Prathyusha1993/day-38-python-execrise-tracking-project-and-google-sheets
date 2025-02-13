import os
from dotenv import load_dotenv
import requests
from datetime import datetime

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


# storing workout data to google sheet
today_date = datetime.now().strftime('%d/%m/%y')
now_time = datetime.now().strftime('%X')

shetty_endpoint = os.getenv('SHETTY_ENDPOINT')
for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    # with no authentication
    # shetty_response = requests.post(url=shetty_endpoint, json=sheet_inputs)
    # print(shetty_response.text)

    # with basic authentication
    authorization_header = {
        'Authorization': os.getenv('AUTH_HEADER')
    }
    sheet_response = requests.post(url=shetty_endpoint, json=sheet_inputs, auth=(os.getenv('MY_USERNAME'),  os.getenv('MY_PASSWORD')))
    print(sheet_response.text)