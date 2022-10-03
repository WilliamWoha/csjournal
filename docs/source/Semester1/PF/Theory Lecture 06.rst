.. _s1-pft-l06:

Theory Lecture 06
-----------------

| This whole time we've been doing ``cout``. Now it's time for actually inputting data. Welcome to variables, data types, and ``cin``.

.. _s1-t004:

Data Types
^^^^^^^^^^

| There's 6 Data Types in C++:
*    Integer (Declared by ``int``)
*    Float (Declared by ``float``)
*    Double (Declared by ``double``)
*    Boolean (Declared by ``bool``)
*    Character (Declared by ``char``)
*    String (Declared by ``string``)
| Out of the 6 above, 5 are already in ``<iostream>`` and part of the foundation of C++. String is the odd one out. To use it, you need to import the ``<string>`` library.

    | #include <string>
| Integers are Whole Numbers only, Float and Double are Decimal Numbers.
| Character holds the data of a single character in ' ', and String holds the data of multiple characters in " ".
| Boolean has only two options: It is either True or False.
|
| Computers don't recognize letters, their memory holds numbers. So they convert them using the ASCII table. Here's what you need to remember: ``A`` has the integer value of 65, ``a`` has the integer value of 97. REMEMBER THEM. YOU GET ASKED QUESTIONS ON THEM.
| 
| Each data type takes location in memory by varying amounts. Int takes 4 bytes, which is 32 bits, and has a range of ``-2147483648`` to ``2147483647``. Short int takes only two bytes, hence having a range of ``-32768`` to ``32767``. Long int has 8 bytes, and Long Long int has 16 bytes. You can use ``cout << sizeof(int)`` to find the number of bytes they take.
| Float takes 8 bytes, Double takes 16 bytes, Bool takes one byte, Char takes one byte, and String is...we don't talk about that.
| You can transfer values from one variable to another but if the first one was bigger in size than the second then some data is truncated, aka lost. We'll deal with that later.
|
| To do a declaration, write ``type name;``. So for example, ``int a;``, ``float num;``, ``char c = 'p'``, ``string a,b,c;``, ``int a=2;``, ``int x=y=z=4;``, ``float num1=2, num2=3.5;`` are all valid declarations. The later ones you can figure out on your own.
| You don't have to immediately declare a value. You can just assign it later. The way to do so would be ``var = value``. So if you have ``int a;`` and then ``a = 3``, and if you did ``cout << a << endl;``, you'd get an output of 3. The ``=`` is what assigns values.

