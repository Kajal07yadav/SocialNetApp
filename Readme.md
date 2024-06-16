# Social Networking Application API

This project is a social media API built with Django and Django REST Framework. It includes functionalities such as user authentication, sending and accepting friend requests

## Getting Started

### Clone the Repository

1) First, clone the repository to your local machine:

`git clone https://github.com/Kajal07yadav/SocialNetApp.git
`

2) cd `SocialNetApp`


## Docker Setup

### Running the project

1) To Build and Start the Docker Container :
    `docker-compose up -d`

2) Apply Migrations :
   ` docker-compose exec web python manage.py migrate`

3) Create a Superuser :to access admin panel
    `docker-compose exec web python manage.py createsuperuser`


## Postman Collection

**Importing the Collection**

`https://www.postman.com/kajal-yadav/workspace/socialauthapi/collection/29592036-6cdf620b-d1e2-4d6b-ad06-50c4a1ace59a?action=share&creator=29592036`
            or
            
**Download Postman Collection**
   `https://drive.google.com/drive/home`

Steps for Import into Postman:

- Open Postman.
- Click on the "Import" button.
- Select the Choose Files button and upload the downloaded .json file.
- The collection will be imported into Postman, and you can start using it to test the API endpoints.

### User Authentication

1) *Registeration :*
POST `http://127.0.01:8000/api/user/register/`

2) *login*
POST `/api/user/login/`

3) *User Profile*
GET `api/user/profile/?search=B`

4) *Change Password*
POST `/api/user/changepassword/`

5) *Forgot Password*
POST `/api/user/send-reset-password-email/`

6) *Reset User Password*
POST `/api/user/reset-password/<uid>/<token>/`

7) *Logout*
POST `/api/user/logout/`



### Social Media API

1) **Send-Friend-Request**
POST `http://127.0.01:8000/social/friend-request/send/`

2) **Respond-Friend-Request**
PATCH `http://127.0.01:8000/social/fr/respond/<int:id>/`

3) **List-Pending-Friend-Requests**
GET `http://127.0.01:8000/social/fr/pendingUser/`

4) **List-of-Users-Accepted-Your-fr**
GET `http://127.0.01:8000/social/fr/requestAccepted/`

5) **List-of-users-Rejected-Your-fr**
GET `http://127.0.01:8000/social/fr/requestRejected/`

6) **List-of-Fr-you-accepted**
GET `http://127.0.01:8000/social/fr/You-accepted/`

7) **List-of-Fr-you-rejected**
GET `http://127.0.01:8000/social/fr/You-rejected/`


## Need Help?

If you encounter any issues or have questions about this project, please feel free to contact me. I'm here to help!

You can reach out to me via:

Email: kajalyadav070496@gmail.com

LinkedIn: https://www.linkedin.com/in/kajal-yadav31/

To view my other project on GitHub : https://github.com/Kajal-Yadav31

and here is my resume : https://drive.google.com/file/d/18tRBIhMVoTwAEVlD-j16d6zuoBJc704q/view







