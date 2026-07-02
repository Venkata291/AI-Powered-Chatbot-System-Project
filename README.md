## AI-Powered Chatbot System

## Overview

The AI-Powered Chatbot System is a web-based chatbot application developed using Python and Flask. It is designed to provide instant responses to user queries using predefined intents and keyword matching. The chatbot analyzes the user's message, identifies matching keywords, and returns an appropriate response. The application is lightweight, easy to deploy, and suitable for learning chatbot development and cloud deployment concepts.

# Objectives

- Develop an AI-powered chatbot using Python.
- Provide instant responses to user questions.
- Implement rule-based intent matching.
- Create a simple and interactive web interface.
- Deploy the chatbot on AWS EC2 using Gunicorn.

# Features

- Rule-Based AI Chatbot
- Instant Response Generation
- Keyword Matching
- Chat History Management
- Clear Chat Option
- Simple and Responsive User Interface
- AWS EC2 Deployment
- Gunicorn Web Server Support

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Flask | Web Framework |
| HTML | Web Page Structure |
| CSS | User Interface Styling |
| Gunicorn | Production Web Server |
| AWS EC2 | Cloud Hosting |
| Ubuntu Linux | Operating System |


## System Architecture


                User
                  │
                  ▼
          Web Browser
                  │
                  ▼
           Flask Application
                  │
                  ▼
         Chatbot Processing
                  │
                  ▼
         Intent Matching Logic
                  │
                  ▼
        Generate Appropriate Reply
                  │
                  ▼
          Display Response



## Project Structure

Sai_AI_Chatbot_System/
│
├── app.py
├── chatbot.py
├── intents.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/


## File Description

# app.py

Acts as the main Flask application. It handles HTTP requests, stores chat history using sessions, and connects the user interface with the chatbot logic.

# chatbot.py

Processes user messages and compares them with predefined keywords. If a keyword matches, it returns the corresponding response.

# intents.py

Contains all chatbot intents, keywords, and predefined responses.

# templates/index.html

Creates the chatbot web interface where users can interact with the chatbot.

# static/style.css

Provides styling for the chatbot interface to improve appearance and readability.


## Working Principle

1. The user enters a message in the chatbot interface.
2. Flask receives the request.
3. The chatbot converts the message into lowercase.
4. It compares the message with predefined keywords.
5. If a matching keyword is found, the corresponding response is returned.
6. If no keyword matches, a default response is displayed.
7. The conversation is stored in the session until the chat is cleared.


## Install Python

sudo apt install python3 python3-pip python3-venv -y

## Install Required Packages

pip install flask gunicorn

pip freeze > requirements.txt


## Running the Application

Start the Flask application.

python3 app.py

Open the browser:

http://EC2_PUBLIC_IP:5000


## Running with Gunicorn

Activate the virtual environment.

source venv/bin/activate

Start Gunicorn.

gunicorn --bind 0.0.0.0:5000 app:app


## Deploying as a Systemd Service

Create a service file.

sudo vi /etc/systemd/system/chatbot.service

Add the following configuration.

[Unit]
Description=AI Chatbot System
After=network.target

[Service]
User=root
WorkingDirectory=/home/ubuntu/Sai_AI_Chatbot_System
ExecStart=/home/ubuntu/Sai_AI_Chatbot_System/venv/bin/gunicorn --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target

Reload and start the service.

sudo systemctl daemon-reload

sudo systemctl enable chatbot

sudo systemctl start chatbot

sudo systemctl status chatbot


## Chatbot Workflow

User Question
      │
      ▼
Flask Receives Request
      │
      ▼
Chatbot Reads Message
      │
      ▼
Search Keyword
      │
      ├───────────────┐
      │               │
Keyword Found      Keyword Not Found
      │               │
      ▼               ▼
Return Response   Default Message
      │
      ▼
Display to User


## Advantages

- Simple and lightweight.
- Easy to understand and maintain.
- Fast response generation.
- Beginner-friendly project.
- Easy deployment on AWS EC2.
- Can be extended into an AI chatbot using Machine Learning.

## Future Enhancements

- Database Integration
- NLP-Based Chatbot
- Machine Learning Support
- Voice-Based Interaction
- User Authentication
- Multiple Language Support
- Chat History Database
- REST API Integration

## Conclusion

This project demonstrates the development of a simple AI-powered chatbot using Python and Flask. It uses rule-based intent matching to provide quick responses and can be successfully deployed on AWS EC2 using Gunicorn and Systemd. The project serves as a strong foundation for building advanced chatbot systems using Artificial Intelligence and Machine Learning.

## Author
Venkata Saibabu Kalluri
Cloud Computing Internship Project
AI-Powered Chatbot System

