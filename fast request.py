import requests

def resolve_https(url, output_file="output.txt"):
    # Make an HTTP GET request
    response = requests.get(url, stream=True)