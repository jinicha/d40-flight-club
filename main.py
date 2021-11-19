import requests
import config

TOKEN = config.TOKEN

headers = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-type": "application/json"
}

print('Welcome to Flight Club!')
print('We find the best flight deals and email you.')
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
email_first_time = input('What is your email? ')
email_second_time = input('Please enter your email one more time. ')
if email_first_time == email_second_time:
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email_first_time
        }
    }
    requests.post(
        url="https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/users",
        json=body,
        headers=headers
    )
    print('You are in the club!')

