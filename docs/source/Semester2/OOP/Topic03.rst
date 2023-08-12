.. _s2-oop-t03:

3) Multidimensional Pointer Arrays
----------------------------------

| Until now we've been working with Pointers in only One Dimension. A Pointer is an integer that holds a memory address. But they can go even further beyond, and become even more annoying to deal with.
|
| I'd say something like "If you wanted to do (x), how would you do it?", but I've yet to properly find out what (x) is, so instead I'll just type this and explain *later* how it's (somewhat) useful.
|
| Here's a small thing that will be useful for pointers which my teacher told me:
.. code-block:: c++
   :linenos:
    
    const int b = 3;
    const int* p = &b;
    int* const c = 4;
    const int* q = &c;

| Anything on the left of the right-most asterisk (``*``) is the thing the pointer is pointing to. So an ``int*`` means it's a pointer, pointing to an int. ``int**`` means it's a pointer, pointing to an ``int*``.
| Yes I just dropped constant pointers here but they're super simple. ``const (data type)* (pointer name)`` just means the pointer is pointing to a const, meaning you can't edit the dereferenced value, but you can change the pointer itself. ``(data type)* const (pointer name)`` just means the pointer itself is a constant and always going to point to one memory location, but you can edit the value in that location. I'm not going into detail for it because constant pointers have only very briefly been touched in my course. I only wrote them here to make the point written earlier: Anything on the left of the right-most asterisk is the thing the pointer is pointing to.
|
| Now for the actual Dynamic Multidimensional arrays.
|
| It's super similar to how regular Multidimensional arrays work. We'll even take the same example.
.. code-block:: c++
   :linenos:

    int* programming = new int[10];
    int* maths = new int[10];
    int* physics = new int[10];
    int* english = new int[10];

| ``programming`` is one array. ``maths`` is another. But what if we wanted more subjects? 
| Unfortunately this time it's not as simple as ``int subjects[4][10]``. We have to go a bit more in-depth.
|
| Every single pointer above, is pointing to 10 locations in the Heap. So a total of 40 locations are occupied. But these 40 ``int`` values are not all together. They're in different, random parts of the Heap. The pointers themselves are not together (in the stack). They're all separate. So it's 4 different pointers, and each pointer is pointing to an array. There's no way to connect them together, unless you do it yourself.
|
| Remember earlier, how anything written on the left is the thing the pointer is pointing to? It doesn't stop at a data type. In fact, it can even point to another pointer.

.. code-block:: c++
   :linenos:

    int a = 5;
    int* ptr = &a;
    int** qtr = &ptr;

| Let's say that ``a`` is stored in the Memory Location ``0x5000``. That location is then stored into the value of the Pointer known as ``ptr``. ``ptr`` is an Integer, and it has its own Memory Location ``0x7000`` where it is stored. But since ``ptr`` is a pointer, the value it holds is ``0x5000``. Now, you've declared another Pointer, called ``qtr``, and you want to use ``qtr`` to access ``a``, but by using ``ptr``. So you'd think doing ``qtr = &a`` is the best option, and you'd be right, but that's something different. No, you have to get to it through ``ptr``. And that's where Double Pointers come in. Although I don't have many examples of where they are useful, they're the only way to make 2D and 3D and more-D *Dynamic* arrays. So ``qtr``, which is declared at a completely separate Memory Location, let's call it ``0x8000``, is now pointing to ``0x7000``, which is the address of ``ptr``, and ``ptr`` is pointing to ``0x5000``, which is the address of ``a``.
| 
| This allows you to now access ``a`` through ``qtr``, by Multi-dereferencing.
|
| If you did ``*ptr``, then you'd dereference the Pointer, and it would be the same as typing ``a``. Now, if we try the same, meaning if we wrote ``*qtr``, then we'd get ``ptr``. Pay attention: We would NOT get ``*ptr``, we would get ``ptr``, meaning that writing ``*qtr`` is the same as writing ``ptr``. Writing ``ptr = &a`` is the same as writing ``*qtr = &a``.
| But we don't want that. We want to modify ``a`` directly. Well, since ``*qtr`` is the same as writing ``ptr``, aka ``*qtr == ptr``, if we apply another asterisk, what will happen? ``**qtr``. Keeping the maths equality, you get ``**qtr == *ptr``. And that's the solution. Since ``qtr`` is a double pointer, it needs to be dereferenced twice to get to the variable. ``**qtr = 10`` would modify ``a``, the same way ``*ptr = 10`` would.
| And just like that if we have an even longer chain, it would work the same way. ``int**** qtr`` would require 4 asterisks (``*``) to access the variable.
|
| And you might think that this just ends up adding extra steps...and for what? Just access it normally.
|
| But see, that's just a bad use case for this. Multidimensional pointers, are what also allow us, to deal with Multidimensional Arrays. Here's how:
| Going back to the example of ``programming``, ``maths``, ``physics``, and ``english``. 4 different pointers in different memory locations, pointing to 4 completely unique groups of data in the heap. There needs to be something that connects them. So what do you use? Here's one possibility:

