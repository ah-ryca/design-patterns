## Chain of Responsibility

Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it along the chain.

### When to use the Chain of Responsibility pattern:
- When your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.
- When it’s essential to execute several handlers in a particular order.
- When the set of handlers and their order are supposed to change at runtime.


### Pros:
- Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform these operations.
- Open/Closed Principle. You can introduce new handlers into the app without breaking the existing client code.

### Cons:
- Some requests may end up unhandled.

### Chain of Responsibility design pattern example in Python:
In this example, we will create a chain of middleware components that process incoming HTTP requests.The middleware components are:
- LoggingMiddleware: Logs the request details.
- AuthenticationMiddleware: Checks if the user is authenticated.
- AuthorizationMiddleware: Checks if the user is authorized to access the requested resource.
- ErrorHandlingMiddleware: Catches and handles errors.

Step 1: Define the Middleware Handler Interface
```python
from abc import ABC, abstractmethod

class Middleware(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, middleware):
        self._next = middleware
        return middleware

    @abstractmethod
    def handle(self, request):
        pass
```

Step 2: Implement Concrete Middleware Handlers
```python
class LoggingMiddleware(Middleware):
    def handle(self, request):
        print(f"Logging request: {request}")
        if self._next:
            self._next.handle(request)

class AuthenticationMiddleware(Middleware):
    def handle(self, request):
        if request.get("authenticated"):
            print("User is authenticated.")
            if self._next:
                self._next.handle(request)
        else:
            print("Authentication failed.")

class AuthorizationMiddleware(Middleware):
    def handle(self, request):
        if request.get("authorized"):
            print("User is authorized.")
            if self._next:
                self._next.handle(request)
        else:
            print("Authorization failed.")

class ErrorHandlingMiddleware(Middleware):
    def handle(self, request):
        try:
            if self._next:
                self._next.handle(request)
        except Exception as e:
            print(f"Error handling request: {e}")
```
Step 3: Create and Configure the Chain of Middleware
```python
# Create middleware components
logging_middleware = LoggingMiddleware()
authentication_middleware = AuthenticationMiddleware()
authorization_middleware = AuthorizationMiddleware()
error_handling_middleware = ErrorHandlingMiddleware()

# Configure the chain
logging_middleware.set_next(authentication_middleware).set_next(authorization_middleware).set_next(error_handling_middleware)

# Example requests
request1 = {"path": "/home", "authenticated": True, "authorized": True}
request2 = {"path": "/admin", "authenticated": True, "authorized": False}
request3 = {"path": "/profile", "authenticated": False, "authorized": False}

# Client sends requests to the first middleware in the chain
print("Request 1:")
logging_middleware.handle(request1)
print("\nRequest 2:")
logging_middleware.handle(request2)
print("\nRequest 3:")
logging_middleware.handle(request3)
```
Output:
```bash
Request 1:
Logging request: {'path': '/home', 'authenticated': True, 'authorized': True}
User is authenticated.
User is authorized.

Request 2:
Logging request: {'path': '/admin', 'authenticated': True, 'authorized': False}
User is authenticated.
Authorization failed.

Request 3:
Logging request: {'path': '/profile', 'authenticated': False, 'authorized': False}
Authentication failed.
```