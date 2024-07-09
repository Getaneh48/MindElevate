# MindElevate: Elevating Your Reading Habit
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Licensing](#licensing)

## Introduction

This web application  is built as a portfolio project for the ALX software engineering program that I am currently attending. Its core purpose is to empower users to cultivate a stronger reading habit. In our fast-paced, digital world, many of us, myself included, struggle to find consistent time and motivation for traditional book reading. Social media and other online distractions often take precedence, and textual content can fall by the wayside. We get swept up in the digital vortex, losing track of time and leaving reading aspirations unfulfilled. This sparked the inspiration for this project: to nudge users away from mindless scrolling and towards intentional reading.

The main focus of this application is to help,
1. Individuals of any age and background who want to cultivate their reading habit
2. Individuals who want to connect with a community of like-minded people.

### Who this app is for

1. For readers of all ages and backgrounds who wish to cultivate a habit of reading.
2. For those who struggle to maintain a consistent reading habit.
3. For book enthusiast looking to connect with a community of like-minded individuals.

### Links
- MindElevate: http://web-01.get4848.tech/
- Linkedin: https://www.linkedin.com/in/getaneh-alemayehu-7a1406b2/

## Features
### Goal setting

The main focus of this application is to make users track their progress for the book they are currently reading. It allows the user to set goals (daily goals and completion goals) for each book they are reading. After the user defines the goals they must periodically log the number of pages they are reading and the number of hours they have read each day. The app collects this information for each book daily. Using this information the app will display statistics for the current status of the selected book, the total number of pages read so far, and the number of pages remaining.

### Rewarding

One of the best features of the app is rewarding the user for the progress they have made so far in the form of badges. The app will reward the user a badge if;
They have completed their daily reading goal
If they have completed reading the book entirely with in their setted goal

### Progress tracking

The app let’s users monitor their reading journey with detailed progress indicators. See the percentage completed, daily and overall goal progress (both pages and time), and visualize their reading patterns across the month using a bar chart. This insightful data empowers the readers to identify strong reading days and potential lags, enabling them to fine-tune their reading habits and stay motivated.

### Tracking reading books

The app goes beyond tracking progress. Keep track of the readers "Currently Reading," "Completed," "Favorites," and "Bookmarked" lists. This comprehensive system allows the readers to manage their reading journey, share their favorite reads with friends, and revisit titles they’ve already enjoyed.

### Recommendation

The app suggests books based on the reader preferences, liked books and reading habits.

## Technologies
### Frontend:
- React.js Framework: To create a professional and engaging user interface (UI) that feels like a native desktop application, I opted for the mature React.js framework. Developed by Facebook, React.js is specifically designed for building single-page applications (SPAs) that rely heavily on JavaScript. My decision to use React was influenced by two key factors: first, its backing by a major tech company ensures its ongoing development and stability, making it a reliable choice for this project. Second, my existing knowledge of React allowed me to hit the ground running without the time investment required to learn a new framework.
- SCSS (Syntactically Awesome Stylesheet): This powerful preprocessor extends the functionality of traditional CSS, allowing developers to define variables, nest rules, create functions, and utilize mixins. These features significantly improve the efficiency and manageability of stylesheets within the project.
HTML5: As the latest standard for web application structure, I employed HTML5 to provide the foundational building blocks for the application.
- JavaScript: Beyond its role in React, JavaScript was also used for specific logic processing and facilitating asynchronous communication with the backend services.
### Backend:
- Flask-RESTful: This lightweight Python framework was chosen due to my existing proficiency in Python. Flask-RESTful simplicity and efficiency made it well-suited for the project's current scope, allowing me to avoid potential complications that might arise from introducing a new framework. Additionally, my familiarity with Flask minimized the learning curve and development time.
- SQLAlchemy ORM (Object-Relational Mapper): This powerful library streamlines database interaction by enabling the definition and manipulation of database entities using Python objects. SQLAlchemy eliminates the need to write raw SQL queries, allowing me to interact with the database using intuitive Python code instead.

## Installation
Clone the entire repository to your local directory
`git clone https://github.com/Getaneh48/MindElevate.git`
### Dependencies
#### Frontend
**React js**
```
  npm install vite --save-dev
  vite
```
Follow the onscreen instruction to install react
#### Backend API server
**python3**
 ```
 sudo apt update
 sudo apt install python3
 ```
**pip3**
 ```
  sudo apt install python3-pip
 ```
**Flask**
```
  pip3 install flask
```
**Flask-Cors**
```
  pip3 install flask-cors
```
**SQLAlchemy**
before installing SQLAlchemy, we need to install MySQLdb mobule version 2.0.x.
```
  sudo apt-get install libmysqlclient-dev
  sudo apt-get install zlib1g-dev
  sudo pip3 install mysqlclient
```
then, Install SQLAlchemy module version 1.4.x.
```
  sudo pip3 install SQLAlchemy
```
## Usage
#### Running the frontend of the MindElevate app
  From the root folder of the app, type the following commands
  ```
    cd frontend
    npm run dev
  ```
#### Running the MindElevate Backend Server
  From the root folder of the app, type the following commands
  ```
    MELV_MYSQL_USER=<user> MELV_MYSQL_PWD=<password> MELV_MYSQL_HOST=<host> MELV_MYSQL_DB=<db name> MELV_TYPE_STORAGE=db
    MELV_API_PORT=<port> python3 -m api.v1.app
  ```
## Licensing

    



