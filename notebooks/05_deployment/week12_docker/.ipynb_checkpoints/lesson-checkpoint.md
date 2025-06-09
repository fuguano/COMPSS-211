# Docker Fundamentals for Computational Social Science

## What is Docker?

**Docker** is a containerization platform that allows you to package applications and their dependencies into lightweight, portable containers. Think of it as a way to create consistent, reproducible environments that can run anywhere.

At its core, Docker solves one of the most persistent problems in software development and research: **"It works on my machine!"** 

## The Shipping Container Analogy

🚢 **Whiteboard Analogy: Docker as Shipping Containers**

Imagine you're shipping goods around the world. Before standardized shipping containers, different ports used different methods:
- Some used wooden crates
- Others used burlap sacks  
- Different sizes, different handling methods
- Chaos when moving between ships, trucks, and trains

**The Solution: Standardized Shipping Containers**
- Same size and shape everywhere
- Can be moved by ship, truck, or train without unpacking
- Contents are isolated and protected
- You know exactly what handling equipment you need

**Docker Containers Work the Same Way:**
- **Your code + dependencies** = the "cargo" inside the container
- **Docker container** = the standardized "shipping container"
- **Different computers** = different "ports" (Windows, Mac, Linux, cloud)
- **Docker Engine** = the standardized "handling equipment"

Just like a shipping container can move from ship to truck to train without changing its contents, a Docker container can move from your laptop to a colleague's computer to the cloud without any changes!

## Solving "It Works on My Machine"

### The Problem
```
👩‍💻 Researcher A: "My sentiment analysis works perfectly!"
👨‍💻 Researcher B: "I can't get it to run. What Python version? Which packages?"
👩‍💻 Researcher A: "Um... Python 3.9? I think I installed some stuff with conda..."
👨‍💻 Researcher B: "I have Python 3.11 and different package versions. Now I'm getting errors..."
```

### The Docker Solution
```
👩‍💻 Researcher A: "Here's my Docker container with everything pre-configured."
👨‍💻 Researcher B: "Perfect! I just run 'docker run your-analysis' and it works exactly like on your machine!"
```

**What Docker Packages Together:**
- ✅ Exact Python version (3.10.8, not just "3.10")
- ✅ Specific package versions (pandas==2.1.0, not "latest")
- ✅ System libraries and dependencies
- ✅ Environment variables and configurations
- ✅ Your code and scripts

## Core Docker Concepts

### 1. Images vs Containers
Think of **images** as blueprints and **containers** as the actual running instance:

- **Docker Image** = Recipe/Blueprint
  - A read-only template with instructions
  - Contains your code, dependencies, and system tools
  - Can be shared and stored in repositories
  - Like a `.exe` installer file

- **Docker Container** = Running Application  
  - A running instance created from an image
  - Has its own isolated environment
  - Can be started, stopped, and deleted
  - Like a running program on your computer

```
Image (Recipe)     →     Container (Running Instance)
📄 Dockerfile     →     🏃‍♂️ Running application
```

### 2. Dockerfile
A **Dockerfile** is a text file with step-by-step instructions to build an image:

```dockerfile
# Start with a base image (like choosing your foundation)
FROM python:3.10-slim

# Set up the working directory (like creating a project folder)
WORKDIR /app

# Copy and install requirements (like setting up your environment)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your code (like adding your scripts)
COPY . .

# Define what happens when the container starts
CMD ["python", "analysis.py"]
```

### 3. Docker Registry (Docker Hub)
- **Docker Hub** = "App Store" for Docker images
- Contains pre-built images (Python, Jupyter, databases, etc.)
- You can upload your own images to share
- Like GitHub but for Docker images instead of code

### 4. Key Docker Commands
```bash
# Build an image from a Dockerfile
docker build -t my-analysis .

# Run a container from an image
docker run my-analysis

# List running containers
docker ps

# List all images
docker images

# Stop a container
docker stop container-name
```

## Why Docker Matters for Research

### 🔬 **Reproducibility**
- Your analysis runs identically on any machine
- No more "dependency hell" or version conflicts
- Research can be replicated years later
- Meets open science standards

### 🤝 **Collaboration**
- Share exact environments with colleagues
- New team members get productive immediately
- No lengthy setup instructions
- Works across different operating systems

### ☁️ **Deployment & Scaling**
- Easy deployment to cloud platforms (AWS, Google Cloud)
- Scale analysis across multiple machines
- Consistent behavior from laptop to supercomputer

### 📦 **Isolation**
- Projects don't interfere with each other
- Safe to experiment without breaking your system
- Multiple Python versions side-by-side

## Docker in Computational Social Science

### Real-World Examples

**📊 Reproducible Data Analysis**
```dockerfile
FROM jupyter/scipy-notebook
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY notebooks/ ./work/
# Anyone can now run your exact analysis environment
```

**🕷️ Web Scraping Projects**
```dockerfile
FROM python:3.10
RUN apt-get update && apt-get install -y chromium-driver
COPY scraper.py .
# Scraper runs consistently regardless of local browser setup
```

**🤖 ML Model Deployment**
```dockerfile
FROM python:3.10-slim
COPY model.pkl ./
COPY predict.py ./
# Model serves predictions in standardized environment
```

## Learning Objectives

By the end of this lesson, you will:

- **Understand** containerization concepts and Docker's role in reproducible research
- **Create** basic Dockerfiles for Python applications
- **Build and run** Docker containers for your own projects
- **Identify** when Docker adds value to research workflows
- **Apply** Docker best practices for computational social science
- **Evaluate** Docker for your final project implementation

## Workshop Structure

### 1. **Live Build Demo** (20 minutes)
Demonstration creating a simple containerized Python application:
- Writing a basic Python script
- Creating a Dockerfile step-by-step
- Building the image (`docker build -t hello-app .`)
- Running the container (`docker run hello-app`)
- Observing the output and behavior

### 2. **Hands-On Practice** (25 minutes)
Modify and rebuild containers:
- Add new dependencies (numpy, pandas)
- Update requirements.txt
- Rebuild and test the enhanced container
- Experience the build-test-iterate cycle

### 3. **Show and Tell** (10 minutes)
Share experiences and use cases:
- Students with Docker experience share stories
- Discuss real-world applications
- Industry and academic examples

### 4. **Discussion** (15 minutes)
Benefits, challenges, and best practices:
- When Docker helps vs. when it's overkill
- Common pitfalls and how to avoid them
- Resource considerations and optimization

### 5. **Final Project Integration** (10 minutes)
How Docker can enhance project reproducibility:
- Bonus point opportunities
- Implementation strategies
- Alternative approaches (GitHub Codespaces)

## Installation Note

Docker installation requires administrative privileges on some systems. If you cannot install Docker, you can still benefit by:

- **Following along** with instructor demonstrations
- **Pairing up** with someone who has Docker installed  
- **Understanding concepts** for future implementation
- **Exploring alternatives** like GitHub Codespaces or virtual environments

The goal is to understand when and how Docker can benefit your research, not necessarily to become a Docker expert in one session.

---

*Remember: Docker is a tool to solve specific problems. Use it when it adds value, not just because it's trendy. Focus on your research goals first, then consider if Docker helps achieve them.*