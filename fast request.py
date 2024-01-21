import requests

def resolve_https(url, output_file="output.txt"):
    # Make an HTTP GET request
    response = requests.get(url, stream=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the file in binary mode and write response content
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024*1024):  # Use a 1 MB chunk size
                if chunk:
                    file.write(chunk)
        print(f"Response written to {output_file}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Specify the output file name (change as needed)
output_file_name = "output.txt"

# Call the function with the specified output file
resolve_https("https://www.google.com", output_file=output_file_name)
