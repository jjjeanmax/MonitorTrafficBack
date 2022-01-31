from corsheaders.defaults import default_headers, default_methods

#################################
# CORS
#################################

# Disable sending cookies for third-party domains
CORS_ALLOW_CREDENTIALS = False

# List of domains that can work with the API
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    # Local domains (uncomment during development)
    "http://localhost:8000",
    "https://localhost:8000",

    "http://localhost:8001",
    "https://localhost:8001",

    "http://localhost:8080",

    "http://localhost:8081",
    "https://localhost:8081",

    "http://localhost:8888",
    "https://localhost:8888",

]

# Available headers for third party domains
CORS_ALLOW_HEADERS = list(default_headers) + [
    'accept-language', 'connection', 'host',
]

# Available methods for third party domains
CORS_ALLOW_METHODS = list(default_methods) + []
