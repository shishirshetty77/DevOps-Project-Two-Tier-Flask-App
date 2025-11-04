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
                // Replace with your GitHub repository URL
                git branch: 'main', url: 'https://github.com/shishirshetty77/DevOps-Project-Two-Tier-Flask-App.git'
            }
        }

        stage('Code Quality Check') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app.py'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests found. Skipping this stage.'


            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {

            sh 'docker-compose down'
        }
    }
}
