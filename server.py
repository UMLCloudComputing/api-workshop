from flask import Flask, request
import json

app = Flask('api-workshop')

mock_db = {}

@app.route('/users', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users_interaction():
    username = request.args.get('username')
    email = request.args.get('email')
    age = int(request.args.get('age'))
    gpa = float(request.args.get('gpa'))

    status_code = None
    if request.method == 'GET':
        data = {}
        if username in mock_db.keys():
            data = {
                'username': username,
                'email': mock_db[username]['email'],
                'age': mock_db[username]['age'],
                'gpa': mock_db[username]['gpa'],
            }
            status_code = 200
        else:
            status_code = 404
        return app.response_class(
            response=json.dumps(data),
            status=status_code,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if None not in [username, email, age, gpa]:
            mock_db[username] = {
                'email': email,
                'age': age,
                'gpa': gpa,
            }
            status_code = 201
        else:
            status_code = 500
        return app.response_class(status=status_code)
    elif request.method == 'PATCH':
        new_data = {
            'email': email,
            'age': age,
            'gpa': gpa,
        }
        for key in new_data.keys():
            if new_data[key] != None:
                mock_db[username][key] = new_data[key]
        status_code = 200
        return app.response_class(status=200)
    elif request.method == 'DELETE':
        if username in mock_db.keys():
            mock_db.pop(username)
            status_code = 200
        else:
            status_code = 500
        return app.response_class(status=status_code)