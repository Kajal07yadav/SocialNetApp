# Social Networking Application API

This project is a social media API built with Django and Django REST Framework. It includes functionalities such as user authentication, sending and accepting friend requests

## Getting Started

### Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/Kajal07yadav/SocialNetApp.git

cd SocialNetApp


## Docker Setup

### Running the project

- 1) To Build and Start the Docker Container :
    docker-compose up

- 2) Apply Migrations :
    docker-compose exec web python manage.py migrate

- 3) Create a Superuser :
    docker-compose exec web python manage.py createsuperuser


## Postman Collection
To help you quickly test and understand the API endpoints, we have included a Postman collection. You can import this collection into Postman to see all the available endpoints and make test requests easily.

Importing the Collection
Download the Postman Collection:
https://www.postman.com/kajal-yadav/workspace/socialauthapi/collection/29592036-c142557c-1e77-4823-b773-49d4a57cab2f?action=share&creator=29592036

Download Postman Collection
Import into Postman:

Open Postman.
Click on the "Import" button.
Select the Choose Files button and upload the downloaded .json file.
The collection will be imported into Postman, and you can start using it to test the API endpoints.
Available Endpoints
The Postman collection includes the following endpoints:

User Authentication
POST /api/token/: Obtain JWT token.
POST /api/token/refresh/: Refresh JWT token.
Friend Requests
POST /api/friend-requests/: Send a friend request.
GET /api/friend-requests/: List received friend requests.
POST /api/friend-requests/<id>/accept/: Accept a friend request.



