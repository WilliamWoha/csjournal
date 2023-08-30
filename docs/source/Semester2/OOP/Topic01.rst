.. _s2-oop-t01:

1) Dangling Pointers
--------------------

| A lot of things were taught in the previous classes. This is in fact the 5th (out of the 32nd) class this semester. But they were just further details about how the memory worked and re-introducing pointers. You can go back to the end of Semester 1 if you need a recap.
|
| When memory is deleted, it isn't actually deleted.

.. code-block:: c++
   :linenos:
   
    int* ptr = new int;
    *ptr = 5;
    delete ptr;
    *ptr = 10;
    cout << *ptr << endl;

| What'll happen?
|
| Let's look at an array. ``0 5 3 2`` are the contents. Let's say I want to completely remove the ``3`` from there. And I don't mean "set the value in that location from 3 to 0". I mean, completely remove it. Wipe it from existence.
| You can't. The location is still there. You'd have to remove it on a hardware level and that's just impossible (to all of you who think it is, just try and do it. Remove only that specific location and no other). All you can do is overwrite the values, not completely remove it from existence. The memory location stays there.
| The ``delete`` keyword only tells the Operating System that the programmer no longer needs to do anything with it. But the location is still there, and it still has the same address. The delete function was called, and then the memory location there was accessed. This Pointer is now what's known as a ``Dangling Pointer``.
|
| This leads into one of the most common problems you'll run into when dealing with Dynamic Memory and Pointers: The unholy ``Segmentation Fault``. The `WikiPedia Article <https://github.com/WilliamWoha>`_ explains it in depth but I'll be summarizing and explaining it here.
|
| A Segmentation Fault occurs when the program tries to access Memory which it isn't allowed to access, or tries to do something with memory it's not allowed to do. This is especially useful, because (despite how frustrating this bug is to come across) it saves programmers from dealing with unpredictable and hard-to-debug scenarios.
| Over time there have been a lot of efforts to try and make it so the program doesn't immediately crash. Because a Dangling Pointer, should in fact cause a Segmentation Fault by that logic. But it doesn't, or at least it doesn't in the compilers I've tried. There are however other ways to make it happen:

.. code-block:: c++
   :linenos:

    int* ptr = NULL;
    *ptr = 5;

    char* str = "hello";
    str[0] = 'i';

    int* ptr = new int[3];
    ptr[10] = 5;

    int* ptr = new int;
    *ptr = 10;
    delete ptr;
    *ptr = 20;

| All of the above scenarios are dealing with memory in a way that's not meant to be dealt with. However if you put them into a Compiler, then only the first two will actually cause a Segmentation Fault, and the last two chunks will both run fine. But that doesn't mean it's ok to do that. The thing is, it depends on the Operating System and the Compiler. A Segmentation Fault is only raised if it's detected, and in some cases it's not detected. There are errors and flags running behind the scenes.
|
| To avoid this error, you just have to be careful about what you're doing with the memory.
| In the case of the first one, the solution is to assign a memory location to the pointer and then dereference it. The pointer is pointing to the NULL address, and you're not meant to change the value at the NULL address.
| For the second one, you'd convert it into a character array because a ``"string literal"`` returns a Constant Character Pointer, so writing ``char str[]`` instead of ``char *str`` lets it be stored as an array instead of constant array. Then individual characters can be modified.
| For the third one, you make sure to stay within the range. This is the most common cause. Just because the code above doesn't raise a segmentation fault, doesn't mean all similar scenarios won't cause it. It'll happen if you're not careful. In 2D and 3D dynamic arrays, even going one over in a loop will make you access a location you're not supposed to. 
| For the last one, the simple step is to write ``ptr = nullptr`` or ``ptr = NULL``, so that just in case you try to accidentally access it again, the compiler warns you against it. Dereferencing ``null`` is the easiest way for it to catch the problem, which is exactly what you *want* it to do. If you used ``delete`` and then tried using the pointer again like normal, then you're using a Dangling Pointer without realizing it. Setting the pointer to ``null`` will prevent you from making that mistake.
| Despite how frustrating Segmentation Faults can be when they show up, they're a blessing in disguise. They're like injuries on the body. Although annoying, it's super important to experience them so you realize there's something wrong happening and it needs to be addressed. If you didn't experience any pain at all you wouldn't know if there was anything wrong with the body that needs fixing. It's your brain's way to tell you to fix something.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 3

    int* ptr = NULL;
    ptr = new int;
    *ptr = 5;

    char str[] = "hello";
    str[0] = 'i';

    int* ptr = new int[3];
    ptr[2] = 5;

    int* ptr = new int;
    *ptr = 10;
    delete ptr;
    ptr = nullptr;
    *ptr = 20; // This will get caught as a Segmentation Fault. This is something you WANT so it stops future problems.
