.. _s1-pf-t07:

7) Inputs, Data Types, and Assigning
------------------------------------

| This whole time we've been doing ``cout``. Now it's time for actually inputting data. Welcome to Variables, Data Types, and ``cin``.

Variables
^^^^^^^^^

| You remember how in :ref:`s1-pf-t04` we talked about Inputs and Variables? I hope you understood it. If not, I'd highly recommend going back and reading it, because these are building blocks of Programs. To summarize it: The computer forgets things unless it stores them in memory, and to make sure it remembers, we tell it to make some room within that memory. That specific space where it stores values are called Variables, and they're most commonly used with Inputs but they can also be used to store other values.

.. code-block:: c++

	#include <iostream>
	using namespace std;
	int main()
	{
		cout << "Enter a number: " << endl;
		cin;
		cout << "Your number is: ";
		return 0;
	}

| The code above is very very simple. It outputs a line telling you (the user) to enter a number, and then using ``cin``, it inputs the number, and then it outputs it.
| 
| But it's wrong. You can try to run that code, and here's the output it will give you:

.. code-block:: c++

	Enter a number:
	Your number is:

| It doesn't remember, because we haven't made a variable yet. So let's try again.

.. code-block:: c++   
   :linenos:
   :emphasize-lines: 5, 7

	#include <iostream>
	using namespace std;
	int main()
	{
		int number; // This is the Variable Declaration statement
		cout << "Enter a number: " << endl;
		cin >> number;
		cout << "Your number is: " << number;
		return 0;
	}

| Reminder: Do make sure that if you're trying this by Copy and Pasting, that the Terminal Option for Code-Runner is enabled.
| 
| Anyways, if you try that second code in VSCode, then it will run exactly like we want it to. It asks for a number, and then whatever number we type with the keyboard, it will actually store it this time into the Memory Location called ``number``. In Line #8, we're now asking it to call the value inside the Memory Location called ``number``.
|
| Now to explain it thoroughly:
*    To make sure the computer actually remembers values, be they input or not, Variables are used. Variables store values. In this case, they're storing numbers.
*    The computer doesn't automatically create Memory Locations. The Programmer has to directly tell the computer to do so, that's what Line #5 is. It's declaring a Memory Location. This Memory Location acts exactly like a Maths Variable, and can be assigned values.
*    The Variable's name is ``number``. It can be named anything else, such as ``a``, ``b``, ``x``, ``name``, ``donut``, etc.
*    The Variable also has a specific Data Type. ``int`` is the Data Type of Integer.

Data Types
^^^^^^^^^^

| There's 6 Data Types in C++:
*    Integer (Declared by ``int``)
*    Float (Declared by ``float``)
*    Double (Declared by ``double``)
*    Boolean (Declared by ``bool``)
*    Character (Declared by ``char``)
*    String (Declared by ``string``)
| The thing is, humans can understand Variables to be anything. They're like boxes. But Computers are, again, stupid. So you use different Data Types depending on what you're doing.
|
| Data Types also have limits depending on their size. Memory is being reserved by the computer, but the computer's memory is not infinite, so it can't store too much.

Integer
"""""""

| The Integer Data Type declares a Variable to store any Integer, and *only* an Integer. This Data Type can't store Fractions or Decimals.
| The range of values for Data Type ``int`` is ``-2147483648`` to ``2147483647``, which are (2\ :sup:`31`\ - 1) and 2\ :sup:`31` \ respectively.
| Remember the Binary system you studied about in :ref:`s1-pf-t01`? A concept of that is used here. The ``int`` Data Type is 32 bits in size, but it also has to store negative values which is why the range isn't from 0 to 2\ :sup:`32`\.

