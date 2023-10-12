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
*   Has-a (A car has a steering wheel)
*   Uses-a (A driver uses a steering wheel)
*   Depends-on (A flower depends on a bee for pollination)
*   Member-of (A student is a member of a class)
*   Is-a (A square is a shape)
| And yes some of them are different ways of saying the same thing. We'll get to the formal terminologies as far as OOP is concerned now.

Composition
^^^^^^^^^^^

| This is a very close relationship between objects. In simple words, it can be described as ``has a``. Such as, a car has an engine. A human has a brain. A phone has a battery. A CPU has transistors. A room has windows. Now, although I did write a bunch of real world examples, this relation is slightly different for OOP. Here, it's for relationships where one or more simple objects combine to make up a more complex object, and the relationship is so strong that if the more complex object were to be destroyed, then so would the more simpler object. Although you can separate an engine from a car or a brain from a human or a battery from a phone, unless you have specific tools or measures to save it, they're going to be destroyed if the car, human, or phone is destroyed.
|
| We can take an example from a game, too. Take for example, Minecraft, or GTA, or really any game which has an inventory and a multiplayer lobby. Imagine the Inventory to be an array that stores a bunch of Objects in it. This inventory is tied to the player. If you're in a multiplayer lobby, the game has to process the data of every person and their inventories, because that's how multiplayer lobbies work. The other person's data also has to be loaded. Now, if you and another person are playing normally, the game will load the corresponding data on your computer and update the game accordingly. But suddenly, if the other player disconnects, then the game calls a destructor to remove that player's data from your computer, as there's nothing to load anymore. The only reason they keep their inventories when they connect again is because they're stored and reloaded later. We're ignoring that specific detail for now and only considering that they disconnected. The player is gone, and so is their inventory.
|
| It can be something much simpler too. Even the ``ComplexInt`` earlier designed is suitable, despite having only two variables in it.
|
| The relation of Composition applies to any class where the Data Members exist within the lifespan of the Class. Meaning that when the Class is created, so are the Data Members. And when the class is Destroyed, so are the data members. It's impossible for the Data Members to exist after the class has been destroyed.
|
| You'll understand this relationship better when you see the others in action, as those are relationships where the class can be destroyed but the object can still exist outside of it.

Aggregation
^^^^^^^^^^^

| This is something we haven't implemented before. Aggregation, in simple words, can be described as ``uses a``. A person uses an address. Every person has an address, but multiple people can live at the same address, and the address doesn't rely on the person to exist. It was already there. Someone either moves in or moves out. A bullet is shot by a gun, but while in flight, if the gun is destroyed, it doesn't matter. The bullet still continues to exist. A driver uses a car, but the car doesn't rely on the driver for existence and destruction. You want to use this kind of relation when you don't want a data member to be destroyed when the class's destructor is called, or if you want something to be linked to multiple Classes, like multiple ``Person`` objects having the same address or same car shared.
|
| You might be wondering how this is possible, as the Data Members we've done till now are all Composition based. Well, not quite. The Data Members present within a class are Composition Based, yes. But if the data members are *pointers*, then it can carry out an Aggregation based relationship, as long as you actually *properly* utilize it.

Association
^^^^^^^^^^^

| This is basically Aggregation but even more loose. Unlike Composition or Aggregation, where the part is part of the whole object, the associated object has practically no relation to the original object. In aggregation, the relationship is always unidirectional. In an association, the relationship may be unidirectional or bidirectional. An example can be of Doctors and Patients. A doctor does have a relationship with their patients, but conceptually it's not a part/whole (object composition) relationship. A doctor can see many patients in a day, and a patient can see many doctors (like for a second opinion, or needing multiple doctors for different tasks). Neither of the object's lifespans are tied to the other.