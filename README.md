# Student Task Manager – AWS Cloud Deployment

## Project Overview
Student Task Manager is a beginner-friendly web application developed using Python Flask and SQLite. It allows users to manage daily tasks through CRUD (Create, Read, Update, Delete) operations.

The application is deployed on an AWS EC2 Ubuntu instance using Gunicorn and Nginx.

## Features
- Add new tasks
- View all tasks
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- Store task information using SQLite
- Web application deployment on AWS EC2

## Technologies Used

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Database | SQLite |
| Web Server | Gunicorn |
| Reverse Proxy | Nginx |
| Cloud Platform | AWS |
| Compute Service | Amazon EC2 |
| Operating System | Ubuntu Linux |
| Version Control | Git and GitHub |

## AWS Architecture

1. The application is hosted on an AWS EC2 Ubuntu instance.
2. Flask handles application requests.
3. Gunicorn runs the Flask application.
4. Nginx acts as a reverse proxy and accepts HTTP requests.
5. SQLite stores the task records.
6. Systemd manages the application service.

## Project Structure

```text
Student_Task_Manager_AWS/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
    └── style.css
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shrutika18/Student_Task_Manager_AWS.git
cd Student_Task_Manager_AWS
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## AWS Deployment

The application was deployed on an AWS EC2 Ubuntu instance.

Deployment components:
- Amazon EC2 for hosting
- Ubuntu for the operating system
- Python virtual environment for dependencies
- Gunicorn for running Flask
- Nginx for reverse proxy
- Systemd for service management

## Challenges and Solutions

- **Application deployment:** Configured Gunicorn to run the Flask application.
- **Reverse proxy configuration:** Configured Nginx to forward HTTP requests to Gunicorn.
- **Service management:** Used systemd to keep the application running.
- **Database management:** Used SQLite to store and manage task records.
- **GitHub upload:** Used Git commands to version-control and upload the project.

## Future Enhancements

- User registration and login
- Role-based access control
- AWS RDS database integration
- Docker containerization
- CI/CD pipeline using GitHub Actions
- Application monitoring

## Author

Cloud and DevOps Learner

**GitHub Repository:**  
https://github.com/Shrutika18/Student_Task_Manager_AWS
