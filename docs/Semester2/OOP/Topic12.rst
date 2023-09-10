.. _s2-oop-t12:

12) Constructors and Arrays
---------------------------

| We can never get away from Arrays, can we. But hey, they're useful. I'd much rather go through the pain of learning them than the pain of living in a world without them.
|
| If you define an Array of Objects as such:

.. code-block:: c++

    Circle circles[30];
    // Or
    Circle* ptr = new Circle[30];

| It will use the Default Constructor for every single one of those created Objects in the Array. However, in the absence of a Default Constructor, Arguments are necessary to pass through to the Constructor. In this case, we use an initializer list.

.. code-block:: c++

    Circle circles[3] = {1, 2, 3};

| This only works, however, if the Constructor in question only needs one argument. If it's more than one, then it'll have to be done in the form of a function call.

.. code-block:: c++

    Circle circles[3] = {Circle(1, 1, 3), Circle(2, 1, 4), Circle(-1, 3, 2)};

| I was confused as well when I first saw this, but all you need to know is that the Constructor and Destructor functions themselves can actually be called on their own, just like regular functions. It's just done under very specific scenarios.
|
| It's not necessary to call the same Constructor for every single Object (assuming the other items in the initializer list are acceptable): 

.. code-block:: c++

    Circle circles[3] = {9, Circle(2, 1, 4), 4};

| In case you want to do a very large amount though, you have to do it in two steps:

.. code-block:: c++

    Circle circles[1000];
    for(int i = 0; i < 1000; i++)
        circles[i] = Circle(i, i, 3);

| It could honestly be any value, doesn't matter. I did extensive testing. If an object already exists, then calling the Constructor for it again just acts as an ``update(parameters)`` or ``reset()`` (or even ``reinitialize()`` if you want) function. It just modifies the existing values, completely skipping the process of creating the Object in Memory, since it already exists. There's no Memory Leaks involved with this either.
|
| If you want to initialize an Object made in the Heap, you can do it by simply:

.. code-block:: c++

    Circle* ptr = new Circle(1, 2, 3);
    
| But if there's more than one Object to make then it'll be done using a loop, like earlier.

.. code-block:: c++

    Circle* circles = new Circle[1000];
    for(int i = 0; i < 1000; i++)
        circles[i] = Circle(i, i, 3);