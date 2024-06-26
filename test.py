import http.client
import base64
import sys
import time

time_allowed_running = 10

proxy_host = 'localhost'
proxy_port = 3128
destination_host = 'www.example.com'
destination_path = '/'

username = 'DEFAULT_USER'
password = 'DEFAULT_PASSWORD'
credentials = f'{username}:{password}'
encoded_credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

# Start counting the time
start = time.time()

# If more than 'time_allowed_running' seconds have passed, exit
while time.time() - start < time_allowed_running:

    # Establish a connection to the proxy server
    conn = http.client.HTTPConnection(proxy_host, proxy_port)

    # Set the proxy authentication
    conn.set_tunnel(destination_host, headers={"Proxy-Authorization": f"Basic {encoded_credentials}"})

    try:
        print(f"Sending the request to {destination_host}")
        conn.request('GET', destination_path)
    except Exception as e:
        print(f"Failed to send the request: {e}")
        continue
    else:
        # Get the response from the server
        response = conn.getresponse()

        # Read the response content
        content = response.read()

        # Assert the response status code
        assert response.status == 200, f"HTTP Error: {response.status} {response.reason}"

        # Print the response content
        print(content)

        # Make sure "<title>Example Domain</title>" is in the response content
        assert b"<title>Example Domain</title>" in content

        # Close the connection
        conn.close()

        # Print success message
        print("Success")
        sys.exit(0)

# Print failure message
print("Failed")
sys.exit(1)