.. code-block:: c++
   :linenos:

    int* programming = new int[10];
    int* maths = new int[10];
    int* physics = new int[10];
    int* english = new int[10];

    int* subjects[4];
    subjects[0] = programming;
    // subjects[n] is the same as writing *(subjects + n)
    subjects[1] = maths;
    subjects[2] = physics;
    subjects[3] = english;

| So now you have the 2D Array of ``subjects``. And writing ``subjects[a][b]`` will let you access any value in the ``[4][10]`` spectrum. But....this isn't dynamic. Because ``subjects`` was declared in the stack, and Dynamic would mean being able to have it be any size.
| I only did this as a way to approach the solution. This isn't the solution, and this is also not something anyone should practically use.
|
| The reason the code above worked is because we made an array that stored Integer Pointers (``int*``). And what did we discuss earlier could store another pointer? A 2D Pointer! So just like how in a regular integer array ``int a[]``, ``a`` is a pointer, here, ``subjects`` is also a pointer. But it's a 2D Pointer. It's an array of 1D Pointers which are kept together using 2D Pointers. So all we have to do is convert this into the dynamic equivalent, using the Heap.
.. code-block:: c++
   :linenos:

    int* programming = new int[10];
    int* maths = new int[10];
    int* physics = new int[10];
    int* english = new int[10];

    int** subjects = new int*[4];
    subjects[0] = programming;
    subjects[1] = maths;
    subjects[2] = physics;
    subjects[3] = english;

| ``new int*`` means, make space in the Heap for the ``int*`` data type. 
| But this isn't the final form. The one drawback with this is that it needs you to manually make so many 1D Arrays to then store in the 2D Array. So, there's an easier solution. And this last code is the final answer for a 2D Dynamic Array.
|
| Instead of having to first make 1D Arrays and then storing them in the Array of Pointers (The 2D Part), we can go the other way around.
.. code-block:: c++
   :linenos:

    int** subjects = new int*[r];
    for(int i = 0; i < r; i++)
        subjects[i] = new int[c];

| And done. That's it. You now have a 2D Dynamic Array, where ``r`` is the number of rows, and ``c`` is the number of columns.
| Here's how you make a 3D Version: 
.. code-block:: c++
   :linenos:

    int*** subjects = new int**[a];
    for(int i = 0; i < a; i++)
    {
        subjects[i] = new int*[b];
        for(int j = 0; j < b; j++)
            subjects[i][j] = new int[c];
    }

| Where ``a``, ``b``, and ``c`` are the dimensions of the 3D Matrix. Like a cube.
| For every dimension you just keep adding more loops to initialize. But once that initial process is done, you have yourself a dynamic array.
|
| The only caveat other than declaring it is deleting it to stop a memory leak. That's gonna be fun.
        
