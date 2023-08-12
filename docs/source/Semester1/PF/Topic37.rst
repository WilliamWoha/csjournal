.. _s1-pf-t37:

37) Pointer Arithmetic
----------------------

Dynamic Array Declaration
^^^^^^^^^^^^^^^^^^^^^^^^^

| There's Constant Pointers as well but honestly I have yet to find a practical programming question or situation for it as of typing this, so I'm not gonna bother with explaining what that is. It's a simple concept. You can find out more about it on your own if you want to.
| 
| Alright so, last time we declared and deleted a Dynamic Variable in the Heap by using the ``new`` keyword and through the help of Pointers. But what if you wanted to make more than one variable? You'd use arrays! We did them a while back. So, how do we do the same thing but in the heap?

.. code-block:: c++
   :linenos:

    char* ptr = new char[5];

| The heap searches for 5 consecutive memory locations of 1 Byte each which are freely available, and when it finds any 5 which are free, it returns the pointer to the *first* one. This detail is important for actually accessing all 5 memory locations.
| If you wanted to access the first location and use it as a variable, you'd use ``*ptr``. You would dereference it. But for the other 4 remaining locations, the only way to access them, is through Pointer Arithmetic. And here's how it works.

How the Heap stores Values
^^^^^^^^^^^^^^^^^^^^^^^^^^

| (If you don't understand how Hexadecimal works, then skip this paragraph. I haven't explained it. This paragraph is only for people who happen to already know what it is) To keep things short, whenever Binary is used, then the computer uses Binary, Octal, or Hexadecimal. In this case, ``0x`` is the prefix for Hexadecimal, ``0b`` is the prefix for Binary, and a non-zero first number is the prefix for a regular base 10 Denary number. I'll be using ``0x`` because that's what the compiler outputs whenever a memory address is output.
|
| In the code written above, 5 consecutive free memory locations in the Heap were found, and then the address to the first one was returned. Let's call this address ``0x5000``. Don't worry about the ``0x``. If you happen to know Hexadecimal then I explained it in the previous paragraph, but if not, just read it as "location 5000" instead. So! ``0x5000`` is the address of the first free memory location. This means if you did ``cout << ptr`` then you'd get ``0x5000``. You wouldn't actually get that if you run it. You'd get a very different answer. But the concept is the same. If you actually test the ``cout`` statement then you'd get a big set of characters starting with ``0x``. That's the Memory Address of the first free location.
| I mentioned that the 5 free locations were consecutive, right? So where would the next variable be stored? The next address, of course! Meaning if you went to ``0x5001`` then that's where you'd get the second free memory location, or in simple words, ``0x5000`` would be the place where ``array[0]`` is, and ``0x5001`` would be the place where ``array[1]`` is. And this logic carries forward. ``0x5002`` would be the place for the next one, and then ``0x5003``, and then ``0x5004``. Voila, 5 consecutive memory locations.
| So if we want to actually access the other parts of the array we just did, we have two options:
*   1) Since the ``ptr`` is set to ``0x5000``, we can just increment that! ``ptr++`` (or ``++ptr``) will set it to ``0x5001``, and incrementing again will increase it to the next, and so on. BUT! There's a big problem with this. If we increment too many times, we may end up losing the original location of this data. Either the starting point could be lost, or the data in its entirety could be lost if we change the Pointer too much. So this method is only for specific situations. Instead, we use the second, superior method:
*   2) Dereference by writing ``*(ptr + 1)``. And this, is where Pointer Arithmetic comes into play. Right here!
| I only wrote the inferior method first because some of you might have been thinking about it, and I wanted to tell you that it's not gonna work as well as the second one. Pointer arithmetic specifically exists for this reason.

Pointer Arithmetic
^^^^^^^^^^^^^^^^^^

| ``0x5000`` is the location of the first freely available memory location. This Address has been stored in the Pointer. This can be dereferenced by using ``*ptr``. This can also be written as ``*(ptr + 0)``. ``0x5001``, or, in Pointer Arithmetic terms, ``*(ptr + 1)``, is the place where the next value of our array is.
| Pointer Arithmetic is simply using a base pointer and applying numbers to it to get to other memory locations. That's it.
|
| So if in an array of size 100, you'd do ``*(ptr + 50)`` to access ``array[50]``, and ``*(ptr + 99)`` to access ``array[99]``. ``*(ptr + 99)`` is read as "Dereference the value at (99 Addresses after Memory Address at ptr)". ``ptr + 99`` would be read as "99 Addresses after Memory Address at ptr".

.. code-block:: c++
   :linenos:

    int arr[5] = {1,2,3,4,5};
    for(int i = 0; i < 5; i++)
        cout << arr[i] << " ";
    cout << endl;

| The code above prints out all values of an array. The pointer equivalent of that is:

.. code-block:: c++
   :linenos:

    int arr[5] = {1,2,3,4,5};
    for(int i = 0; i < 5; i++)
        cout << *(arr + i) << " ";
    cout << endl;

