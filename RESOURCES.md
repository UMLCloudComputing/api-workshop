# Tutorial on APIs

Welcome to our tutorial on APIs. In this tutorial, you will learn about what an API is, what REST APIs are, how HTTP requests work, and how you can utilize them in Python. There will also be an optional mini-project that will help you become familiar with Git and use an API of your choosing to create something. 

**Prerequisite Knowledge Required**: [Basic Python Programming](https://learnxinyminutes.com/python/), [Pip Usage](https://www.w3schools.com/python/python_pip.asp)

## What is an API?

API stands for "Application Programming Interface." An API is a way for two pieces of software to be able to communicate with each other using a set of definitions and protocols. There are a ton of different APIs that do a wide array of things from getting weather data to generating trivia questions. You can utilize these in your programs to use the data that they provide. This can save a lot of time and provide a lot of functionality to your programs. 

The way APIs are built is usually in a client server relationship. The client makes requests and the server then responds to those requests. There are also four main ways that an API can be set up. 

#### SOAP APIs

"Simple Object Access Protocol" APIs simply exchange messages in XML format. This type of API was popular in the past however is not used much today.

#### RPC APIs

"Remote Procedure Calls" APIs simply just have the client call a function on the server and then the server responds with the output. 

#### Websocket APIs

Websocket APIs provide two way communication between a client and server. Think of this like being on a phone call with someone. One of you might talk more then the other, one might not talk at all, or you both will talk back and forth. 

#### REST APIs

"Representational State Transfer" APIs are the most popular and important type of API. The client sends a request to the server and the server uses that request to call internal functions and then returns the output. An important thing to note here is that this is done entirely stateless so the server does not remember anything about the client. This is the type of API we will be taking a look at today!

## REST APIs

As mentioned above REST stands for Representational State Transfer. These APIs use methods like GET, POST, DELETE to access or manipulate data on the server. Also as mentioned this is done entirely stateless. This means that the server does not need to remember anything about the clients requests to function. 

### Benefits of Using REST APIs

#### Integration

APIs can be used to integrate new applications with existing software systems. This can speed up the development process because you do not need to build everything from scratch.

#### Expansion
Using APIs can help benefit a lot of different platforms allowing for easy expansion of your service. 

#### Ease of Maintenance
Because an API is like a bridge between services. Each part of the system is obliged to make internal changes so that the API is not impacted.

### Types of REST APIs
There are different types of REST APIs that can be built. 

#### Public

For anybody to use but may require authentication.

#### Private

Used for internal use and is not open to the public. 

#### Partner

These are only accessible by authorized external developers to aid business-to-business partnerships.

#### Composite 

These combine two or more different APIs to address complex system requirements or behaviors. 

### API Security 

There are two main ways to secure a REST API and this is through the use of authentication tokens and API keys. Authentication tokens are used to authorize a user to make API calls. They are used to check if the user making that call is really them. They are given out when you login in to the service with your credentials. Auth tokens also usually expire after some time and will require you to refresh them. A common scheme for this is OAuth. API keys are the other method to secure them and are not as secure as auth tokens. API keys are usually given out to access the API. These all the application to be identified and give it access to the API. These do not expire and usually come in the form of a client id and secret. These also can be used to monitor the activity of the key.

### API Endpoints

API endpoints are the final touch in the communication system. These include server URLs and locations. These endpoints are what services will happen at that location. You will see this more in the Python example below. 

## Basics of HTTP Requests & Responses

One other important element that needs to be understood before getting into the Python examples is the basics of HTTP requests. These are how you will communicate with the API most of the time. 

### Parts of an HTTP Request

There are a few different parts of an HTTP request. These include the request line, the request headers, and the request body. The request line will not be talked about in much detail here besides the methods so if you would like to learn more check out the article below. 

### HTTP Request Methods 

The request method is the method that you intend to interact with on the endpoint. Below are the important ones that you need to know when making requests to REST APIs.

- GET - used to retrieve data from the endpoint. 
- POST - used to send data to an endpoint, data is from the request body or query parameters.
- PUT - used to replace a resource with what is uploaded. 
- PATCH - used to partiially update a resource. 
- DELETE - used to delete a resource. 

### HTTP Request Headers

A request's headers can provide the server with additional information about the client's request. These are important for specifiying different things and a list of them can be found below in the tutorialpoint article about requests. Most of the time the most important ones are `Content-Type` and `Authorization`. `Content-Type` provides informatoin about the encoding of the data in the request and `Authorization` provides the credentials of the client when making requests to protected resources. 

### HTTP Request Body

The request body is where you can provide any data for the request. Most of the time this is where the data you are sending to the server will go. It can be encoded as a JSON or other formats however, JSON is the most common place nowadays.

### Query Parameters

Query parameters are parameters that you can specify at the end of the URL.

```
http://localhost:5000/users?username=johncloudcomputing
```

In the above example, the query parameters are anything after the `?`. They are split into key pair values where this is the format `KEY=VALUE`. You can specify multiple by having a `&` in between them. Special characters like punctuation and braces need to be encoded but there are usually libraries built into most languages standard library that can handle this. 

### Parts of an HTTP Response

Like HTTP requests there are also parts of the response. The parts include the status line, headers, and then the body. The status line contains the status code that has been returned from the server and that is one of the most important parts of a response. The headers include various information for example, how long the client should cache the data contained in the response. The body is just like the HTTP request body and can have a variety of different formats but like requests, JSON is the most popular in modern day. 

### Status Codes

As mentioned previously, status codes are one of the most important parts of a response. They can be used on the client to display errors that might have occured. The codes are formatted in a three digit number where the first digit determines the type. Below are what each digit means:
- 1XX - Informational (Means the request was received and the process is continuing)
- 2XX - Success (Means the action was successfully received, understood, and accepted)
- 3XX - Redirection (Means further action must be taken in order to complete the request)
- 4XX - Client Error (Means the request contains were incorrect or can't be fulfilled)
- 5XX - Server Error (Means the server failed to fulfill an apparently valid request)

The one you are probably most familiar with is 404 or not found. If you want to learn what different codes are in each set check out this page of the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#informational_responses).

To play around with HTTP requests you can use the command line tool [CURL](https://curl.se/) or if you're more of a fan of GUIs you can use something like [Postman](https://www.postman.com/). 

## Calling REST APIs in Python

Now for the fun part of the lesson, how to call web REST APIs in Python. For this section of the lesson we have developed an example for you to follow so please make sure Python is installed on your computer and also that you have downloaded the project is self. This can be done by either using the `git clone` command on git or simply just heading to the repository's page and clicking green code button then download zip.

### Playing Around With The Example

To start the example, you first need to install the dependencies for it. This can be done by running the command. 
```
pip install -r requirements.txt
```
Once you have completed this you should be good to start the example. The first thing you should do is start the mock server by running the following command.
```
python -m flash --app server run
```
Please make sure this window or terminal stays open for the entire time or there will problems. Next if you want to open the visualation that we created for this open up the file `visualization.html`. This is a simple webpage that will show the current status of the database along with a list of all of the transactions that have been made. To start the client to begin making requests simply just run the following command. 
```
python client.py
```
Now play around with making some requests and seeing how the database changes. You can either refresh the page or press the refresh button to see your updates happen. Try to play around with the four methods that are listed.

### Requests Library

Now how does this client make the requests to the server that has been set up. Let's take a look at the `client.py` file for that. For starters, http requests in Python are made with the `requests` library which needs to be installed via pip. The next four sections will explain how each request is made.

### GET Requests

The GET request is simple. Lets take a look at the get interaction function:
```python
# Code that does a GET interaction with the endpoint
def get_interaction(username: str) -> None:
    res = requests.get(build_url({'username': username}))
    data = json.loads(res.content)
    if res.status_code == 200:
        print(f'{username}\'s entry:\n' + json.dumps(data, indent=4))
    else:
        print('Not a valid username!')
```
This function takes a username which to do the get request to. This is taken from standard input before the function is called and then what is typed is passed to this function. This function starts by building the URL to make the get request to. If you would like to see how this function works take a look at the source file but all it is doing is getting the URL in the format that was mentioned about with the query parameters. After that it is using the request library's `get()` function to make a get request at that URL. The return of the that is the response for the request. The first thing that is done after that is turning the body into a json we can use. Then the status code is checked to see if it is 200 which means success and then prints the data if it was valid and an error if not. 

### POST Requests 

Here is the code for the POST request:
```python
# Code that does a POST interaction with the endpoint
def post_interaction(user_data: dict) -> None:
    res = requests.post(build_url(user_data))
    if res.status_code == 201:
        print('Successfully created!')
    else:
        print('Failed to create...')
```
Same kind of procedure as before however the difference this time is the parameter being a dictonary of all of the attributes of a user and what is done with a request. The status code for 201 is made because that is the code for successfully created. Any other status will print an error message.

### PATCH Requests

Here is the code for the PATCH request:
```python
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
```
All of these follow a similar structure however this one checks to see which data to include in the query parameters before making the request. After that the 200 status code is checked to see if the update was successful.

### DELETE Requests

Here is the code for the DELETE request:
```python
# Code that does a DELETE interaction with the endpoint
def delete_interaction(username: str) -> None:
    res = requests.delete(build_url({'username': username}))
    if res.status_code == 200:
        print('Successfully deleted!')
    else:
        print('Failed to delete...')
```
This is pretty much just the same as the GET request just doing delete instead.

For more information on the Python `requests` library check our this [W3 Schools page](https://www.w3schools.com/python/module_requests.asp).

## How to Use Git + Mini Project

The last portion of this lesson will contain a mini project that will help you get familiar with Git and practice what you learned here.   

### Setting Up Development Environment

For this you can use your local machine if you are already familiar with Git and setting up your ssh keys and such. However, for new people we recommend using Github Codespaces. To create one, click the green code button that you might have used to download the code earlier and then after that click codespaces and create a new one. This will set up a cloud environment where you will have all the tools needed to do this. Once created run: `pip install -r requirements.txt` to make sure all of the dependencies have been downloaded. 

### Creating Your Branch

When using version control, branch driven development is a staple. Branch driven development is when you split up the work onto seperate branches where the main branch holds all the code that is complete and working. Please read [this article](https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/) to find out more.

To create a branch using the Git CLI use the following command:
```
git checkout -b <BRANCH-NAME>
```
It is recommended you name your branch something like yourname/example. Next push the branch to the remote origin by doing this command:
```
git push --set-upstream origin <BRANCH-NAME>
```
After this verify that your branch is visible on GitHub. 

### Develop Your Code

It is finally time for the fun part where you develop your code. First check out the file `CONTRIBUTING.md` in the other examples directory to find out more about what you need to include with your example. For ideas on APIs to call here is a [GitHub Repo](https://github.com/public-apis/public-apis) of a bunch of cool and free to use APIs. Think about a cool little program you could develop with this and then go and create it. Once you've tested it, come back here and follow the rest of the tutorial and learn how to commit it and make a pull request.

### Making + Pushing a Commit

Now that you have written your code it is time to push it to the repository. First off you can see what files you have made changes to by using the `git status` command. These are the list of files you can add to your commit. You can either go and add each on individually by using `git add <FILENAME>` or you can use `git add *` to just add all of them. Once you have added all of the files that you would like to have added run the following command to make the commit. 
```
git commit -m "SOME COMMIT MESSAGE"
```
For the commit message you usually want to make it something meaningful. [This article](https://www.conventionalcommits.org/en/v1.0.0/) talks a little bit about how you can write them. A lot of us in the club follow those conventions. 

Next is pushing your commit to the origin. This can be done with the following command:
```
git push
```
Once this is completed check if your commit is visible on your branch on the repo.

### Making a Pull Request

Head over to your branch on the GitHub repository. On there you will see a line that says Your branch is some amount of commits ahead of the main branch. Click on the contribute button there and then click open pull request. Fill out the form that is there and then post it. You're now all set and one of the club admins will review your work and let you know if it is good to be merged into the main branch. If there is any feedback you will recieve and email or notification on GitHub so be sure to check in. Once your code is merged you have successfully contributed an example to our repo!

## Conclusion

We hope you learned something through this tutorial. If you would like to learn more there are some sources below that were used to help make this document. There are links on those pages that will lead you to more stuff. Happy coding!

## Sources

1) https://aws.amazon.com/what-is/api/
2) https://www.tutorialspoint.com/http/http_requests.htm
3) https://www.tutorialspoint.com/http/http_methods.htm
4) https://www.tutorialspoint.com/http/http_responses.htm