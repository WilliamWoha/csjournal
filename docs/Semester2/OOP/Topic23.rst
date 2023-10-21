.. _s2-oop-t23:

23) Association, Composition, and Aggregation
---------------------------------------------

| These three are easy to understand in concept. It's their implementation that gets you confused until and unless you actually practice. All three of them are gonna be covered on this page. Also, we'll be using some Class Diagrams to explain some of the concepts. I personally recommend using `draw.io <draw.io>`_ as it's completely free to use, and the service I'm using for the hosting of these sites (ReadTheDocs) supports extensions for drawing their diagrams on these pages as well. You'll understand what Class Diagrams are and why we need them as we proceed later down the page.
|
| Till now we've been understanding how to do implementations of Objects in Object Oriented Programming. We can create our own Classes, have Data Members and Member Functions for said classes to perform specific operations and manipulate and arrange the data in ways that would be useful to us. The implementation of the Object is complete. We have brought a new creation into the world. Now we must prepare it for socializing, an introvert's biggest nightmare.
|
| Think of an Object as a representation of its real world counterpart. There's relationships and heirarchies. Understanding these let you have reusable and extensible code. You have a car, which has an engine, doors, tyres, windows, a steering wheel, and many other thousands of simpler components working together to make the whole vehicle function. Each part can exist on its own. You can separate the steering wheel or the tyres or even the engine (if you're experienced enough), and put in a different one or repair it, and so on. Similarly, you can have objects of different data types interact with each other and perform operations on data to serve the user. You might think, a car isn't a suitable example since you're not really making Objects of those specific data types, but it is. Take a game like Car Mechanic Simulator. Every single part of the car can be disassembled and modified. Different parts can use different materials and different operations can be applied to each of them. If you still don't understand, though, or haven't played the game, then we can take an example of Amazon, or any shopping website. The interface itself has thousands of categories and millions of products distributed within those categories. Each product is an object, with its own price tag, company of origin, location, URL for the product page, and so on. And products can be added to a Cart. One cart can hold multiple products inside of it. There's also millions of users registered on the site itself, and each user has their own data such as their date of birth, ID, name, etc. These users interact with carts to add or remove products. They can also call a member function of the cart to buy all products at once, or call a member function of buying an individual object. Once a purchase is made, the data is manipulated to alert Amazon that a purchase is made and that a product must be shipped. Then a new Instance of the product is made and shown as something to deliver. Once it's delivered, it's added to the user's page of total things purchased.
|
| I'm going into great detail about Amazon's functionality if it were made via OOP because at my specific university, the final exam question asked you to write the code implementation for it. I don't actually know if Amazon functions like that, but it could. You can do everything that OOP does, without OOP. OOP is just a style, and lets you deal with data in this way. In my own case, other than the exam, I used OOP to create a game called ``Vulcan``. I couldn't publish it because it containted copyrighted music, but it was a space shooter game with a player spaceship, enemy spaceship, bullets, levels, and so on. Each level had enemies, and each enemies had bullets, and each bullet interacted with other bullets or your own ship. All of these interactions are done through Association, Composition, and Aggregation. So, with that out of the way, let's get started.

Relationships
^^^^^^^^^^^^^

| There's many relationships present between real world objects. These are:
*   Part-of (An engine is a part of a car)
*   Has-a (A car has a steering wheel)
*   Uses-a (A driver uses a steering wheel)
*   Depends-on (A flower depends on a bee for pollination)
*   Member-of (A student is a member of a class)
*   Is-a (A square is a shape)
| And yes some of them are different ways of saying the same thing. We'll get to the formal terminologies as far as OOP is concerned now.

Composition
^^^^^^^^^^^

