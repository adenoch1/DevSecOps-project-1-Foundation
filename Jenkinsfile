pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install -r app/requirements.txt
                    pip install pytest bandit pip-audit
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pytest -q
                '''
            }
        }

        stage('Security Scans') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    bandit -r app -ll
                    pip-audit -r app/requirements.txt
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devsecops-project1 -f docker/Dockerfile .'
            }
        }
    }

    post {
        always {
            echo "Pipeline Completed"
        }
        success {
            echo "✔ SUCCESS: All stages passed"
        }
        failure {
            echo "❌ FAILURE: Review logs above"
        }
    }
}
