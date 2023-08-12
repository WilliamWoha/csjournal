.. _s1-pf-t34:

34) Pointers Part 2
-------------------

| Originally this and the previous page were just one page, but it was a lot of information at once. So I split it in half. This page continues directly from the previous one though.
|
| If you do ``cout << &a``, then you get the Memory Address where ``a`` is stored. So whenever, for some reason, you need to know the Address, you do that. But with an ``int``, there's 4 bytes. Four Memory Locations, so Four Memory Addresses. Meaning ``&a`` is actually referring to the first of those 4 addresses. To explain in House terms, you needed more than one house, so you decided to buy 4 of them side by side, and use them all at once. You build one gigantic house on that. Although there's still 4 addresses, it's all just one house. And if anyone asks for the address, then you give the address to the start. The output of ``&a`` will be different for different computers and environments, but the concept is still the same.
| 
| This is important to know because the way you actually end up configuring the Values (meaning, the data type you declare something as) will affect how the computer actually looks at them and uses them and understands them.
|
| I did mention that Pointers are integer variables. But that doesn't mean you always declare them with ``int*``. That first word instead serves the programmer. ``(Stuff)*`` means, I'm declaring a Pointer which will Point specifically to ``Stuff``. And ``Stuff`` can be anything. An Int, Float, Char, String, and later in Semester 2 when we do OOP, it can also be custom data types. It can even be another pointer, but that comes way later.

.. code-block:: c++
   :linenos:

	int a;
	char b;
	float c;

	int* ptr1 = &a; // This is correct
	char* ptr2 = &b; // This is correct
	float* ptr3 = &c; // This is correct

	int* ptr4 = &b; // This is NOT correct
	char* ptr5 = &a; // This is also NOT correct
	float* ptry &a; // This, too, is NOT correct

| The naming of Pointers follows the same logic as the naming of Variables. I just used ``ptr`` because it's easy to identify. The declarations of ``ptr1``, ``ptr2``, and ``ptr3`` are all correct. But the declarations of ``ptr4``, ``ptr5``, and ``ptr6`` aren't. The reason? The data types the pointers are declared with don't match up with the data types of the actual variables they're pointing to. It's important for them to match, specifically for two reasons:
*	1) So the programmer knows what kind of Data the pointer is pointing to. Makes programming easier. You don't accidentally mix things up because the program forbids you to.
*	2) The more important reason is Pointer Arithmetic. We'll get to that in a bit.
| I do first want to point out some other wrong declarations of Pointers:
.. code-block:: c++
   :linenos:

	int a = 5;
	int* p = a; // Incorrect
	int* p = *a; // Incorrect
	int* p = &a; // Correct
	cout << p << endl; // Will output an address
	a = 50
	cout << p << endl; // Will output the same address
	// The location hasn't changed. Only the values have.

| Now, what if we want to reach ``a`` through ``p``? Well, remember how the ``*`` symbol has multiple uses? It's used here once again, for dereferencing.
| Pointers hold Addresses. But they can also be used to reach the values at said addresses. Here's how:
.. code-block:: c++
   :linenos:

	int a = 5;
	char b = 'B';
	int* ptrA = &a;
	char* ptrB = &b;
	cout << a << " " << b << endl; // Outputs 5 and B
	cout << ptrA << " " << ptrB << endl; // Outputs address of a and address of b
	cout << &a << " " << &b << endl; // Outputs address of a and address of b
	cout << *ptrA << " " << *ptrB << endl; // Outputs 5 and B

| In this case, ``ptrA`` and ``ptrB`` hold the memory addresses of ``a`` and ``b`` respectively. So if we want to see the actual values at the addresses of ``ptrA`` and ``ptrB``, we just Dereference them, by doing ``*ptrA``. This operation is the same as saying "the *value* at this location". So you can use them like regular variables as well.
.. code-block:: c++
   :linenos:

    // Code to swap values of two variables using pointer dereferencing.
	int a = 10;
	int b = 20;
	int* ptr1 = &a;
	int* ptr2 = &b;
	int temp = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = temp;
	cout << a << " " << b << endl; // Outputs 20 10
	cout << *ptr1 << " " << *ptr2 << endl; // Outputs 20 10.
	// The values of a and b have been swapped.

| Multiple pointers can point to one memory location, but one pointer can't point to multiple memory locations.
.. code-block:: c++
   :linenos:

	int a = 10;
	int* p1 = &a;
	int* p2 = &a;

| Lastly, there's the NULL address. I didn't write in my notes whether Pointers during declaration have a Garbage Address, but I don't think they do. I'll have to check that later. But to be safe, it's good practice to declare it as NULL. It's the same as saying ``int a = 0;`` or ``int a[5] = {};``.
.. code-block:: c++
   :linenos:

	int *ptr = NULL;

| To summarize everything of this page and the last one.... And if it doesn't make sense, just keep reading into it and practicing. They'll make sense with practice:
*	Pointers are ``int`` data types that hold Memory Addresses
*	They're important for Memory Control and Dynamic Memory
*	The pointer's data type has to match the variable's data type so Pointer Arithmetic can be done properly
*	Changing the value of a variable will not store the address of it, and hence, won't affect the Pointer
*	Pointers can be dereferenced for accessing the values stored at their addresses
*	Multiple Pointers can point to a single Memory Address
*	Declare a pointer as NULL if there immediately isn't a Memory Location to assign to it
