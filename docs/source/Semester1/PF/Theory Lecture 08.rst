.. _s1-pft-l08:

Theory Lecture 08
-----------------

| Week 4.
| This is gonna be a long one because of something called the Keyboard Buffer. Get ready.

.. _s1-pft-t008:

Variable Assigning using itself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: c++

	int sum = 30;
	sum = sum + 10;

| Does that make sense to you?
| If you called ``sum`` after those two lines, you'd get a value of 40.
| When assigning (meaning in statements with ``=`` in them), the Compiler first works out the things on the right side, then assigns it to the variable on the left side. So for the line ``sum = sum + 10``, it first takes the value of ``sum`` from memory, does the required operations on it (in this case, addition of 10), and then assigns it. It just so happens to be that the assigning part happens to be at the original memory location.
| In these situations, aka the ones where the variable works on itself, we can do something called `Combined Assignments`.
*    ``sum = sum + 10`` is ``sum += 10``
*    ``sum = sum - 10`` is ``sum -= 10``
*    ``sum = sum * 10`` is ``sum *= 10``
*    ``sum = sum / 10`` is ``sum /= 10``
*    ``sum = sum % 10`` is ``sum %= 10``
| If we do ``cout << sum + 10``, will the value of ``sum`` change? No. That just calculates and then outputs, there's no assigning taking place.

| ``x += b + 5;`` is just
| ``x = x + b + 5;``

.. _s1-pft-t009:

Keyboard Buffer (.get(), getline(), .ignore())
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Here's a funny thing about using ``#iostream <string>``. If you try to put data into a ``string`` variable via a ``cin`` statement, it won't store values past an escape sequence. Here's the program:

.. code-block:: c++

	string name;
	cin >> "Enter name: ";

| If I write John Cena into that, then try to check the value of ``name``, it will give me an output of ``John``.
| But there's this thing called the Keyboard Buffer. The thing is, this Buffer holds the data for all the keys pressed via the keyboard. ``John Cena`` is stored in the Keyboard Buffer, but the ``cin`` statement only read it until ``John``.
| Here's an even funnier thing:

.. code-block:: c++
   :linenos:

	string name, city;
	cout << "Please enter your full name: " << endl;
	cin >> name;
	cout << "Please enter your city: " << endl;
	cin >> city;
	cout << "Your full name is " << name << ", and your city is " << city << endl;

| If you ran that code and entered John Cena into the first prompt for an input, then you wouldn't even get the second prompt, and the code would output: ``Your full name is John, and your city is Cena``. This is because of the Keyboard Buffer.
| "John Cena" is stored in the buffer, but the ``cin`` statement finds an escape sequence at the space present between John and Cena. So it stops there. But then another ``cin`` statement is called. Since it stopped at the space button, it then picks up from there and finds Cena, and just puts that into the second ``cin`` statement.
|
| The solution? Use a thing called ``getline(cin, var);``. It works the same way as ``cin >> var;``. You just write ``getline(cin, var);`` instead. But the difference is, this time no matter what you write, all of it will be stored into the variable. It only stops when the Enter key is pressed, and doesn't store the ``\n`` from that either.
|
| There's also ``.get()``. You write it as ``var = cin.get()``. This will read any key that is pressed and store it into the variable. Be it Enter, Space, Escape, Tab, anything. It reads all of it. It's used in games for checking for specific button key presses.

.. code-block:: c++
   :linenos:

	char key;
	cin >> key;
	if (key == '\n')
	{
    		// (Some Code to trigger something)
	}

| You want it to only work when Enter is pressed, but ``cin`` won't store Enter. So the solution? Replace ``cin >> key;`` with ``key = cin.get()``. If you press Enter, then ``\n`` will be stored into ``key``.
| If you just write ``cin.get();`` then it won't store the key, but instead works like a "Press Any Key to Continue" button.
| 
| There's an even funnier problem though.

.. code-block:: c++
   :linenos:

	int number;
	char ch;
	cout << "Enter number: " << endl;
	cin >> number;
	cout << "Enter Character: " << endl;
	cin.get(ch);
	cout << "Thank you." << endl;

| This code has a problem.
| You won't get the opportunity to store a character into the ``cin.get()``.
| In the first ``cin``, if you write 324 then press Enter, the buffer would have these characters in it:
| ``3`` ``2`` ``4`` ``\n``
| ``\n`` is an escape sequence and is one character. ``cin`` reads until that point and stores the numbers into the variable, but ``\n`` isn't removed, it's still there. That gets stored into ``cin.get(ch)``. You don't get the prompt.
|
| The solution? Another command. ``cin.ignore(cond1, cond2)``. This is mentioned now instead of way back with John Cena because it only solves the problem of the rest of the Keyboard Buffer going into the next ``cin`` statement. It didn't solve the problem of Space not being stored.
| ``cin.ignore(cond1, cond2)`` will ignore characters in the Keyboard Buffer until either Condition 1 is fulfilled, or Condition 2 is fulfilled. Condition 1 is a number value, and Condition 2 is a character check. ``cin.ignore(20,'\n')`` will ignore characters in the Keyboard Buffer until a ``\n`` is found, or until 20 spaces.

