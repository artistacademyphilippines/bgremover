# gunicorn_config.py

bind = "0.0.0.0:80"  # Bind to all available IPs on port 8000, adjust the port if needed
workers = 4  # Number of worker processes (adjust based on your CPU cores)
