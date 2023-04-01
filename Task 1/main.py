import requests

url = 'https://randomuser.me/api/?results=100&gender=male'

response = requests.get(url)
response_json = response.json()


male_users = [
    {
        'full_name': f'{user["name"]["first"]} {user["name"]["last"]}',
        'email': user['email'],
        'gender':  user['gender']
    } for user in response_json['results']
]

for user in male_users:
    print(user)
    print()
