.. _s1-pf-t33:

33) Pointers Part 1
-------------------

| Welcome to the bane of my existence.
|
| Ok in all honesty, Pointers aren't that complicated. They're a concept that's simple but people fear them because of how much they're capable of doing. And people also hate doing something in a worse way and having their options limited. Case in point, C++ has dynamic arrays which can change their own size called Vectors, but no we're stuck with using 3D Pointers for Dynamic Memory Allocation instead. It's difficult, but the purpose is to understand the foundations and not be spoiled on easier tasks. This is what makes robust and skilled programmers.
|
| To understand Pointers, the memory must be looked at, and once you understand Pointers, you'll be using them quite a bit. Pointers and OOP make C++ special. The whole reason Pointers exist is for memory allocation and control. If this isn't something you wanted, then you're learning the wrong language. Significantly more control, but significantly more work. That's the trade. Why is control important you might ask? Because it lets you make things far far more efficient and more powerful. RollerCoaster Tycoon is a game which was made in Assembly Language, which is the programming language *just before* the individual bits and transistors of the actual computer itself. And if you look up the minimum requirements for that game, then it runs on a computer with a 90Mhz CPU, 16MB of RAM, and a 1MB Graphics Card. You might think it's that low because the game is old, but 180MB of space is required for it, which is as much as Undertale, a game which takes 2GB of RAM and a 128MB Graphics Card. More than a hundred times more efficient. That's what more Control lets you do.
|
| We declare variables as memory locations to store data.
.. code-block:: c++
   :linenos:

	int a = 10;

| 4 Bytes are reserved in the Memory, and then any modifications done to ``a`` are done to the values at the memory address. As for the memory address itself, we usually don't need it. We can just access ``a`` directly and use it. But if you were curious anyways, then it would be gotten this way:
.. code-block:: c++
   :linenos:

	cout << &a << endl; // Outputs the Memory Location where variable a is stored.

| Now, there's multiple types of Variables. ``int``, ``float``, ``double``, ``char``, ``bool``, ``string``, and so on. Just like that, a Pointer is also a variable. Specifically, it's an ``int``. The only difference is, the values kept in this variable are different from what you'd expect. Instead of holding something like a value of 10, or a specific character, it holds a Memory Location. It is *always* an ``int``, but you'll see later different declarations on it and think otherwise. I'll explain everything in due time. For now, the main gist is this:
|
| Pointers are specific ``int`` variables that hold Memory Locations.
|
| Here's how you declare it:
.. code-block:: c++
   :linenos:

	int* a;

| You might be looking at that and thinking that I just wrote a statement multiplying ``int`` with ``a``. I can't remember if I already wrote about this, but I'll write it again anyways.
| 
| C++ has Operator Overloading. In a ``cout`` statement, you use ``<<`` and ``>>`` for input and output. But those symbols are also used for Bitwise Shifting. Similarly, ``a&b`` is a bitwise ANDing of the variables ``a`` and ``b``, but ``&a`` is the address in the Memory where the variable ``a`` is stored. The same symbol in C++ can be used for different things. So in this case, the Code is not meant to be read as "``int`` times ``a``", but instead as "``a`` is declared as a pointer variable, which is pointing to an ``int`` data type".
|
| I've defined a Pointer as a specific ``int`` variable that holds a Memory Location. Meaning they're as simple as:
.. code-block:: c++
   :linenos:

	int a = 10;
	int* ptr;
	ptr = &a;

| That's it. That's literally it. If you do ``cout << ptr`` then you get the same output as ``cout << &a``. It just holds the Address. But why is it important?
|
| I'll explain how this works in just a bit but the one, fundamental thing to remember, is that Pointers give control over Memory. So much so that they're the only way to access the Heap. What is the Heap you ask? It's the place where you can do
.. code-block:: c++
   :linenos:

	int size = 0;
	cout << "Enter size: ";
	cin >> size;
	int array[size] = {};

| the way it was intended. The Heap is the part of the Computer Memory which is specifically used for Dynamic Memory, and lets you edit the program *while* it is running. That, and Memory Control, is the power of pointers. 