| This is a very close relationship between objects. In simple words, it can be described as ``has a``. Such as, a car has an engine. A human has a heart. A phone has a battery. A CPU has transistors. A room has windows. Now, although I did write a bunch of real world examples, this relation is slightly different for OOP. Here, it's for relationships where one or more simple objects combine to make up a more complex object, and the relationship is so strong that if the more complex object were to be destroyed, then so would the more simpler object. The best example for this is a human and their heart. I'm using the term of destroyed because that's what happens to memory when it's freed. Taking the example of the heart, yes, you can do transplants or store it in special containment units or even the fridge like Medic from TF2 did in Meet The Medic, but unless you're an expert, or insane, or lucky, in 99% of cases, the lesser object will be destroyed when the more complex object is destroyed. It can't exist independently unless you take measures to make that happen, and if you're using this relationship at all, then you're not taking measures to make it happen. You want *all* the memory to be freed when the Class's object is destroyed.
|
| We can take an example from a game, too. Take for example, Minecraft, or GTA, or really any game which has an inventory and a multiplayer lobby. Imagine the Inventory to be an array that stores a bunch of Objects in it, and that this inventory is tied to a class called Player. If you're in a multiplayer lobby, the game has to process the data of every person and their inventories, because that's how multiplayer lobbies work. The other person's data also has to be loaded. Now, if you and another person are playing normally, the game will load the corresponding data on your computer and update the game accordingly. But suddenly, if the other player disconnects, then the game calls a destructor to remove that player's data from your computer, as there's nothing to load anymore. The only reason they keep their inventories when they connect again is because they're stored and reloaded later. We're ignoring that specific detail for now and only considering that they disconnected. The other player is gone, and so is their inventory. The game on *your* end won't load their stuff anymore, so it destroyed the Player Class, and with that, freed up all the memory their presence was taking, including their inventory. It's no longer being loaded on your computer.
|
| It can be something much simpler too. Even the ``ComplexInt`` earlier designed is suitable, despite having only two variables in it. If the object is destroyed, you can't access its variables anymore. But we're usually referring to relationships between *Classes*, and that usually doesn't involve primitive data types such as ``float`` or ``char``.
|
| The relation of Composition applies to any class where the Data Members exist within the lifespan of the Class. Meaning that when the Class is created, so are the Data Members. And when the class is Destroyed, so are the data members. The person is born, they have organs. They die, so do the organs. It's impossible for the Data Members to exist after the class has been destroyed.
|
| You'll understand this relationship better when you see the others in action, as those are relationships where the class can be destroyed but the object can still exist outside of it.
|
| I'm going in depth for this because if you're from the same university as me then you're going to have a *lot* of questions asked about what the relation is and how it works, and how it's different from other types. Realistically, you've already done this with *every single class* done so far, because it's easy to make a class have Data Members that are born and die with the Class. It's Aggregation that gets you confused. Understanding the fundamentals is important so you can learn what to use when and why.

.. code-block:: c++
   :linenos:

    class Coordinate {
    public:
      float x;
      float y;
    };
    class Circle {
    public:
      Coordinate center;
      float radius;
    };
    class Polygon {
    public:
      Coordinate* vertices; // Array of vertices
      int numOfVertices;
    };

| Above is an example of the class ``Coordinate`` having a Composition relation with ``Circle`` and ``Polygon``.
|
| Class relations are standardized and presented in diagram form through something called ``UML Class Diagrams``. https://creately.com/guides/class-diagram-relationships/ has more info about it, and I'd recommend giving it a look because you might get asked to either make these diagrams, or to interpret them. To represent the code above via a UML diagram, it would look like this:
|

.. raw:: html
    :file: images/composition_1.svg

|
| Here's another example of a UML Diagram, and I'll write the corresponding code for it just below.
|
.. raw:: html
    :file: images/composition_2.svg
|
| And finally the code.
|
.. code-block:: c++
   :linenos:

    class Library;
    class Book;
    class Page;
    class Line;
    class Word;
    // I wouldn't be implementing Words as a class as string exists.
    // But sometimes string isn't allowed, so I still implemented it.

    // class Letters is not required as char already exists.

    class Library {
      Book* books;
      int numOfBooks;
    };
    class Book {
      Page* pages;
      int numOfPages;
    };
    class Page {
      Line* lines;
      int numOfLines;
    };
    class Line {
      Word* words;
      int numOfWords;
    };
    class Word {
      char* arr;
      int numOfLetters;
    };

| I never knew about lines 1, 2, 3, 4, and 5 until I started writing this. I never ended up using it but it's still useful. Similar to how you can do ``func();`` and then ``func{ code }``, aka function declaration and definition respectively, you can also declare a class. This process is formally called ``forward declaration``, and https://www.geeksforgeeks.org/what-are-forward-declarations-in-c/ has more details about it. I just put it here for keeping the order. If you don't write those, you just have to make the Classes in reverse order. First the word, then the Line, then the Page, and so on until the Library.
|
| In this specific situation, if you do ``Library* ptr = new Library;``, you'll also be expected to write a destructor for ``Library``, which is going to be a long and tedious process because to prevent memory leaks, you also need a destructor for ``Book``. Each book needs to run a destructor for ``Page``, each page needs to run a destructor for ``Line``,  each line needs to run a destructor for ``Word``, and finally, each word needs to run an operation to ``delete[] arr``. It's like a 5D array, or even 6D if you for some reason decide to make an array of ``Library`` in whatever you're doing.

