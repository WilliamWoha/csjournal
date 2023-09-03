.. _s1-pf-t15:

15) Conditional Statements (SWITCH and Ternary)
-----------------------------------------------

SWITCH Statements
^^^^^^^^^^^^^^^^^

| Imagine IF/ELSE Statements but another way of writing them with different features and different limits.
| That's SWITCH case. Here's the Syntax for it:


.. code-block:: c++
   :linenos:

	switch(condition)
	{
		case a:
			// Code
			break;
		case b:
			// Code
			break;
		default:
			// Code
	}

| SWITCH makes the code look very organized but also has two advantages over IF/ELSE:
*    It can save time by ``break;`` statements which reduce the code to run
*    It can fall through multiple statements
|
| So, now to explain.
| The code above is exactly the same as ``if, else if, else``.
|
*    ``switch(condition)``: Switch is the Syntax for triggering it, just like ``if``. Inside of ``condition`` you write the thing to evaluate, just like the one used in ``if``. The main difference however, is that there's no Relational Checks. You don't use ``>=, <=, >, <, ==, !=`` in Switch cases. Instead, you just write the expression.
*    ``case value:``  : This is the syntax to actually see what the ``(condition)`` turns out to be.
*    ``break;``  : This is used to stop the execution of the statement when it's done.
|
| So the way it works is, first the Program solves for ``(condition)``, and then compares the values to the ``case`` statements it has. ``case a`` means, ``condition == a?``, and if that's true then it goes into that statement and starts executing code.
| If it happens to be false then it checks ``condition == b?``, and so on.
| If it finds none of them to be true then it just goes into the ``default`` statement, which is basically just ``else``.
|
| The reason why a ``break`` statement is there is because if it's not written then the code continues to execute the lines that come afterwards.


.. code-block:: c++
   :linenos:

	case a:
		// Code 1
	case b:
		// Code 2

| Since there's no ``break`` statement, if the ``condition`` evaluates to ``a``, then it will execude all of ``Code 1``, and then, not finding a ``break`` statement, continue, and then also execute all of ``Code 2``.
| If the ``condition`` were to evaluate to ``b`` then it would only execute ``Code 2``.
|
| This can be used to one's advantage though.
|
| As for which one to use between IF and SWITCH, that's honestly your own personal preference, but IF is far more popular because it can use Logical Operators (AND, OR, NOT), and also because it's more suited to Boolean statements.


Ternary
^^^^^^^

| These are IF statements but just compressed down to only one line because somebody thought it was too much of a hassle to write multiple lines just for doing one thing.


.. code-block:: c++
   :linenos:

	if (condition)
	{
		(code)
	}
	else
		(different code)
	// That's IF statements.
	(condition) ? (code) : (different code) ;
	// That's Ternary.

| The regular IF statement took 6 lines, while the Ternary statement took only one line.
| The key difference between turning the IF itself into a less readable version, aka if(condition){code}else{different code}, is that there's still the words ``if`` and ``else`` in there. Ternary has the advantage of just replacing those with a ``?`` and an `:``, making it more readable in just one line. 
|
|
| I'll update this page with example code later but, both of those are useful when used right. IF/ELSE came before them, but there's a reason these two were invented.