| You just replace ``arr[i]`` with ``*(arr + i)``.
|
| You might be thinking why I didn't use a Dynamic Array here. And that's to explain Pointer Arithmetic. You might also be confused and thinking if the code I just wrote works, because this *isn't* dynamic. Well, it was shocking to me as well. A lot of things in C++ actually use Pointers but we don't realize it.
| For example, try doing that code above but do ``cout << arr``. What do you get? You get a long string of characters starting with ``0x``. So in reality, ``arr`` is also a Pointer. So writing ``arr[3]`` is in fact just writing ``*(arr + 3)`` in a different notation. Specifically, ``[]`` is called Subscript Notation and ``*()`` is called Pointer Notation.
| Yes, this means you can also use ``ptr[3]`` for accessing a Dynamic Array instead of ``*(ptr + 3)``. But the Pointer Notation is important to know for Dynamic 2D Arrays which is what we're doing in the next Semester, in OOP. (Future Edit: Vectors are so much better than this but our uni forces us to learn these methods, so all we can do is survive.)
| Another example is of a String Literal. A String Literal, if you don't know, is just ``"Writing things in between two speech marks."``. That's also a Pointer. Specifically, it's a Const Char Pointer. You don't need to know what that is but all you need to know is, the Computer reads from the start of this Pointer to a NULL character. So doing ``cout << "Hello!" << endl;`` will result in an output of ``"Hello!"``, but doing ``cout << "Hello!" + 2 << endl;`` will result in an output of ``"llo!"``.
|
| So, all that leads back to accessing a Dynamic Array using Pointer Notation.

.. code-block:: c++
   :linenos:

    int* ptr = new int[5];
    for(int i = 0; i < 5; i++)
        *(ptr + i) = i + 1;

    for(int i = 0; i < 5; i++)
        cout << *(ptr + i) << endl;
    
| The code above will declare a Dynamic Array of size 5, store {1,2,3,4,5} into it, and then Output it. But you can use a Dynamic Array the same way you can use any regular array.
| Finally, the teasing comes to an end. And so does this semester.
|
| Here's how to make an array be made *during* runtime:

.. code-block:: c++
   :linenos:

    int size = 0;
    cout << "Enter Array Size: ";
    cin >> size;
    int* ptr = new int[size];
    for(int i = 0; i < size; i++)
    {
        cout << "Enter value " << i+1 << endl;
        cin >> *(ptr + i);
    }

| There may be someone somewhere reading that and thinking...what about a way to make it so it keeps making more memory as the user enters data, and when the user stops entering data, then it stops making more memory?
| And yes, there is. But unfortunately, it's not with this. Even this has limits. It can't actively change its size during runtime. You can declare it and create it during runtime, and also free it up during runtime, but actively changing its size to expand cannot be done, because the Heap searches for consecutive free locations *only* when the ``new`` keyword is called.
|
| But don't lose hope! There is a way. It's called Vectors. I have no idea how they work, but what I do know is that they're Arrays that can actively change their size at any point. The time of typing this is 19th Feb 2023, at 6:07PM. I've been told I'll learn about Vectors in Semester 3. So, we'll see next year if we learn more about them.
|
| The absolute last thing I wanted to bring up is of how I mentioned that it's important for Pointers to have a data type. Such as writing ``char*`` for a ``char`` data type, or ``int*`` for an ``int`` data type. It's with Pointer Arithmetic. The computer has memory locations, with addresses, and at each address a value can be stored. But the thing is, every single value is the same size: 1 Byte. Every unique memory address associates to one byte of storage. This means that for an array of data type ``char``, the next array value is just one Memory Address across. So ``0x5000`` is the first one, and then ``0x5001`` is the second one. But for ``int``, which is 4 Bytes long, this isn't the case! ``0x5000 0x5001 0x5002 0x5003`` are 4 consecutive bytes in the memory, and all 4 combined would make up one ``int``! So in an array of integers, ``*(ptr + i)`` would end up pointing to ``0x5001``, which is the same value. But see, that's where the Pointer's Data Type comes in. If the Pointer *knows* that it's pointing to an ``int``, then it can automatically account for that! If you do ``*(ptr + i)`` for an array of Integers, you'll notice that there's no errors, and it works fine. This is because the Compiler is automatically moving it 4 Locations (since it's 4 bytes long) instead of one, and you can even see this by doing ``cout << ptr+i`` in a loop. Now, if you don't know Hexadecimal, then it's going to be hard to actually explain that the multiple addresses you see are actually 4 values apart. But I got these two random addresses from my Compiler: ``0x56458a6f02c4`` and ``0x56458a6f02c8``. Even if you don't understand Hexadecimal, look at the last values. It says 4, and then says 8. So for an ``int``, it goes up by 4 Bytes.
|
| The real formula for ``*(ptr + i)`` is ``*(ptr + i multiplied by (size of data type))``, but it's handled by the compiler.
|
| Now, as an absolute final afterthought, yes, if you wanted to for some reason access individual bytes of the same data type via a Pointer, then a Void Pointer does exist. But that's for Semester 2. Anyways, that's it.
|
| Congrats on finishing this semester!

