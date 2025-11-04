# Flask-Postgres App with Docker and Jenkins

This project is a two-tier web application built with Flask and PostgreSQL. It's fully containerized using Docker and includes a Jenkinsfile for CI/CD automation. This README provides a comprehensive guide to understanding, setting up, and deploying the application.

## Project Overview

The application is a simple web-based message board where users can post and view messages. The backend is a Flask application that connects to a PostgreSQL database to store the messages. The entire application is designed to be run in Docker containers, making it portable and easy to deploy.

### Features

*   **Two-Tier Architecture:** A classic client-server architecture with a web tier (Flask) and a database tier (PostgreSQL).
*   **Containerized:** Fully containerized with Docker for easy setup and deployment.
*   **CI/CD Ready:** Includes a `Jenkinsfile` for automated building, testing, and deployment.
*   **Database Integration:** Uses PostgreSQL to store application data.
*   **Simple UI:** A clean and simple user interface for posting and viewing messages.

## DevOps Practices

This project demonstrates several key DevOps practices:

*   **Infrastructure as Code (IaC):** The `docker-compose.yml` and `Dockerfile` define the application's infrastructure as code, ensuring consistent environments.
*   **Continuous Integration (CI):** The `Jenkinsfile` automates the process of building and testing the application whenever new code is pushed to the repository.
*   **Continuous Deployment (CD):** The Jenkins pipeline can be extended to automatically deploy the application to a staging or production environment.
*   **Containerization:** Docker is used to package the application and its dependencies into a portable container, eliminating the "it works on my machine" problem.

## Technologies Used

*   **Backend:** Flask (Python)
*   **Database:** PostgreSQL
*   **Containerization:** Docker
*   **CI/CD:** Jenkins
*   **Frontend:** HTML, CSS

## Project Workflow

Here is a high-level overview of the project workflow:

```
1. Developer pushes code to Git repository.
   |
   v
2. Jenkins pipeline is triggered automatically.
   |
   v
3. Jenkins builds the Docker image for the Flask app.
   |
   v
4. Jenkins runs the application using docker-compose.
   |
   v
5. (Optional) Jenkins can be configured to run tests.
   |
   v
6. (Optional) Jenkins can deploy the application to a server.
```

## Prerequisites

Before you begin, ensure you have the following installed:

*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   [Jenkins](https://www.jenkins.io/download/) (Optional, for CI/CD)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-postgres-app.git
cd flask-postgres-app
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root and add the following variables:

```
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
```

### 3. Build and Run with Docker Compose

```bash
docker-compose up --build
```

This command will build the Docker images for the Flask app and the PostgreSQL database, and then start the containers. The application will be accessible at `http://localhost:5000`.

## Jenkins CI/CD Pipeline

This project includes a `Jenkinsfile` that defines a basic CI/CD pipeline. To use it, you will need to set up a new Jenkins pipeline and point it to your Git repository.

### Pipeline Stages

*   **Checkout:** Checks out the source code from the Git repository.
*   **Build:** Builds the Docker image for the Flask application.
*   **Run:** Runs the application using `docker-compose`.

### Setting Up the Jenkins Pipeline

1.  Install the "Docker" and "Docker Pipeline" plugins in Jenkins.
2.  Create a new "Pipeline" project in Jenkins.
3.  In the "Pipeline" section, select "Pipeline script from SCM".
4.  Select "Git" as the SCM and enter your repository URL.
5.  The "Script Path" should be `Jenkinsfile`.
6.  Save the pipeline and run it.

## Project Structure

```
.
├── app.py              # Flask application
├── docker-compose.yml  # Docker Compose file
├── Dockerfile          # Dockerfile for the Flask app
├── Jenkinsfile         # Jenkins pipeline definition
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # HTML template for the web UI
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.