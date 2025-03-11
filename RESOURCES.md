# Tutorial on APIs

Welcome to our tutorial on APIs. In this tutorial, you will learn about what an API is, what REST APIs are, how HTTP requests work, and how you can utilize them in Python. There will also be an optional mini-project that will help you become familiar with Git and use an API of your choosing to create something. 

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

## Basics on HTTP Requests

## Calling APIs in Python

## How to Use Git + Mini Project

## Sources

1) https://aws.amazon.com/what-is/api/
2) https://www.tutorialspoint.com/http/http_requests.htm
3) 
4) 
5) 