Aggregation
^^^^^^^^^^^

| This is something we haven't implemented before. Aggregation, in simple words, can be described as ``uses a``. A person uses an address. Every person has an address, but multiple people can live at the same address, and the address doesn't rely on the person to exist. It was already there. Someone either moves in or moves out. A bullet is shot by a gun, but while in flight, if the gun is destroyed, it doesn't matter. The bullet still continues to exist. A driver uses a car, but the car doesn't rely on the driver for existence and destruction. You want to use this kind of relation when you don't want a data member to be destroyed when the class's destructor is called, or if you want something to be linked to multiple Classes, like multiple ``Person`` objects having the same address or same car shared.
|
| Here's the UML Diagram showing Aggregation. Notice that the diamond is hollow instead of filled. Again, I won't be going into details about the diagrams, but they'll still be present here for reference. You can search on the internet for more reference and details about UML Diagrams, or go to https://creately.com/guides/class-diagram-relationships/ to learn more, as mentioned earlier. 
|

.. raw:: html
    :file: images/aggregation_1.svg

|
| You might be wondering how this relation is possible, as the Data Members we've done till now are all Composition based. See, till now we've been using pointers within Data Members just for dynamic arrays. This time, we'll be using them for utilizing this relation. Here's an example of Composition, which I'm putting here to show you how NOT to do Aggregation:

.. code-block:: c++
   :linenos:

    class Part {
        // Code
    };
    class Whole {
    private:
        Part* p;
    public:
        Whole() {
            this->p = new Part;
        }
        ~Whole() {
            delete p;
        }
    };
    int main() {
        Whole w;
    }

| This IS NOT aggregation. I'm specifically writing this here because I made the mistake of thinking that having a pointer counts as aggregation. I didn't understand it properly and suffered the consequences, don't repeat the mistake I did. The above code is Composition, and the *below* code is Aggregation. Go back and forth and see the differences to realize how it works.

.. code-block:: c++
   :linenos:

    class Part {
        // Code
    };
    class Whole {
    private:
        Part* p;
    public:
        Whole(Part* p) {
            this->p = p;
        }
    };
    int main() {
        Part* p = new Part;
        Whole w(p);
    }

| You don't have to throw it in the constructor. This is still just a basic version. In the most realistic implementation you'd be making the Whole have access to ``p`` and lose access to ``p`` at different parts throughout the program using function calls, like throwing a grenade in call of duty but dying just after throwing it. The grenade doesn't vanish with you. Here's an example with both the diagram and the code:
|

.. raw:: html
    :file: images/aggregation_2.svg

|

.. code-block:: c++
   :linenos:

    class Address {
        // Code
    };
    class Employee {
    private:
        Address* address;
    public:
        Whole() {
            address = nullptr;
        }
        void updateAddress(Address* address) {
            this->address = address;
        }
    };
    int main() {
        Address a[4];
        // Pretend there's a bunch of Addresses with values.
        Employee e[10];
        // Pretend there's a bunch of Employees with values.
        e[0].updateAddress(a[3]);
        e[4].updateAddress(a[1]);
        e[2].updateAddress(nullptr); // Clearing the address
    }

Association
^^^^^^^^^^^

| This is basically Aggregation but even more loose. Unlike Composition or Aggregation, where the part is part of the whole object, the associated object has practically no relation to the original object. In aggregation, the relationship is always unidirectional. In an association, the relationship may be unidirectional or bidirectional. An example can be of Doctors and Patients. A doctor does have a relationship with their patients, but conceptually it's not a part/whole (object composition) relationship. A doctor can see many patients in a day, and a patient can see many doctors (like for a second opinion, or needing multiple doctors for different tasks). Neither of the object's lifespans are tied to the other.
|
| This relation is almost never used because it requires at least one of the classes to have forward declaration. Class A has a data member for an object of Class B, and Class B has a data member for an object of Class A. Forward declaration isn't a bad thing, it's just that the situation for the having two classes be members of each other is extremely rare. But, it still exists. https://www.learncpp.com/cpp-tutorial/association/ has more info and some example code for it if you want to know more, and you can go to https://creately.com/guides/class-diagram-relationships/ for the UML Diagram. It's just a line. You're not gonna use this.