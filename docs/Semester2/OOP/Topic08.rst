.. _s2-oop-t08:

8) Intro to Classes
-------------------

| This part warrants a slight history lesson because once you learn of classes you might be wondering why they exist if Structures are basically identical, or vice versa. So here's one from https://www.freecodecamp.org/news/c-vs-cpp-whats-the-difference/:
|
| In 1979, the researcher Bjarne Stroustrup was hired at AT&T Bell Laboratories. During the 1970s the complexity and computational power of computers increased and limitations in the C programming language started to crop up. In the early 1980s, Bjarne Stroustrup created a new language which was influenced by two things:
*	The Object Oriented Programming capabilities of another language, Simula, which offered a different approach to programming compared to C. Code could be abstracted and better-organized and anything could be represented using classes.
*	The systems programming language, C, which offered the ability to get really close to the machine hardware and do demanding low level computational tasks.
| Those two ideas combined allowed for higher level abstraction without losing the low level efficiency of C. So, the language 'C with classes' was created. In 1984 'C with classes' was renamed to C++. So, C++ is a superset of C, meaning that it was an extension of C and is based on it. C++ just provides additional capabilities to the C language.
|
| The thing is, structures aren't part of C++. They were originally made for C, and don't actually have that much to do with 'Object Oriented Programming'. If you've done OOP before you might have thought that any variable created with the custom Data Type of a Structure might be called an Object, but as https://www.geeksforgeeks.org/structure-vs-class-in-cpp/ put it, an instance of a *Structure* is a Structure Variable, not an Object. Variables made from *Classes* are called Objects.
|
| Alright that's enough teasing, now to get into the actual lesson.

Intro to Classes
^^^^^^^^^^^^^^^^

| Object Oriented Programming aims to organize programs in a way that mimics the real world. Objects have individual attributes and behaviours. It involves thinking in terms of Objects. A fruit is a category. An apple is an Object that belongs to that category. A car is a category. A BMW M3 GTR is an Object that belongs to that category. And different Objects can interact with each other. An animal can eat a vegetable, a Car can be driven by a person, and so on. OOP lets these interactions be possible. It's a style of programming, many like it, many dislike it, but it's still a very fundamentally useful skill to have because it lets you approach some problems which otherwise with regular, what we call 'procedural' programming, would have been significantly more difficult or even impossible (Procedural programming is just using variables and functions without associating anything to Structures or Classes).
|
| A class is an Abstract Data Type, or a User Defined Data Type, similar to a struct. An Object is an instance of a class, the same way a Struct Variable is an Instance of a Struct. A class is like a blueprint and an object is the execution of that blueprint. But this overall concept is a little bit more involved than a Struct. Let's get into the details. 

More about Classes
""""""""""""""""""

