
# Yet to be decided API
# Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
Brief introduction to the project, its purpose, and any relevant background information.

## Installation
Instructions on how to install and set up the project locally. Include prerequisites and any dependencies needed.

```bash
# Clone the repository
git clone git@github.com:OsamaRiasat/yet-to-be-decided-api.git

# Navigate to the project directory
cd yet_to_be_decided_api

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# API documentation

# Swagger
http://127.0.0.1:8000/api/schema/swagger-ui/
```

## Usage
Instructions on how to use the project, including any configuration settings or environment variables that need to be set.

```bash

# Start the development server
python manage.py runserver
```
