import socket

# website to target
website = "www.example.com"

# create a socket and connect to the website on port 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((website, 80))

# send a GET request for the website's root page
sock.sendall(b"GET / HTTP/1.1\r\nHost: " + website.encode() + b"\r\n\r\n")

# receive and print the banner
banner = sock.recv(1024).decode()
print(banner)

# close the socket
sock.close()
