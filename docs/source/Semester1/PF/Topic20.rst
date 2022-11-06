.. _s1-pf-t20:

20) DO WHILE Loops
------------------

| This one's simple. Incredibly simple.
|
| It's just WHILE but written in a different way. It's also the first (and possibly only) situation where you'd use a semicolon with some kind of Selection or Loop structure.
|
.. code-block:: c++
   :linenos:
   :emphasize-lines: 2,8
	
	int counter = 0;
	while (counter < 10)
	{
		cout << "Hello World!" << endl;
		counter++;
	}
	
	if (counter == 10)
	{
		cout << "Loop complete." << endl;
	}

| That above is some sample code, don't focus on what it does. Instead, look at the statements for ``if`` and ``while``. They're highlighted.
| Notice the lack of any semicolons throughout those structures? There's just a set of (round brackets) for the condition check and a set of {curly brackets} for running the code if the condition is true.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 2,8
	
	int counter = 0;
	while (counter < 10);
	{
		cout << "Hello World!" << endl;
		counter++;
	}
	
	if (counter == 10);
	{
		cout << "Loop complete." << endl;
	}

| Here's the same code but with semicolons in front of the condition. Guess what happens.
|
| I don't know what you guessed, but if it was something along the lines of the code block inside the {curly brackets} not executing, then you're right!
| It associates that semicolon with the WHILE and IF statements, and considers that to be the entire block of code, completely skipping the actual code in the {curly brackets}. The same happens if the semicolon was put at the end of the {curly brackets};
|
| It might act differently depending on the compiler but, you avoid semicolons in these scenarios. It's not only discouraged, it's straight up just banned. Except for this scenario with DO/WHILE.
|
.. code-block:: c++
   :linenos:
	
	do 
	{
		// Code
	} 
	while (condition);
	//
	// Can also be written as
	//
	do 
	{
		// Code
	} while (condition);
	//
	// Or
	//
	do {
		// Code
	} while (condition);

| The way it works is **exactly** like a WHILE loop. Not even joking, that's why there's a ``while (condition)`` written at the end there. It works on the same principle.
| The only difference is, it will execute the code *at least* once, even if the condition was never even initially true.
| It can be good to prevent repetition. For example:

.. code-block:: c++
   :linenos:
	
	int num = 0;
	cout << "Enter a number between 1 and 10: " << endl;
	cin >> num;
	while (num < 1 || num > 10)
	{
		cout << "Invalid Entry. Please try again: " << endl;
		cin >> num;
	}

| That's a sample of using a WHILE loop.
| If the original entry is valid, then the loop is skipped entirely as the condition check fails.
| Here's how to do it with a DO/WHILE loop:


.. code-block:: c++
   :linenos:

	int num = 0;
	do {
		cout << "Enter a number between 1 and 10: " << endl;
		cin >> num;
	} while (num < 1 || num > 10);

| It took way less lines and it's basically the same thing. It prevents repetition.
| You don't *have* to use it if you don't want to, but it's still good to know about. Ultimately it's up to you for which one you want to use. But remember that even if the condition was never true to begin with, like for the code above if the entered number was between 1 and 10, then the code will still run *at least* once.
