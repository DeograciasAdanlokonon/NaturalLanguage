import requests
import datetime as dt

# Query to use in Nutritionix parameter
query = input("Tell me which exercises you did: ")

# Set datetime
now = dt.datetime.now()

# Go to the Nutritionix API (https://www.nutritionix.com/business/api) website and select "Get Your API Key"
# to sign up for a free account and set your APP_ID and API_KEY.
APP_ID = "YOUR NUTRITIONIX APP_ID"
API_KEY = "YOUR NUTRITIONIX API_KEY"


#  Log into https://sheety.co/ with your Google Account. Make sure you give Sheety permission to access your
#  Google sheets. If you miss this step, log out of Sheety and log in again
SHEETY_TOKEN = "YOUR SHEETY BASIC TOKEN"   # Use Sheety documentation https://sheety.co/docs/authentication.html


# Set endpoints
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "your_sheety_endpoint"


# Nutritionix params and headers (Use Nutritionix API Documentation)
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
nutritionix_params = {
    "query": query
}

# Sheety headers
sheety_headers = {"Authorization": SHEETY_TOKEN}


# TODO: 1- Make request on Nutritionix API
response = requests.post(nutritionix_endpoint, json=nutritionix_params, headers=headers)
data = response.json()
new_post_data = data['exercises']

# TODO: 2- Catch data into a dictionary and make Sheety request
for item in new_post_data:
    sheety_params = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories']
        }
    }
    new_post = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(new_post.text)  # print a dictionary for each line inserted in your Google sheet


