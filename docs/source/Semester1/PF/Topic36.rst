.. _s1-pf-t36:

36) Dynamic Memory Allocation
-----------------------------

| This is gonna get a loooot more tedious in Semester 2. I know, because I'm typing this while already a month into Semester 2. A fantastic schedule I have.
| But for now my notes from the previous semester just explain about this in a very basic level. So this, and Pointer Arithmetic. Then the Semester ends. Hooray!
|
| I'm trying to get my hands on some sample questions my Uni made me do, and also the assignments and stuff. When I find those I'll update the site.
|
| Alright, here goes.
|
| So on the previous page I explained about the memory layout in C Programs. C++ also works like that since it's just C with the ability to do Object Oriented Programming. I don't know if C# is included though. Anyways, the thing about the Heap is, you can't actually access it through normal means. When you write ``int a`` or ``char b`` then the program by default creates those in the Stack. But you can't do the same thing with the Heap. And this is where a major use of Pointers comes in: They're the only way to actually utilize the Heap.

.. code-block:: c++
   :linenos:

    int* ptr = new int;

| The key player in this is the ``new`` keyword. The way it works is, the Heap is just this giant pool of memory that sits there, waiting to be used. It could also be doing something else because of things the programmer is unaware of, but for the most part, it doesn't do anyhting. There's memory available to use there. But when you declare a normal variable, it ends up being declared in the Stack instead. Even pointers are declared in the Stack. In the example above, the actual ``int`` variable, which is the Pointer, is declared in the Stack. So, to actually access the heap, you use the ``new`` keyword.
|
| The ``new`` keyword returns a *Memory Address* in the Heap, and allocates space in the Heap to use as a Memory Location. Using the ``new`` keyword returns an address, and that address has to be stored into a Pointer. And that's exactly what's happening here. We've declared a pointer that will remember the location of this Memory Address, and through this pointer, we can access the variable which has now been prepared in the Heap.
|
| So now, you can just dereference the pointer and use it like a normal variable.

.. code-block:: c++
   :linenos:

    int* ptr = new int;
    *ptr = 10;
    cout << *ptr << endl; // Outputs value at Memory Location. In this case, 10.
    cout << ptr << endl; // Outputs Memory Address in Heap where value is stored.

| Since we did an ``int``, it means 4 Bytes have been prepared in the Heap, and the address to the start of those first 4 bytes has been returned and stored in the pointer.
|
| If we were to instead do:
.. code-block:: c++
   :linenos:

    char* ptr = new char;

| Then only one Byte would be prepared in the Heap.
|
| The thing with Dynamic Memory Allocation is, that this ability to access the Heap also requires manual cleanup. If you call a function, then the variables declared in that function are all destroyed when that function calling is complete. This is to save up on memory. But the Memory *Locations* themselves aren't destroyed. The Computer just remembers that there's no more use for those specific locations, and then declares them as 'free to use'. Data isn't ever destroyed. It's declared 'free', then new data is put there.
|
| Just like that, data in the Heap also has to be freed when there's no longer a use for it. That power comes with the ``delete`` keyword.

.. code-block:: c++
   :linenos:
   
   int* ptr = new int;
   delete ptr;

| What the code above does is, in the first line, the computer searches for free data in the Heap, and when it finds it, it returns the address to it and stores it in the pointer.
| Now lets say we've done everything we've wanted to with that data, and no longer need it. So we tell the computer, "Hey! You can have this back. I don't need it anymore." That's what the ``delete`` keyword does. It tells the computer that we no longer need the data, and hence, the computer declares that specific memory location to be free again.
| If you don't end up deleting the data but also don't use it, then it's the equivalent of a Memory Leak. I'll go more in depth in Semester 2 for what a Memory Leak is, but it just means wasting memory.
|
| Alright, onto the last topic of this Semester. Pointer Arithmetic, here we come.