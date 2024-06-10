import http.client
import base64

proxy_host = 'localhost'
proxy_port = 3128
destination_host = 'www.example.com'
destination_path = '/'

username = 'DEFAULT_USER'
password = 'DEFAULT_PASSWORD'
credentials = f'{username}:{password}'
encoded_credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

# Establish a connection to the proxy server
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Set the proxy authentication
conn.set_tunnel(destination_host, headers={"Proxy-Authorization": f"Basic {encoded_credentials}"})

# Send the request
conn.request('GET', destination_path)

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