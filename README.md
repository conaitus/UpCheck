![Version](https://img.shields.io/badge/Version-1.0.0-blue) ![Downloads](https://shields.io/github/downloads/ConanProZs/UpCheck/total) ![Forks](https://img.shields.io/github/forks/ConanProZs/UpCheck?style=social) ![watchers](https://img.shields.io/github/watchers/ConanProZs/UpCheck?style=social)

&nbsp;
![The logo](https://raw.githubusercontent.com/ConanProZs/UpCheck/main/icon.png)

# Welcome
If you don't know what UpCheck is then I am going to explain it in [What is it, And what are the requirements?](#what-is-it-and-what-are-the-requirements).


## How to Download
#### Download on server computer
First, you need a web server on your server computer, If you don't have one you can use the server.py file by
cloning this repo using `git clone https://github.com/ConanProZs/UpCheck.git`,
And you need python installed on your server computer for the server.py, And it needs Linux or windows to run. 
*(You can try run it on Mac but it's not tested on it.)*

#### Download on moderater computer
* First, clone this repo using `git clone https://github.com/ConanProZs/UpCheck.git`
* Second, you need python installed on your server computer and it needs Linux or windows to run. *(You can run it on Mac but it's not tested on it.)*
* Third, you need to install all the needed modules. The modules are:
curses, notifypy, stopwatch


## Running the program
First, run the web server *(server.py)* on the server computer
Second, run Ngrok http on port 25559 (If you dont know how, Go to https://ngrok.com/)
Third, run UrlChecker and enter the ngrok Url


## What is it, And what are the requirements?
It's a program for people that have a server computer with Linux or Windows 10.
*You can run it on Mac but it's not tested on it.*

It allows you to moderate your server computer with another computer
And sends notifications.

##### Here are the requirements for the server computer:
- Latest version of python *(recommended)*
- A web server *(You can use our server.py file if you don't have a web server)*
- [Ngrok *(It is free!)*](https://ngrok.com/)

##### Here are the requirements for the moderater computer:
- Latest version of python *(recommended)*
- UrlChecker.py file on it
