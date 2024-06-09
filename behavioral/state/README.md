## State

The state disng pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. The pattern involves creating state objects that represent various states of the object and a context object that maintains a reference to the current state object. The context object delegates the state-specific behavior to the current state object.


### When to use the Singleton pattern

- Use the State pattern when the object behavior is determined by its state and the object has to change its behavior at runtime depending on that state.

- Use the State pattern when you have a class with a large number of conditional statements that change the behavior of the class based on the state.

### Pros:
- Single Responsibility Principle. Organizes the code related to a particular state into a separate class.

- Open/Closed Principle. Makes it easy to add new states without changing the context or other state classes.

### Cons:
-  If a system has only a few states or rarely changes states, the State pattern can be an overkill.

### State design pattern example in Python:


```python
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def play(self, context):
        pass

    @abstractmethod
    def pause(self, context):
        pass

    @abstractmethod
    def stop(self, context):
        pass


class PlayingState(State):
    def play(self, context):
        print("Already playing.")

    def pause(self, context):
        print("Pasuing playback.")
        context.set_state(PausedState())

    def stop(self, context):
        print("Stopping playback.")
        context.set_state(StoppedState())


class PausedState(State):
    def play(self, context):
        print("Resuming playback.")
        context.set_state(PlayingState())

    def pause(self, context):
        print("Already paused.")

    def stop(self, context):
        print("Stopping playback from paused state.")
        context.set_state(StoppedState())


class StoppedState(State):
    def play(self, context):
        print("Start playing.")
        context.set_state(PlayingState())

    def pause(self, context):
        print("Can't pause. The media player is stopped.")

    def stop(self, context):
        print("The media player is already stopped.")


class MediaPlayer:

    def __init__(self):
        self.state = StoppedState()

    def set_state(self, state):
        self.state = state

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)


media_player = MediaPlayer()
media_player.play()
media_player.pause()
media_player.play()
media_player.stop()
media_player.pause()

```

Output:
```
Start playing.
Pasuing playback.
Resuming playback.
Stopping playback.
Can't pause. The media player is stopped.
```