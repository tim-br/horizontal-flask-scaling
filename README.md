# Horizontal Flask Scaling

A demonstration project showing horizontal scaling patterns with Flask and etcd. This project accompanies the upcoming blog series "Building Scalable Services with Flask and etcd".

## Current Features
- Basic Flask service that multiplies numbers
- Simulated processing delays (2-5s)
- RESTful GET endpoint

## Setup
```bash
# Create virtualenv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run service
python app.py
```

## Usage

`curl http://localhost:5000/multiply/5`
