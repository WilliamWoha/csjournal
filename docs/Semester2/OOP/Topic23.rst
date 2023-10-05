.. _s2-oop-t23:

23) Association, Composition, and Aggregation
---------------------------------------------

| These three are easy to understand in concept. It's their implementation that gets you confused until and unless you actually practice. All three of them are gonna be covered on this page. Also, we'll be using some Class Diagrams to explain some of the concepts. I personally recommend using `draw.io <draw.io>`_ as it's completely free to use, and the service I'm using for the hosting of these sites (ReadTheDocs) supports extensions for drawing their diagrams on these pages as well. You'll understand what Class Diagrams are and why we need them as we proceed later down the page.
|
| Till now we've been understanding how to do implementations of Objects in Object Oriented Programming. We can create our own Classes, have Data Members and Member Functions for said classes to perform specific operations and manipulate and arrange the data in ways that would be useful to us. The implementation of the Object is complete. We have brought a new creation into the world. Now we must prepare it for socializing, an introvert's biggest nightmare.
|
| Think of an Object is a representation of its real world counterpart. There's relationships and heirarchies. Understanding these let you have reusable and extensible code. You have a car, which has an engine, doors, tyres, windows, a steering wheel, and many other thousands of simpler components working together to make the whole vehicle function. Each part can exist on its own. You can separate the steering wheel or the tyres or even the engine (if you're experienced enough), and put in a different one or repair it, and so on. Similarly, you can have objects of different data types interact with each other and perform operations on data to serve the user. You might think, a car isn't a suitable example since you're not really making Objects of those specific data types, but it is. Take a game like Car Mechanic Simulator. Every single part of the car can be disassembled and modified. Different parts can use different materials and different operations can be applied to each of them. If you still don't understand, though, or haven't played the game, then we can take an example of Amazon, or any shopping website. The interface itself has thousands of categories and millions of products distributed within those categories. Each product is an object, with its own price tag, company of origin, location, URL for the product page, and so on. And products can be added to a Cart. One cart can hold multiple products inside of it. There's also millions of users registered on the site itself, and each user has their own data such as their date of birth, ID, name, etc. These users interact with carts to add or remove products. They can also call a member function of the cart to buy all products at once, or call a member function of buying an individual object. Once a purchase is made, the data is manipulated to alert Amazon that a purchase is made and that a product must be shipped. Then a new Instance of the product is made and shown as something to deliver. Once it's delivered, it's added to the user's page of total things purchased.
|
| I'm going into great detail about Amazon's functionality if it were made via OOP because at my specific university, the final exam question asked you to write the code implementation for it. I don't actually know if Amazon functions like that, but it could. You can do everything that OOP does, without OOP. OOP is just a style, and lets you deal with data in this way. In my own case, other than the exam, I used OOP to create a game called ``Vulcan``. I couldn't publish it because it containted copyrighted music, but it was a space shooter game with a player spaceship, enemy spaceship, bullets, levels, and so on. Each level had enemies, and each enemies had bullets, and each bullet interacted with other bullets or your own ship. All of these interactions are done through Association, Composition, and Aggregation. So, with that out of the way, let's get started.

Relationships
^^^^^^^^^^^^^

| There's many relationships present between real world objects. These are:
*   Part-of (An engine is a part of a car)
*   Has-a ()
*   Uses-a
*   Depends-on
*   Member-of
*   Is-a

Association
^^^^^^^^^^^

| 