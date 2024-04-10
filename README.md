
# Django WhatsApp Clone
![Static Badge](https://img.shields.io/badge/Python-green?logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-darkgreen)

💻 A small functional person-to-person message center application built using **Django**. It has a REST API and uses WebSockets to notify clients of new messages and avoid polling.

## Features

- **Signup/Login**
- One-on-One personal chat with other users

## Architecture

1. When a user logs in, the frontend downloads the user list and opens a WebSocket connection to the server (notifications channel).
2. When a user selects another user to chat, the frontend downloads the latest 15 messages (configurable in settings) they've exchanged.
3. When a user sends a message, the frontend sends a POST to the REST API. Django saves the message and notifies the users involved using the WebSocket connection (sends the new message ID).
4. When the frontend receives a new message notification (with the message ID), it performs a GET query to the API to download the received message.

## Scaling

The project uses **Django Channels** for handling WebSocket requests. Channels take Django into a multi-process model, allowing you to run one or more interface servers and worker servers connected by a channel layer. Consider switching to the Redis backend for better performance and scalability in a distributed environment.

For more information on Channels, refer to the [official documentation](https://channels.readthedocs.io/en/latest/introduction.html).

## Assumptions

Due to time constraints, this project lacks:

- User Selector
- Pagination
- Good Test Coverage
- Better Comments / Documentation Strings
- Modern Frontend Framework (like React)
- Proper UX / UI design (currently uses plain Bootstrap)

## Running the Project Locally

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/suhailvs/django-whatsapp
   cd django-whatsapp
   ```

2. Ideally, create a virtual environment and install the project's dependencies:
   ```
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Initialize the database and run the server:
   ```
   ./manage.py migrate
   ./manage.py runserver
   ```

4. Optional: Install and start Redis Server (for better performance):
   ```
   sudo add-apt-repository ppa:redislabs/redis
   sudo apt-get update
   sudo apt-get install redis redis-server
   ```

5. Access the app at [http://localhost:8000/](http://localhost:8000/)
