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
def get_interaction(username: str) -> None:
    res = requests.get(build_url({'username': username}))
    data = json.loads(res.content)
    if res.status_code == 200:
        print(f'{username}\'s entry:\n' + json.dumps(data, indent=4))
    else:
        print('Not a valid username!')

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
def delete_interaction(username: str) -> None:
    res = requests.delete(build_url({'username': username}))
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
            username = input('\nEnter a username: ')
            get_interaction(username)
        case '2':
            username = input('\nEnter the new user\'s username: ')
            email = input('Enter the new user\'s email: ')
            age = input('Enter the new user\'s age: ')
            gpa = input ('Enter the new user\'s gpa: ')

            post_interaction({
                'username': username,
                'email': email,
                'age': age,
                'gpa': gpa,
            })
        case '3':
            username = input('\nEnter the username of the user you wish to update: ')
            print('If you wish to not update them just type None.')
            email = input('Enter the new email for the user: ')
            age = input('Enter the new age for the user: ')
            gpa = input('Enter the new gpa for the user: ')

            patch_interaction({
                'username': username,
                'email': email,
                'age': age,
                'gpa': gpa,
            })
        case '4':
            username = input('\nEnter the username of the user you wish to delete: ')
            delete_interaction(username)
        case '5':
            break

    print('')
