# api-workshop

A repository to help new devs learn about APIs and how to use Git on the way. 

## Contents

This repo contains three different things: a lesson on APIs, a demo, and other examples.

### Lesson on APIs

See the RESOURCES.md file for the lesson on APIs. It will cover the following:

1) What is an API?
2) Rest APIs
3) Basic Information About HTTP Requests
4) Calling APIs in Python
5) How to Use Git

### CRUS REST API Demo

The demo contains a program that simulates a REST API that does CRUD operations on a database. There is also a visualization that will show all of the transactions made on the database as well as it's current contents. 

To run the program, Python must be installed on your computer. With Python installed run this command to install all packages used:
```
pip install -r requirements.txt
```
Once all of the required packages are installed run the server with the following command:
```
python -m flask --app server run
```
This will open the server on `port 5000` of your localhost and is needed for the client to be able to make requests. To run the client program run the following python command:
```
python client.py
```
If you would like to view the visualization for the visualization open up the `visualization.html` file in your browser. This can be done by either going to your file explorer and opening the file (most OSes default to opening HTML files in your browser) or entering the following path in your search bar.
```
file://(LOCATION)/api-workshop/visualization.html
```
If you encounter any bugs with the demo please open an issue explaining what is broken.

## Contributing

If you would like to contribute to any of the resources in this workshop please reach out to us on our Discord server which can be found on our [website](https://umlcloudcomputing.org/)!