.. _s2-oop-t24:

24) Intro to Inheritance
------------------------

| *The syntax might seem much sweeter*
| *Where objects and subtypes play*
| *But frills like inheritance*
| *Will only get in the way*
|
| (https://youtu.be/tas0O586t80 if you're interested in where that's from)
|
| I hope you understood the previous page because this one is going to get way more complicated. In :ref:`s2-oop-t08` I talked about how there were Categories, and Objects that belonged to categories. 
|
| ``"A fruit is a category. An apple is an Object that belongs to that category. A car is a category. A BMW M3 GTR is an Object that belongs to that category. And different Objects can interact with each other. An animal can eat a vegetable, a Car can be driven by a person, and so on. OOP lets these interactions be possible."``
|
| With inheritance, we're expanding on that. It's not so straightforward as, ``car`` and then ``BMW M3 GTR``. If you're working with way more data and need to handle more classes then you need extra specifications. So something like ``Vehicle``, which has the Objects ``Car``, ``Train``, ``Boat``, and ``Plane``. Then ``Car`` could further have ``Sports Car``, ``Road Car``, ``Vintage Car``. ``Sports Car`` could have ``BMW M3 GTR`` or ``Porsche 918 Spyder`` or ``McLaren P1``. ``Vintage Car`` could have ``VW Beetle`` or ``Ferrari 250 GTO`` or ``Aston Martin DB4``. You get the point. Instead of making one Class, and then an Object, we're making an entire hierarchy, and as we go down, we finally get to the Object we're making.
|
| Here's a UML Diagram representing this scenario:
|

.. raw:: html
    :file: images/inheritance_1.svg

|
| I didn't add the specific car examples because those are ``Objects`` and not actual Classes. Everything you see above is a Class. You *can* put Objects into diagrams like this if you're making it through draw.io or whatever other service, but we're not dealing with that right now.
|
| The purpose of this? Code reusability and Polymorphism. We'll do Polymorphism later. Let's say you wanted to have 3 Classes: ``Circle``, ``Rectangle``, and ``Triangle``. Each of those would have their own Data Members and Functions. With this specific example, you'd have only a handful of Data Members, but if the Class were way bigger or way more complex, then you'd be dealing with way more code, and a lot of it would be repeated. Instead, if you define a Class as ``Shape``, and make it have all the fundamental features, then you could make ``Circle``, ``Rectangle``, and ``Triangle`` inherit from that class. You'd be repeating things way less. Why bother repeating code that's similar between two different Classes? There's a billion other examples where Inheritance is useful. Basically anything that can have a hierarchy can have inheritance. The other useful thing about it is that it reduces workload on the programmer for similar scenarios. If you wanted to modify the code for ``Circle``, ``Rectangle``,  and ``Triangle``, then you'd have to go into all of those Classes and do it individually. With inheritance, you only have to modify the base class.
|
| Inheritance lets you create a new class from an existing class. The new class inherits all the functionality and data members of the existing class, and adds its own capabilities to it. The Base class, also called the Parent class, which is what we inherit from, is unchanged by the process. The base class has many common characteristics. The new class, which we call a Derived or Child class, is a *specialized* version of the existing class. Every class derived from the base class will have these same characteristics, but on top of that they'll have unique attributes as well. All insects have similar characteristics, but a bee and a grasshopper have further special features. It goes from generic to specific. ``Vehicle`` to ``Car`` to ``Sports Car`` to ``BMW M3 GTR``. ``Vehicle`` is generic, and ``BMW M3 GTR`` is specific. The higher up you go, the more it becomes generalized (or abstracted). The lower you go, the more it becomes specialized.
|
| Inheritance specifies an ``is-a`` relationship. A BMW M3 GTR is a Sports Car. A Sports Car is a Car. A Car is a vehicle. A poodle is a dog. A flower is a plant. A football player is an athlete.
|
| This page just serves as an introduction page describing the relation. It's not as simple as, how to have two classes use each other. There's way more to it, and we'll be covering it all on the next page. The list is as follows:
*   Class Access
*   Constructors and Destructors
*   Method Overriding
*   Single-Level, Multi-Level, and Multi Inheritance
*   The Diamond problem
*   Virtual Inheritance
| And no, it doesn't actually end there. That's *almost* where it ends. The thing is, inheritance is just a runner-up for what is arguably one of the most powerful operations you can do in C++: Polymorphism. To give a preview of what that is, imagine you have a game with 50 characters. We can take Tekken. Each Character is its own Class, pre-defined before the game runs, and when choosing a character you just set one of those Objects as the active one. But having 50 Objects be declared is a lot of memory, and it's especially more complicated and confusing if every object handles things differently with different functions. Although each character in Tekken can do the same thing, such as Punch or Kick, it doesn't do it the same way. They do them at different damages, different speeds, different sound effects are played, and different animations are rendered. And to keep track of every single one is going to be a nightmare. Polymorphism lets you manage it all in a way more simple and effective manner. Instead of having ``PandaKick()`` or ``BobPunch()``, you just have a class ``Bob`` or ``Panda`` and both of those have the functionality of ``Punch()``. Easier to remember, less syntax to deal with.