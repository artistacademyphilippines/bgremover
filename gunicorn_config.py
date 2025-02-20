# gunicorn_config.py

bind = "0.0.0.0:80"  # Bind to all available IPs on port 8000, adjust the port if needed
workers = 4  # Number of worker processes (adjust based on your CPU cores)
worker_class = "sync"  # Sync worker type, ideal for Flask API
threads = 2  # Number of threads per worker (adjust based on the load)
timeout = 120  # Timeout in seconds (increase if your API performs longer operations)
keepalive = 5  # Keep alive time for HTTP connections
loglevel = "info"  # Log level for Gunicorn
accesslog = "-"  # Logs access requests to stdout (you can set a file path to log into a file)
errorlog = "-"  # Logs errors to stdout (you can set a file path to log into a file)
capture_output = True  # Capture stdout and stderr (useful for debugging)
worker_connections = 1000  # Max number of simultaneous clients for each worker

# Optionally, set a specific user and group to run Gunicorn as (for security purposes)
# user = "www-data"
# group = "www-data"
