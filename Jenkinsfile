pipeline {
    agent any

    environment {
        DB_HOST = 'db'
        DB_NAME = 'postgres'
        DB_USER = 'postgres'
        DB_PASSWORD = 'your_postgres_password'
    }

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/shishirshetty77/DevOps-Project-Two-Tier-Flask-App.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running flake8 for linting...'
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 app.py --ignore=E501 || true
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker containers...'
                sh '''
                    docker compose build
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No test cases defined — skipping test stage.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application containers...'
                sh '''
                    docker compose down || true
                    docker compose up -d
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment...'
            sh '''
                docker compose down || true
                docker system prune -af || true
            '''
        }

        success {
            echo ' Pipeline executed successfully!'
        }

        failure {
            echo ' Pipeline failed. Please check the logs for details.'
        }
    }
}
