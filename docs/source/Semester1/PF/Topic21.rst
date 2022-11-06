.. _s1-pf-t21:

21) FOR Loops
-------------

| These are the last category of loops, but they're also my favourite. I think you'll enjoy them.
|
| The thing with FOR loops is, they exist specifically for going through numbers.
| You can make a WHILE loop run until an exact set of strings is entered (which is how password verification works) or just use counters for dealing with numbers. FOR loops let you deal with those much more easily. Here's the Syntax:


.. code-block:: c++
   :linenos:
	
	for(int i = 1; i <= 10; i++)
	{
		cout << "Hello World!" << endl;
	}

| And that code will run exactly 10 times.
| So let's talk about how it works.
|
| The main body is ``for(   ;   ;   )``, followed by a set of {curly brackets} within which the code is written. The curly brackets are the same for all loops. But the main body is different. Again, no semicolons just like WHILE loops.
| Inside the (round brackets) there's two semicolons, meaning there's three sections.
*    In the first section is declaration of a variable
*    In the second section is the condition to check (which is a similarity it has with WHILE loops)
*    In the third section it can run code which is usually used to increment or modify the variable
| The part that's most important to let the loop run is the second one. You can skip the first, or the third, or even both, but not the second. In fact, you can convert it to a WHILE loop like this.

.. code-block:: c++
   :linenos:
	
	int i = 1;
	for(; i <= 10 ;)
	{
		cout << "Hello World!" << endl;
		i++;
	}

| And voila you have a WHILE loop.

.. code-block:: c++
   :linenos:
	
	for(int i = 1; i <= 10; i++)
	{
		cout << "Hello World!" << endl;
	}

| I'm pasting this here again to explain how it works.
|
| So, the way it works is, first the main body statement is executed. A variable is declared and then the condition is checked. If the condition is true, it runs the code inside the {curly brackets}. Then when it reaches the end, it runs the code in the Third Section. In this case, that's ``i++``. It can also be ``i = i + 1`` or ``i = i + 2`` or ``i = 2 * i`` or whatever, as long as the variable being used for the condition check is actually being modified. If it's not modified, the code will still work, but it'll be a never ending loop.
| After running the code in the Third Section, it then checks the Condition in the Second section again. If it's true, it runs the loop again. It keeps going until the Condition is false, at which point it breaks the loop.