Float and Double
""""""""""""""""

| These Data Types declare variables to store any value at all, and is mostly used for Decimal Values. They use a very complicated formula for doing so, because how the heck do you store Binary numbers in Fractional forms?
| Anyways. This formula allows them to get a range of (±3.4 x 10\ :sup:`38`\) to (±3.4 x 10\ :sup:`-38`\), which means a range of ``±340000000000000000000000000000000000000`` to ``±0.000000000000000000000000000000000000034``.
| There's a catch though. You might be thinking, if they can store values so much bigger and also use decimals, then they're far better than integers, right?
| Nope. Different use cases, and different limits. The thing is, Floating Points use a specific formula to be able to do this. You can look up how Floating Point Numbers work if you're interested. But all you need to know is, the values aren't going to be accurate.

.. code-block:: c++   
   :linenos:

	#include <iostream>
	using namespace std;
	int main()
	{
		cout << int((2.3 - 2.0) * 10) << endl;
	}

| That code above gives the output of 0.3*10, which is supposed to be 3. But if you actually run it, the answer is 2.
| You might be thinking that the int( at the start is responsible for that output. Well, no. You'll learn Typecasting later but for now all you need to know about the int() in the start is, it gives the integer value of any decimal number, without rounding. So int(21.5) would give 21, int(3.00001) would give 3, and int(2.99999) would give 2.
| So from the example of int(2.99999) you can probably guess what's happening here, but if not, I'll still explain.
| Floating point numbers are inaccurate because the formula they use for storing numbers, don't store the *exact* numbers, but rather very very close approximations. 3 is not stored as exactly 3, but instead as something like 3.00000000000054. So in the code above, what's happening is, the result is being calculated as 2.9999999, but it's not at 3.
| 
| The approximation it takes is the closer one. So between, 2.8 and 3.1, for storing the number 3, it will use 3.1. Between 2.99 and 3.02, it will use 2.99. That's why this is happening.
| But that's just how computers are and you can't really do anything about it, though there's something you can do to make things more accurate which is the use of ``Double``. It's the same thing as ``Float``, literally, except it just uses more Memory Locations. This causes the range to increase to (±3.4 x 10\ :sup:`308`\) to (±3.4 x 10\ :sup:`-308`\). It can hold values more accurately than ``Float``, but still can suffer from this problem.
|
| It's not something to worry about at the beginner level. The only reason I bring this up is because, some people tend to think that ``Int`` has no reason to exist if ``Float`` can already hold numbers with decimal points, and also have a much much higher range. This is NOT true. Different Data Types are used for different purposes.
|

Boolean
"""""""

| This one's the simplest and most fun one, I love using it. It can just hold two values and that's it: It can either be set to ``true``, or it can be set to ``false``. It's not really usable for any calculations or anything but it's most useful for Flags, which are something we'll see in :ref:`s1-pf-t12`.

Character
"""""""""
| Ah, the Character. The thing is, with billions of people on the planet and with so many languages and symbols, you might be wondering how it can actually store all of those symbols from all of those languages?
| Well, the truth is, we don't. We do it the *American* way, and just store the English language.
| Other languages can only be stored in computers by using something called the UTF-8 format, but Programming is pretty much entirely in English, so instead, the ASCII table is used, which uses only 8 bits. That gives it upto 255 values, and within that it can store every single letter of the English alphabet, some numbers, some special characters such as ``!@#$%^&*(){}[]:;"'<>,.?/``, some extra things like Escape Sequences ``\t, \n, \\, \", etc``, and more. It's enough for most people.
| 
| Any time you want to work with a single character, you use this. Although you may not really use it for declaration so much, you'll end up using it way more in later concepts such as :ref:`s1-pf-t12`, with things like "Would you like to try again? [Y/N]" and then you can read the individual 'Y' or the individual 'N' if the person presses them. This Data Type is also the foundation for the next one: String.

String
""""""

| Out of the 6 above, 5 are already in ``<iostream>`` and part of the foundation of C++. String is the odd one out. To use it, you need to import the ``<string>`` library.

.. code-block:: c++

	#include <string>

| Strings are just Multiple Characters. The main way to differentiate them is, one character will use ``' '``, while more than one will use ``" "``. 'a' is an example of a Char. "a" is an example of a String. 'aa' is technically a Char data type but it's impossible for this to exist since Char can only store *only* one character.
| Any time you want to store more than one character, you use Strings. There's also Character Arrays but we deal with that later.

Declaration and Assigning
"""""""""""""""""""""""""

| To do a declaration, write ``type name;``. So for example,

.. code-block:: c++
   :linenos:

	int a;	
	int a = 2;
	float num;	
	float num1 = 2;
	double num2 = 3.5
	bool isEven = false;
	char c = 'p';
	string a, b, c;
	string name = "John Cena";
	int a = 2, b = 3, c = 4;

| These are all valid declarations. The less traditional ones ones you can figure out on your own.
| You don't have to immediately assign a value during declaration. You can just assign it later. The way to do so would be ``var = value``. The Equals sign here means the Program is telling the computer to put what's on the right side, into what's on the left side. It's a bit similar to Maths, but not entirely. If you do x = 5 in Maths then you can't do things like 2x = 10. It doesn't know that. You just put the variable name on the left, and the value on the right. But what you can also do is make it calculate the values, and use other variables. So for example I have a variable ``a`` which has a number stored in it, and I want to have another variable ``b`` which has twice the value of ``a``. I can simply do ``b = a * 2`` which is read as "In variable b, store the result of (a times 2)".
| You'll learn more as you keep reading along and eventually things should make more sense.
