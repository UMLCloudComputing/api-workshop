from urllib.parse import urlencode, urlunsplit, urlsplit
import requests
import json

SERVER_URL = 'http://localhost:5000/users'

# Function to build the URL with query params 
def build_url(query_params: dict) -> str:
    query_string = urlencode(query_params)
    split_url = list(urlsplit(SERVER_URL))
    split_url[3] = query_string
    return urlunsplit(split_url)

# Code that does a GET interaction with the endpoint
def get_interaction(email: str) -> None:
    res = requests.get(build_url({'email': email}))
    data = json.loads(res.content)
    if res.status_code == 200:
        print(f'{email}\'s entry:\n' + json.dumps(data, indent=4))
    else:
        print('Not a valid email!')

# Code that does a POST interaction with the endpoint
def post_interaction(user_data: dict) -> None:
    res = requests.post(build_url(user_data))
    if res.status_code == 201:
        print('Successfully created!')
    else:
        print('Failed to create...')

# Code that does a PATCH interaction with the endpoint
def patch_interaction(user_data: dict) -> None:
    filtered_data = {}
    print(user_data)
    for key in user_data.keys():
        if user_data[key] != 'None':
            filtered_data[key] = user_data[key]
    res = requests.patch(build_url(filtered_data))
    if res.status_code == 200:
        print('Successfully updated!')
    else:
        print('Failed to update...')

# Code that does a DELETE interaction with the endpoint
def delete_interaction(email: str) -> None:
    res = requests.delete(build_url({'email': email}))
    if res.status_code == 200:
        print('Successfully deleted!')
    else:
        print('Failed to delete...')

print('Making API Rquests Demo')
print('Please make sure the server flash app is running to proceed!')

while True:
    print('1) GET Request')
    print('2) POST Request')
    print('3) PATCH Request')
    print('4) DELETE Request')
    print('5) Quit')
    choice = input('Select an option from the menu (enter the number): ')

    match choice:
        case '1':
            email = input('\nEnter an email: ')
            get_interaction(email)
        case '2':
            email = input('\nEnter the new user\'s email: ')
            name = input('Enter the new user\'s name: ')
            major = input('Enter the new user\'s major: ')
            year = input ('Enter the new user\'s year: ')

            post_interaction({
                'email': email,
                'name': name,
                'major': major,
                'year': year,
            })
        case '3':
            email = input('\nEnter the email of the user you wish to update: ')
            print('If you wish to not update them just type None.')
            major = input('Enter the new major for the user: ')
            year = input('Enter the new year for the user: ')

            patch_interaction({
                'email': email,
                'name': 'None',
                'major': major,
                'year': year,
            })
        case '4':
            email = input('\nEnter the email of the user you wish to delete: ')
            delete_interaction(email)
        case '5':
            break
        case _:
            print('\nInvalid option!')

    print('')
