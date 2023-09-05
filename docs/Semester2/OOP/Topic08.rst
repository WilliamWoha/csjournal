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

| The thing is, structures aren't part of C++. They were originally made for C, and don't actually have that much to do with 'Object Oriented Programming'. If you've done OOP before you might have thought that any variable created with the custom Data Type of a Structure might be called an Object, but as https://www.geeksforgeeks.org/structure-vs-class-in-cpp/ put it, it's a Structure Variable, not an Object. Variables made from Classes are called Objects.
|
| Alright that's enough teasing, now to get into the actual lesson.

Intro to Classes
^^^^^^^^^^^^^^^^

| Object Oriented Programming aims to organize programs in a way that mimics the real world. Objects have individual attributes and behaviours. It involves thinking in terms of Objects. A fruit is a category. An apple is an object that belongs to that category. A car is a category. A BMW M3 GTR is an Object that belongs to that category. And different Objects can interact with each other. An animal can eat a vegetable, a Car can be driven by a person, and so on. OOP lets these interactions be possible. It's a style of programming, many like it, many dislike it, but it's still a very fundamentally useful skill to have because it lets you approach some problems which otherwise with regular, what we call 'procedural' programming, would have been significantly more difficult or even impossible.
|
| A class is an Abstract Data Type, or a User Defined Data Type, similar to a struct. An Object is an instance of a class, the same way a Struct Variable is an Instance of a Struct. A class is like a blueprint and an object is the execution of that blueprint. But it's a little bit more involved than a Struct. Let's get into the details. 