# http-server
A simple Python-based HTTP server is a program that allows you to serve web content using the HTTP protocol. It listens for incoming HTTP requests from clients (such as web browsers) and responds to those requests by sending back the requested content.


This is a simple Python HTTP server that listens for incoming requests, processes them, and sends back the corresponding responses. Let's go through the code and provide a short description of each section:

1. Importing necessary modules:
   - The `socket` module is imported to create and handle sockets.
   
2. Defining the `generateResponse` function:
   - This function takes an HTTP request as input.
   - It extracts the filename from the request.
   - If the filename is `'/'`, it sets it to `'/index.html'`.
   - It tries to open the file specified by the filename in a `'files'` directory.
   - If the file is found, it reads its content and generates an HTTP response with a status of `200 OK` and the file content.
   - If the file is not found, it generates an HTTP response with a status of `404 NOT FOUND`.

3. Setting up the server:
   - The host is set to `'127.0.0.1'`, which is the localhost.
   - The port is set to `8080`.
   - A socket is created using the `AF_INET` address family and the `SOCK_STREAM` socket type.
   - The `setsockopt` method is called to enable the `SO_REUSEADDR` option, allowing the socket to reuse the address.
   - The socket is bound to the host and port.
   - The server starts listening for incoming connections.

4. Handling incoming requests:
   - In a loop, the server accepts a client connection.
   - It receives the HTTP request from the client and decodes it.
   - The `generateResponse` function is called to generate the appropriate HTML response based on the request.
   - The response is encoded and sent back to the client.
   - The client socket is closed.

This server responds with either the content of a requested file or a "File Not Found" message with the appropriate HTTP status code. It is a basic implementation and should not be used in a production environment, as it lacks error handling, security measures, and scalability features.


## License

This project is licensed under the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/). You are free to download and use this application, but you must provide appropriate credit to the original authors.
