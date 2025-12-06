CI-CD-DevSecOps-Project1
[![CI-CD-DevSecOps-Project1](https://github.com/adenoch1/DevSecOps-project-1-Foundation/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/adenoch1/DevSecOps-project-1-Foundation/actions/workflows/ci-cd.yml)

#  Project 1 — DevSecOps CI/CD Foundation

This project kick-starts your **DevSecOps / SRE** journey and lays the foundation for secure pipelines, automated testing, and container-based development.

---

#  **Project Overview**

This repository includes:

### 🔹 Application
- A simple **Python Flask API**
  - `GET /` → Returns a hello response  
  - `GET /health` → Healthcheck endpoint  

### 🔹 Containerization
- `Dockerfile` using **python:3.11-slim**
- Security-hardened build steps

### 🔹 GitHub Actions CI/CD
Your cloud CI pipeline performs:

- Checkout + dependency installation  
- Unit testing using `pytest`  
- Static analysis via **Bandit**  
- Dependency vulnerability scanning via **pip-audit**  
- Docker build using Buildx  
- Trivy filesystem scan for vulnerabilities  

### 🔹 Jenkins Pipeline (Jenkinsfile)
A matching on-prem / local CI pipeline:

- Checkout  
- Python virtual environment  
- Dependency installation  
- Unit tests  
- Bandit + pip-audit security scans  
- Docker image build  

### 🔹 Developer Tooling
- Pre-commit hooks (formatting + linting)
- Sample `.env.example`

---

# **Run the Application Locally**

```bash
# Install virtual environment
python -m venv .venv

# To activate the virtual environment:
# For linux/macOS/WSL/Git Bash, use this:
source .venv/bin/activate 

# For Windows (Powershell), use this:
.venv\Scripts\Activate

# For CMD, use:
.venv/Scripts/activate.bat

# Install dependencies:
pip install -r app/requirements.txt

# Set environment variable:
# For Windows(Powershell/CMD), use this:
$env:FLASK_DEBUG = "1"
python app/app.py

# For Linux/MacOS/Git Bash, use this:
export FLASK_DEBUG=1
python app/app.py

Visit:

http://localhost:5000

http://localhost:5000/health

# Run Tests Locally
pytest -q

# Push Code to GitHub (Trigger CI Pipeline)

# 1. Initialize the directory
git init

# 2. Stage all changes
git add .

# 3. Commit with a clear message
git commit -m "Initial commit DevSecOps"

# 4. connect local to remote
git remote add origin https://github.com/adenoch1/DevSecOps-project-1-Foundation.git

# 5. Push to main branch (or master if that is your default)
git push origin main

# In case of any conflict, pull, merg and re-push
git pull origin main

# correct the conflict and push
git push origin main.
# 4. Open GitHub → Actions tab
# CI workflow will start automatically

# 5. Watch the pipeline
# - Tests
# - Security scans
# - Docker build
# - Trivy scan
# If successful, the badge turns green


# Build and Run the Docker Image

docker build -t devsecops-project1 -f docker/Dockerfile .
docker run -p 5000:5000 devsecops-project1

# Jenkins Setup (Local Using Docker)

To run the Jenkins CI pipeline locally:

Start Docker Desktop
Docker must be running before starting Jenkins.

Run Jenkins with Docker Socket Mount

docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

# Retrieve Jenkins Password

docker exec -it jenkins bash
cat /var/jenkins_home/secrets/initialAdminPassword
exit    # to exit the container

Open Jenkins UI:
http://localhost:8080

# Install These Plugins

Blue Ocean
Docker Pipeline
Docker
GitHub
Credentials
Pipeline Utility Steps
AnsiColor
Workspace Cleanup

# Install Tools Inside Jenkins Container

docker exec -u root -it jenkins bash
apt-get update
apt-get install -y python3 python3-pip python3-venv docker.io

# add jenkins to docker group
usermod -aG docker jenkins

# Fix Docker Permissions on Host
chown root:docker /var/run/docker.sock

# exit the container
exit

# restart jenkins container
docker restart jenkins

# Test Docker Access from Jenkins

docker exec -u jenkins -it jenkins docker ps
If containers list, Jenkins is ready.

Set Up Jenkins Pipeline

In Jenkins UI:
Click New Item
Enter: DevSecOps-Project1-Pipeline
Select Pipeline

Click OK

Configure Source (SCM)

Under Pipeline, select:
Pipeline script from SCM
Choose Git

Enter your repository URL, for example:
https://github.com/<your-username>/<your-repo>.git

Set the correct branch name (e.g. main)
Click Save

Run the Build
Click Build Now in your Jenkins project.

This will:
Pull your code from GitHub
Run your Jenkinsfile
Build a Docker image inside your local Docker daemon

Verify Docker Image
On your machine, run: docker ps

You should see your image/container if it’s running.
To list all images: docker images

Inspect the Image for Exposed Ports
To view metadata (including exposed ports):
docker image inspect devsecops-project1

look for:
"ExposedPorts": {
    "5000/tcp": {}
}

Run Your Application Container
Your application listens on port 5000 inside the container, so map it to 8081 on the host:

docker run -d -p 8081:5000 devsecops-project1:latest

Access the Application
Open in your browser: http://127.0.0.1:8081 or http://localhost:8081

Summary
Jenkins builds the Docker image during the pipeline
The new image is stored in your local Docker daemon
You run it using docker run -p
The port mapping is: HOST_PORT:CONTAINER_PORT
View the application in your web browser

Local Docker build tests the Dockerfile.
Local Jenkins build tests the Jenkinsfile.
Once both pass, we can confidently push images to a registry and deploy.

Next Steps (Project 1B → 1C)
You can extend this project with:

# DevSecOps Enhancements

Trivy image scanning
Gitleaks secret scanning
SBOM generation (CycloneDX)
Container signing (Cosign)

# Deployment Automation

GitHub Container Registry (GHCR)
AWS ECR + ECS Fargate
AWS EC2 + Systemd service
App Runner or Lambda container images

# Infrastructure-as-Code

Terraform for AWS infra
AWS CDK (Python)
- Extend with:
  - Terraform or CDK to deploy infrastructure
  - CloudWatch logging and metrics
  - More endpoints and tests

Purpose of This Project
This is the foundation of your long-term DevSecOps portfolio.
It demonstrates:
CI/CD fundamentals
Security automation
Containerization
Running parallel pipelines (GitHub Actions + Jenkins)
Professional code structure

Author
Enoch Adekanye
DevSecOps | SRE | Cloud Engineer
