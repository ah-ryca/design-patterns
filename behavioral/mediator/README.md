## Mediator

A behavioral design pattern which reduce dependencied between objects.
It restricts direct communications between the objects and force them to collaborate only via a mediator object.


The primary goal of Mediator is to eliminate mutual dependencies among a set of system components. Instead, these components become dependent on a single mediator object.

- Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes.

- Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other components.

- Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.

---

## An example in TypeScript:
```

interface Mediator {
    notify(sender: object, event: string): void;
}


class ConcreteMediator implements Mediator {
    private component1: Component1;

    private component2: Component2;

    constructor(c1: Component1, c2: Component2) {
        this.component1 = c1;
        this.component1.setMediator(this);
        this.component2 = c2;
        this.component2.setMediator(this);
    }

    public notify(sender: object, event: string): void {
        if (event === 'A') {
            console.log('Mediator reacts on A and triggers following operations:');
            this.component2.doC();
        }

        if (event === 'D') {
            console.log('Mediator reacts on D and triggers following operations:');
            this.component1.doB();
            this.component2.doC();
        }
    }
}


class BaseComponent {
    protected mediator: Mediator;

    constructor(mediator?: Mediator) {
        this.mediator = mediator!;
    }

    public setMediator(mediator: Mediator): void {
        this.mediator = mediator;
    }
}


class Component1 extends BaseComponent {
    public doA(): void {
        console.log('Component 1 does A.');
        this.mediator.notify(this, 'A');
    }

    public doB(): void {
        console.log('Component 1 does B.');
        this.mediator.notify(this, 'B');
    }
}

class Component2 extends BaseComponent {
    public doC(): void {
        console.log('Component 2 does C.');
        this.mediator.notify(this, 'C');
    }

    public doD(): void {
        console.log('Component 2 does D.');
        this.mediator.notify(this, 'D');
    }
}




const c1 = new Component1();
const c2 = new Component2();
const mediator = new ConcreteMediator(c1, c2);

console.log('Client triggers operation A.');
c1.doA();

console.log('');
console.log('Client triggers operation D.');
c2.doD();
```

---

## Another example in GO
### An excellent example of the Mediator pattern is a railway station traffic system. Two trains never communicate between themselves for the availability of the platform. The stationManager acts as a mediator and makes the platform available to only one of the arriving trains while keeping the rest in a queue. A departing train notifies the stations, which lets the next train in the queue to arrive.
## train.go: Component
```
package main

type Train interface {
    arrive()
    depart()
    permitArrival()
}
```
## passengerTrain.go: Concrete component
```
package main

import "fmt"

type PassengerTrain struct {
    mediator Mediator
}

func (g *PassengerTrain) arrive() {
    if !g.mediator.canArrive(g) {
        fmt.Println("PassengerTrain: Arrival blocked, waiting")
        return
    }
    fmt.Println("PassengerTrain: Arrived")
}

func (g *PassengerTrain) depart() {
    fmt.Println("PassengerTrain: Leaving")
    g.mediator.notifyAboutDeparture()
}

func (g *PassengerTrain) permitArrival() {
    fmt.Println("PassengerTrain: Arrival permitted, arriving")
    g.arrive()
}
```
## freightTrain.go: Concrete component
```
package main

import "fmt"

type FreightTrain struct {
    mediator Mediator
}

func (g *FreightTrain) arrive() {
    if !g.mediator.canArrive(g) {
        fmt.Println("FreightTrain: Arrival blocked, waiting")
        return
    }
    fmt.Println("FreightTrain: Arrived")
}

func (g *FreightTrain) depart() {
    fmt.Println("FreightTrain: Leaving")
    g.mediator.notifyAboutDeparture()
}

func (g *FreightTrain) permitArrival() {
    fmt.Println("FreightTrain: Arrival permitted")
    g.arrive()
}
```
## mediator.go: Mediator interface
```
package main

type Mediator interface {
    canArrive(Train) bool
    notifyAboutDeparture()
}
```
## stationManager.go: Concrete mediator
```
package main

type StationManager struct {
    isPlatformFree bool
    trainQueue     []Train
}

func newStationManger() *StationManager {
    return &StationManager{
        isPlatformFree: true,
    }
}

func (s *StationManager) canArrive(t Train) bool {
    if s.isPlatformFree {
        s.isPlatformFree = false
        return true
    }
    s.trainQueue = append(s.trainQueue, t)
    return false
}

func (s *StationManager) notifyAboutDeparture() {
    if !s.isPlatformFree {
        s.isPlatformFree = true
    }
    if len(s.trainQueue) > 0 {
        firstTrainInQueue := s.trainQueue[0]
        s.trainQueue = s.trainQueue[1:]
        firstTrainInQueue.permitArrival()
    }
}
```
## main.go: Client code
```
package main

func main() {
    stationManager := newStationManger()

    passengerTrain := &PassengerTrain{
        mediator: stationManager,
    }
    freightTrain := &FreightTrain{
        mediator: stationManager,
    }

    passengerTrain.arrive()
    freightTrain.arrive()
    passengerTrain.depart()
}
```