| A class has Member Variables and Member Functions, just like a Struct. It has some extra functionality compared to structures however, such as having a Constructor (After some research, I found out Structures in C don't have constructors, but Structures in C++ do. I guess they made their functionality similar to Classes after being carried over from C). Here's the syntax for a Class:

.. code-block:: c++
   :linenos:

    class ClassName {
        Datatype Variable;
	Datatype Variable2;
        ReturnType Function() {
	    // Function Body
	}
        ReturnType Function2() {
	    // Function Body
	}
    };

| It's almost completely identical to a Structure. Here's even a practical implementation of it, you wouldn't be able to tell it's different unless you noticed the syntax saying ``class`` instead of ``struct`` in the first line.

.. code-block:: c++
   :linenos:

    class Rectangle {
	double width;
	double length;

	double displayWidth();
	double displayLength();
	double displayArea();
    };
    int main() {
        Rectangle r1;
        Rectangle r2;
        Rectangle r3;
    }

| However, if you try to do ``r1.width = 5`` in ``int main()``, you'll get an error. It's not accessible in the same way. This is where one of the main differences comes between them: Access Specifiers.

Access Specifiers
"""""""""""""""""

| If you run the code above then try to do ``r1.width = 5`` in ``int main()``, you'll get an error. If you do the same with a ``struct``, however, it'll work normally. This is because Classes, other than being used as a Blueprint to manage data, are also responsible for two key things: ``Data Encapsulation``, and ``Data Hiding``.
|
| Data Encapsulation is just the formal term for grouping data and functionality together. You're already doing it by putting specific variables together and assigning specific functions within the same body of a class or a struct. Data Hiding on the other hand is basically putting all of that into a box and hiding it. You might think, what's the point of making the variables or functions if you can't actually use them? The box is sealed. It's useless to you. Well, yeah. That's because you didn't add an interface to it.
|
| It's kind of like an electrical panel on the wall. Would you rather have to deal with the wires directly, with the risk of messing something up? Or would you rather put it all into a panel and then have switches and control monitors attached to it for easy access and functionality? You're hiding the wires behind the panel by doing the second thing, but doing so significantly reduces risk of something going wrong, and also makes your life easier by having buttons to interact.
| 
| In this case, the struct is giving full access to the wires, but the class is hiding that access. To specify if you want something to be openly available or hidden, you use Access Specifiers. Here's how to write them:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 2,4

    class Rectangle {
    private:
	double width;
    public:
	double length;
    };
    int main() {
        Rectangle r1;
    }

| ``private:`` means, anything written below will be sealed away and inaccessible beyond the body of the class. ``public:`` means it will be available in any other function outside of the class. Here, just for explanation, I've made it so ``width`` is a private member and ``length`` is a public one. Now, ``length`` will act the same way as on previous pages when structs were used. You can just type ``r1.length = 5`` and no errors will be given, it acts as a regular variable. But this won't be the case for ``width``. Here's where you have to actually create the functionality for accessing the private data member, using Getters and Setters. The solution is posted below.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 6,9,12,15

    class Rectangle {
    private:
	double width;
	double length;
    public:
	double getLength() {
		return length;
	}
	double getWidth() {
		return width;
	}
	void setLength(double l) {
		length = l;
	}
	void setWidth(double w) {
		width = w;
	}
    };
    int main() {
        Rectangle r1;
	r1.setLength(5);
	cout << r1.getLength() << endl;
    }

| The ``width`` and ``length`` variables are sealed, and inaccessible. For this reason we've set up the Getters (Lines 6 and 9), and Setters (Lines 12 and 15). And you might be wondering what's the point of these if these are just extra steps to have access to the variables we did, and do the same things we did earlier? It's because there's the option to do more within those codes. For example, width and length can't be negative. So we can modify those further to give specific functionality that otherwise wouldn't be possible with using the variables in their regular way.

.. code-block:: c++
   :linenos:

    public:
	void setLength(double l) {
	    if(l >= 0)
	        length = l;
	}
	void setWidth(double w) {
	    if(w >= 0)
	        width = w;
	}

| In fact, we can write just about any code we want in there, for whatever reason we might need. All we do is flip a switch on a board (aka call the member function). Everything else that happens behind the board isn't our concern, or if it is, then we just do things to make our own lives easier. That's the whole point of the interface. Why bother with trying to change code through variables within a config file instead of going into a game's settings to do it through an easier and more visually appealing menu?
|
| To wrap this page up, I will mention that Structures can also do this. Set Private and Public Data Members. This website https://www.geeksforgeeks.org/difference-c-structures-c-structures/ has more info about the functionality of Structures in C vs C++. So a lot of resources will emphasize on using Classes in C++ instead. Data Hiding is possible in C++ Structures but not in C Structures, which further makes the difference between them smaller, so everything we've done thus far can also technically be done in Structures as well, but nearly all of C++ uses Classes and Class Diagrams because that's just the bigger priority. Structures just got brought along from C, Classes are the bread and butter of C++ Object Oriented Programming, so try to practice with those instead. The whole reason I even covered Structures was because they're still part of the syllabus, and they're so identical that if you learn them you may as well say you've learnt Classes.
