.. _s1-pf-t19:

19) WHILE Loops
---------------

| Another holy grail. Though I talked about it far less in the pages that lead up to it compared to :ref:`s1-pf-t12`. If your knowledge of IF statements needs improvement though then I'd recommend going back there and revising, because it is a *fundamental* part in knowing how Loops work.
|
| There's 3 types of LOOP structures. ``WHILE``, ``DO WHILE``, and ``FOR``. And *all of them* rely on the logic of IF statements. We'll be talking about WHILE structures on this page.
|
| Let's say you want to write ``Hello World!`` 10 times. Then there'd be 10 statements.


.. code-block:: c++
   :linenos:

	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;
	cout << "Hello World!" << endl;

| Which is fine, it's not taking up too much space. But what if you wanted to write it 100 times? That would take up 100 lines of space.
| We can make it much easier, and also make it dynamic, by using WHILE loops. This lets us not only repeat something over and over, it also lets us define how many times to repeat it.
|
| A WHILE loop is sipmle. In Layman's terms, it translates to "As long as this is happening, do this". In more Pseudocode terms, it translates to "As long as (Condition) is true, do this". That's it.
| Here's how to write it.


.. code-block:: c++
   :linenos:

	while (condition)
	{
		cout << "Hello World!" << endl;
	}

| The loop breaks the moment the ``condition`` is no longer true.
| BUT. You have to be careful. If you set a condition that never changes within the loop, then you can't break out.
| For example:


.. code-block:: c++
   :linenos:

	while (5 > 3)
	{
		cout << "Hello World!" << endl;
 	}

| The code above would run until the end of time itself. Or until it crashes or gets stopped by the user, or whatever. It keeps checking, "Is (5 > 3) true?" and it keeps saying yes, so it keeps going into the loop.
| The loop is supposed to continue until the statement is *no longer* true. "As long as (condition) is true, do this. But when it's no longer true, stop doing this". So you have to do something to make it no longer true.
|
| There's multiple ways to go about this. The most popular is with a counter variable.


.. code-block:: c++
   :linenos:

	int counter = 0;
	while (counter < 10)
	{
		cout << "Hello World!" << endl;
		counter++; // Again, it's the same as ++counter, if used on its own.
	}

| That loop would output 10 ``Hello World!"`` statements.
| Here's what's happening:
*    First the while() condition works like an IF check. It sees, ``is (counter < 10) true?``, which it is, since we defined it to be 0. So it goes into the loop.
*    It then carries out the code found within the loop. In this case, the ``cout`` statement.
*    The statement for increasing ``counter`` is also part of the code within the ``{loop}``. So it also runs that.
*    When it reaches the end of the loop, and arrives at ``}``, it then goes back to the start, and goes to the first step, checking the condition again.
*    If it finds that the condition is true, it then continues with the loop. In this case, the value of ``counter`` is only 1. So it goes again.
*    On the third loop, the value would be 2, and then it would be 3, then 4, and so on, until it reaches 9.
*    On the 9th *loop*, ``counter++`` would make it have a value of 10.
*    Once it reaches the end of the loop, it then goes back and checks, ``is (counter < 10) true?``, which now, is not. So it breaks the loop.
| One thing to note here, is that the condition check is done only when the code reaches the closing bracket ``}`` of the WHILE structure. If you had a bunch of code, and put ``counter++`` at the start of it, and the value of ``counter`` was now a value that would render the original condition as false, the rest of the code would still execute. It doesn't immediately stop, it only does the check when the block of code finishes.
|
| What's even more useful about LOOPs though, is that their ability to change values with iterations can be used for making code that changes itself!
|
.. code-block:: c++
   :linenos:

	int counter = 0;
	while (counter < 10)
	{
		cout << counter << '\t' << counter*counter << endl;
		counter++;
	}

| The code above would give this output:

.. code-block:: c++
   :linenos:

	0	0
	1	1
	2	4
	3	9
	4	16
	5	25
	6	36
	7	49
	8	64
	9	81

| Which is an output of every number from 0 to 9 and its square!
| If I wanted to make it from 1 to 10 then I'd make it ``counter = 1`` and ``while (counter < 11)`` or ``while (counter <= 10)``. It wouldn't work on ``while (counter == 10)`` because then it wouldn't go into the loop at all. The condition check would fail.
|
| If you wanted to do a loop that showed even numbers from 1 to 100, the code would be:

.. code-block:: c++
   :linenos:

	int counter = 2;
	while (counter <= 100)
	{
		cout << counter;
		counter = counter + 2;
	}

| From the code above you can see that it doesn't even have to be incremented by 1, it can be done using whatever Condition and whatever values you like! Remember: "As long as (condition) is true, do this. When it's no longer true, stop doing this". So you can use it however you like!
|
| This is also an extremely effective method for input validation to make sure when a Program is running, the user doesn't enter a value that you don't want them to.
|
.. code-block:: c++
   :linenos:

	char op;
	int a;
	int b;
	cout << "Enter first number: " << endl;
	cin >> a;
	cout << "Enter second number: " << endl;
	cin >> b;
	cout << "Enter operation to apply (+,-,*,/)" << endl;
	cin >> op;
	while (op != '+' && op != '-' && op != '*' && op != '/')
	{
		cout << "Invalid Entry. Please try again." << endl;
		cin >> op;
	}
	
	if (op == '+')
		cout << a << " + " << b << " is " << a + b << endl;
	else if (op == '-')
		cout << a << " - " << b << " is " << a - b << endl;
	else if (op == '*')
		cout << a << " * " << b << " is " << a * b << endl;
	else if (op == '/')
		cout << a << " / " << b << " is " << a / b << endl;

| The code above is the code for a simple calculator. You enter two numbers and an operation to apply, and then it outputs. But notice the WHILE loop and how it's used. It's gonna continue until the person enters an actual valid operator, and won't let the program go further if the value isn't something we want it to be.
|
| Make it a habit to have input validations and checks, it's good practice to do so and also makes sure inputs are only the values we want them to be.




