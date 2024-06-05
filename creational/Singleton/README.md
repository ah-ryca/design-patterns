## Singleton

The Singleton design pattern is a creational pattern that ensures a class has only one instance and provides a global point of access to that instance. This is useful in scenarios where exactly one object is needed to coordinate actions across the system, such as a configuration manager, logging system, or database connection pool.

### When to use the Singleton pattern

- Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database connection shared by different parts of the program.

- Use the Singleton pattern when you need stricter control over global variables.

### Pros:
- You can be sure that a class has only a single instance.
- You gain a global access point to that instance.
- The singleton object is initialized only when it is requested for the first time.

### Cons:
- Violates the Single Responsibility Principle. The pattern solves two problems at the time.
- The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.

### Singleton example in Python:

### Method 1: Using metaclass

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

```
A metaclass in Python is a class of a class that defines how a class behaves. A class is an instance of a metaclass. Metaclasses can be used to control the creation and behavior of classes.

**SingletonMeta Class:**  
`_instances`: A class-level dictionary to store the unique instance of each class that uses this metaclass.  
`__call__`: This method is called when an instance of the class is created. It checks if an instance of the class already exists in `_instances`. If it doesn't, it creates a new instance using `super(SingletonMeta, cls).__call__(*args, **kwargs)` and stores it in `_instances`.

**SingletonClass:**  
This class uses `SingletonMeta` as its metaclass. The `__init__` method initializes the instance with a value. Because of the metaclass, only one instance of `SingletonClass` will ever be created.


### Method 2: Using a decorator

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton:
    def some_business_logic(self):
        pass
```

### Method 3: Using a base class

```python
class SingletonBase:
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class SingletonClass(SingletonBase):
    def __init__(self, value):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True
```