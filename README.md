# Poker hand recording and analysis application 
## Creater: Hillman

1. [`Project Overview`](#project-overview)

2. [`Programming Languages for this application`](#programming-languages-for-this-application)

3. [`Developing an Application for Multiple Users`](#developing-an-application-for-multiple-users)

4. [`Main Features`](#main-features)

5. [`Additional Features`](#additional-features)

6. [`User Features`](user-features)

7. [`Admin Features`](#admin-features)

8. [`Non-Functional Requirements`](#non-functional-requirements)

9. [`Initial Set Up`](#initial-set-up)

10. [`Tracking`](#tracker) 

11. [`References`](#references) 
## Project Overview

Objective: Create a web-based application for recording, sharing, and analyzing poker hands, with features for user management, hand categorization, and analysis tools.

Target Audience: Poker players and enthusiasts who want to analyze hands, share their gameplay, and study different game scenarios.

Platforms: Web application accessible via browsers like Google Chrome, Safari, Firefox, etc.

## Programming Languages for this application

### Frontend:
- React.js: React.js is a powerful and popular JavaScript library for building user interfaces, especially single-page applications. It is well-suited for creating a dynamic, responsive user experience where users can easily navigate and interact with the application.

### Backend:
- Python (Flask or Django): Flask is a lightweight framework that is great for smaller projects and is very flexible. Django, on the other hand, is a more robust and comprehensive framework, which includes built-in tools for user 
authentication, database management, and more. Django could be more suitable if you expect your project to scale.

- Node.js with Express: If you’re already using JavaScript on the frontend (e.g., React.js), Node.js with Express could be a natural choice for the backend, allowing for seamless integration and use of JavaScript across your stack.

### Database:
- PostgreSQL: A robust relational database system that is well-suited for applications requiring complex queries and transactions. It’s particularly good for structured data like poker hands.


### Additional Tools:
- WebSocket or Socket.io: For real-time communication (e.g., live hand analysis, chat features), you may want to integrate WebSocket or Socket.io.
- Docker: Containerizing your application using Docker can help ensure consistency across different environments (development, testing, production).

## Developing an Application for Multiple Users

### Phase 1: Planning and Design

- User Stories and Wireframes: Start by creating user stories to define what your users will be able to do (e.g., register, login, upload hands, search for hands, etc.). Create wireframes to visualize the layout and flow of the application.

- Database Schema Design: Design your database schema to handle users, poker hands, comments, and other relevant data. Think about the relationships between entities (e.g., a user can upload many hands, each hand can have many comments).

### Phase 2: Authentication and User Management

- User Authentication: Implement a secure user authentication system. If using Django, you can leverage its built-in authentication. With Flask or Express, you might need to implement this from scratch or use libraries like Flask-Security, Flask-Login, or Passport.js.

- Hashing Passwords: Ensure that user passwords are securely hashed before storing them in your database. Use bcrypt or similar libraries.

- Token-based Authentication: Consider using JWT (JSON Web Tokens) for session management and API security, especially if you plan to offer a mobile version or an API for third-party integrations.

- Role Management: Depending on your needs, you might implement roles (e.g., admin, regular user) to manage permissions within the app.

### Phase 3: Hand History Upload and Search

- Data Entry Forms: Create forms for users to upload hand histories. Allow them to input the hand details manually or parse hand histories from supported formats (e.g., GGpoker, PokerStars).

- Search Functionality: Implement a robust search system that allows users to filter and search hand histories by various criteria (position, stacks, date, etc.). This might involve using full-text search capabilities in your database or integrating a search engine like Elasticsearch.

### Phase 4: UI/UX Development

- User Interface: Develop the UI with React.js (or your chosen frontend framework), focusing on an intuitive and responsive design. Ensure users can easily navigate the app, upload hands, and view analysis.

- Data Visualization: Consider integrating libraries like D3.js or Chart.js for visualizing poker hand data, such as chip stacks, pot sizes, or equity graphs.

### Phase 5: Security Considerations

- HTTPS and SSL: Ensure that your application runs over HTTPS to protect data in transit.

- Input Validation and Sanitization: Protect against common security threats like SQL injection and cross-site scripting (XSS) by validating and sanitizing user inputs.

- Rate Limiting: Implement rate limiting to protect your app from abuse, such as brute force attacks on the login system.

### Phase 6: Testing and Deployment

- Testing: Implement both unit tests and integration tests to ensure the functionality and security of your application. Use tools like pytest (for Python), Jest (for JavaScript), or others relevant to your chosen tech stack.

- Continuous Integration/Continuous Deployment (CI/CD): Set up CI/CD pipelines to automate testing and deployment. Tools like GitHub Actions, Travis CI, or Jenkins can be useful here.

- Deployment: Deploy your application on a cloud platform (e.g., AWS, Heroku, DigitalOcean) and consider using Docker to package your application for easy deployment.

### Phase 7: Scaling and Maintenance

- Scalability: As your user base grows, monitor and scale your infrastructure accordingly. This might involve database optimizations, caching strategies (e.g., Redis), or load balancing.

- User Feedback and Iteration: Continuously gather user feedback and iterate on the application to add new features, fix bugs, and improve the user experience.


## Main Features

### 1. Hand Recording and Management
- Hand Entry: Users can manually enter hand details or upload hand histories from supported formats (e.g., GGpoker, PokerStars).

- Hand Details: Capture details such as player positions, stack sizes, actions per street (flop, turn, river), pot size, and showdown results.

- Hand Deletion: Users can delete hands they’ve recorded, with a confirmation prompt to avoid accidental deletions.

### 2. Session Notes
- Notes Section: Each session (group of hands) should have a notes section where users can input observations, thoughts, or strategies.

### 3. Navigation and Filtering
-  Navigation Bar: Users can navigate through different hands using filters like game type, player positions, and actions taken at each stage (flop, turn, river).

- Search and Filter: Users can search and filter hands by criteria such as date, position, opponent type, stack sizes, and more.

### 4. Cross-Platform Access
- Responsive Design: The application should be accessible on any device with a web browser, ensuring a seamless experience across desktop, tablet, and mobile devices.

## Additional Features

### 1. Hand Grid Overview
- Grid Display: A grid or table view displaying all hands in a session or a search result, with key details (e.g., date, game type, position, result) for quick overview and selection.

### 2. Hand Visualization
- Hand Replay: Implement a visual replay feature where users can step through the hand street by street.

## User Features

### 1. User Authentication
- Registration/Login: Secure registration and login system, utilizing email verification and strong password policies.

- User Profiles: Basic user profiles where users can see their recorded hands, sessions, and notes.

- Session Management: Users can log in and out securely, with session timeouts for additional security.

### 2. User Settings
- Profile Management: Allow users to update their profiles, change passwords, and manage notification settings.

- Privacy Settings: Users can choose to make their hands and notes public or private.

## Admin Features

### 1. User Management
- User List and Activity Monitoring: Admins can view a list of users, their activity, and login/logout history.

- User Actions: Admins can manage users, including banning, deleting, or resetting passwords.

### 2. Maintenance
- Data Backup: Regular backups of the database to prevent data loss.

- Performance Monitoring: Tools to monitor server performance, database load, and application health.

## Non-Functional Requirements

### 1. Security
- Data Protection: Ensure all user data (especially hand histories and personal details) are securely stored, using encryption for sensitive data.

- Secure Communication: Use HTTPS to encrypt all data transmitted between users and the server.

- Input Validation: Implement thorough input validation to prevent SQL injection, XSS, and other common vulnerabilities.

### 2. Performance
- Scalability: Design the system to scale with increasing user numbers, ensuring consistent performance.

- Responsive Design: Ensure the application is responsive and performs well on various devices.

### 3. Reliability
- Uptime: Aim for high uptime with minimal downtime, using redundant systems where necessary.

- Error Handling: Implement comprehensive error handling to provide meaningful feedback to users and avoid crashes.

### 4. Usability
- Intuitive Interface: The user interface should be simple and easy to navigate, with a focus on UX best practices.

- Documentation: Provide clear documentation and possibly tutorials for users to understand how to use the application effectively.

## Initial Set Up 

### 1. Install Python and create a virtual environment 

``` 
python3 -m venv env
source env/bin/activate 
```

### 2. Install Django 
``` 
pip install django 
```

### 3.Install PostgreSQL in official PostgreSQL website: https://www.postgresql.org/download/windows/.

Run the downloaded installer and follow the prompts.
Choose the components you want to install (typically, you'll need PostgreSQL Server, pgAdmin, and Command Line Tools).
Set a password for the default postgres user (make sure to remember this).

### 4. Open Terminal and install PostgreSQL using:
``` 
brew install postgresql 
```

### 5. To create a databse for the project on macOS terminal: 
``` 
psql -U postgres 
``` 

### 6. Install Node.js and React: 
``` 
npx create-react-app poker-app-frontend 
```

### 7. Create the Django Project 

``` 
django-admin startproject poker_project
cd poker_project
python manage.py startapp poker_app 
```

### 8. configure Django setting ( in settings.py ) to use PostgreSQL: 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'poker_app',
        'USER': 'poker_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### 9. Set Up User Authentication in Django 'User' model 
Run initial migrations to set up the database: 
``` 
python manage.py migrate
```

### 10. Create a superuser to access the admin panel
``` 
python manage.py createsuperuser 
```

### 11. Run migrations to apply the models:
``` 
python manage.py makemigrations poker_app
python manage.py migrate 
```

### 12. Navigate to your React project directory:
``` 
cd ../poker-app-frontend 
```

### 13. Start the React development server: 
``` 
cd ../poker-app-frontend 
```

### 14. Connect React Frontend to Django Backend:

Use Django REST Framework (DRF) to create APIs that the React frontend can interact with.

Install DRF:            
``` 
pip install djangorestframework 
```

Add it to your Django INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
## Tracker

###  <p align="center"> 30 August 2024 </p>
Use
```
python manage.py runserver

```

Then visit http://localhost:8000/api/pokerhands/ in your browser. If you’ve created some PokerHand instances, you should see them listed here in JSON format. If not, you can use POST requests to create new entries.


###  <p align="center"> 31 August 2024 </p>

User Registration: Send a POST request to http://localhost:8000/api/register/ with username, email, and password to register a new user.

Login and Obtain JWT: Send a POST request to http://localhost:8000/api/token/ with username and password to obtain a JWT token.

View and Update Profile: Use the token to access http://localhost:8000/api/profile/ to view and update the user’s profile.

simply open another terminal and use the following command: 
```
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MTQwNDg1LCJpYXQiOjE3MjUxNDAxODUsImp0aSI6IjlhNjI0NDI2ZjllMjQ4MTZiZWVlZGNjYTJmZjc4Yjk5IiwidXNlcl9pZCI6Mn0.tSh4rDZkDGL9OONQ-DKARIxFE9s-joeZQQfbiXtYmDc" http://localhost:8000/api/profile/
```

CRUD Operations on Poker Hands: Ensure the poker hands can be created, viewed, updated, and deleted, and that these operations respect the user’s ownership.

###  <p align="center"> 1 September 2024 </p>

Progress: Made a template for login, register user, main page and posting hand history. 

Posting: It is very simple by posting Positions, Stack sizes, hand history comment. A lot to improve. 

Main page: Only user can delete and edit the post, where others can view it like Threads. 

TO DO: 
1. improve the hand history posting, improve the view 
2. Search button where people can search by different key words. 
3. A lot to edit in the post hand 
4. Styling




## References