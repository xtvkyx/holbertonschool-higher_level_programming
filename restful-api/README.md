## 0. Basics of HTTP/HTTPS

### Difference between HTTP and HTTPS
HTTP is the basic communication protocol used on the web. It does **not** encrypt data, so information can be read by others if intercepted.
HTTPS is HTTP with encryption using SSL/TLS, which protects the data from being read or modified. It is used for secure websites like login pages and payments.

### Structure of an HTTP Request
- Method (GET, POST, etc.)
- Path (/index.html)
- Version (HTTP/1.1)
- Headers (User-Agent, Accept, etc.)
- Optional body (for POST, PUT)

Example:

# RESTful API

## Task 1: Consume data from an API using command line tools (curl)

This task demonstrates how to interact with a RESTful API using curl.
### curl --version
Shows the installed version of curl and confirms that it's available.

### GET request
`curl https://jsonplaceholder.typicode.com/posts`
Fetches all posts from the API and returns them in JSON format.

### GET headers only
`curl -I https://jsonplaceholder.typicode.com/posts`
Returns only the HTTP response headers such as status code and content type.

### POST request
`curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`
Sends data to create a new post. JSONPlaceholder simulates creation and returns the new post with id 101.

