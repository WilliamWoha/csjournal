.. _s1-pf-t12:

12) Conditional Statements (IF/ELSE)
------------------------------------

IF/ELSE
^^^^^^^

| At last we come to the HOLY GRAIL.
| Ok so the easiest way to understand it is, "If this happens then do this, otherwise do this". That's literally it. You just have to write that in code form.
| The key to understand this is Relational Operators and Logical Operators (You were probably wondering when we'd get to those huh?).
|
| Here's Relational Operators:
*    ``>=``: Greater than or equal to
*    ``<=``: Less than or equal to
*    ``>``: Greater than
*    ``<``: Less than
*    ``==``: Equal to
*    ``!=``: Not Equal to
| And now here's some Logical Operators:
*    ``&&``: AND
*    ``||``: OR
*    ``!``: NOT
|
| I'll explain later how all of those work. All you need to know is, IF statements work on TRUTHs. Absolute truths. If you tell it something that's wrong, it won't do it.
| Here's how the syntax works.

.. code-block:: c++
   :linenos:
   
	if (condition) {
		(code)
		(more code)
	}

| It can also be written as:

.. code-block:: c++
   :linenos:

	if (condition)
	{
		(code)
		(more code)
	}

| There's no actual semicolon to write for the ``if`` statement itself. Just for the lines between it which are regular code. The brackets around ``condition`` are NECESSARY. No matter how big the statement is, there has to be one set of brackets holding it all together.
| The indentation (which means the gap for the code between the if statement) isn't necessary but is highly recommended for making code readable. It's just good practice to do.
| Then there's ELSE statements. Which mean, if the original IF condition isn't filled, then execute this code. "If this happens then do this, OTHERWISE do this". The ELSE statement is just the otherwise part of that sentence. And else just means the opposite of the if statement. You don't write a condition for it.

.. code-block:: c++
   :linenos:

	if (condition)
	{
		(code)
		(more code)
	}
	else
	{
		(code)
		(more code)
	}

| Here's an example:

.. code-block:: c++
   :linenos:

	if (num % 2 == 0)
	{
		cout << "The number is an even number." << endl;
	}
	else
	{
		cout << "The number is an odd number." << endl;
	}

| So, the way the IF statement works is, whatever is written in the ``(condition)`` in front of the IF statement, it checks it. If it's true, it will do whatever comes within the ``{curly brackets}`` that follow it.
| If however, that situation is NOT true, then it will instead do what's in the ``{curly brackets}`` that come after ELSE.
|
| You can write IF statements without any ELSE statements but not the other way around.
|
| The reason that the Equals comparison sign is ``==`` and not ``=`` is because ``=`` is used for ASSIGNING. So if you just did one equals sign in an IF statement it would give an error. And in some cases, it doesn't even do that. I've had too many headaches with finding out that I was missing a second Equals sign but it wasn't an error because a Boolean was being used. So be very VERY careful with this.
|
| Here's something new. Let's say you have a statement called ``int n = 0;``
| Then you make an if statement of ``if (n)``. Would that statement trigger? Nope. But that's not because of the lack of comparison, it's just because n is 0. If you instead did ``int n = 1;`` or ``int n = 5;`` or ``int n = -3``, and then did ``if (n)``, then that statement would in fact trigger, because it's just checking that it's not 0. ``if (n)`` is the same as writing ``if (n != 0)``. ``if (!0)`` would also be true.
|
| The way Logical Operators (such as AND, OR, and NOT, or rather, &&, ||, and !) work, is that they check the absolute truths with logic. They work together with the Relational Operators for making the code easier.
|
| Let's say you wanted an IF statement to run if someone pressed Y, but you don't know if they pressed ``Y`` or ``y``. You can just put both into the IF statement.

.. code-block:: c++
   :linenos:

	if (button == 'Y' || button == 'y') // This translates to: If button equals 'y' or if button equals 'Y'
	{
		// Code
	}

|
| A bit more practice is required to understand the Logical Operators if you don't already. I'll try to find resources and questions for more practice.
|
| One more thing to know about this (and I'm typing this now AFTER my exams. I didn't know it before) is that there's a priority for these operators and you need to know which one is carried out when.
| The highest to lowest priority goes as such:
*    Arithmetic Operators ``( + - / * % )``
*    Bitwise Shift Operators ``( << >> )``
*    Relational Operators ``( > >= < <= )``
*    Equality Operators ``( == != )``
*    Bitwise AND Operator ``( & )``
*    Bitwise XOR Operator ``( ^ )``
*    Bitwise OR Operator ``( | )``
*    Logical AND Operator ``( && )``
*    Logical OR Operator ``( || )``
| Yeah so I made the mistake of not knowing that the Logical AND is above the Logical OR, so in a question that asked ``A || B && C`` I assumed it was going left to right. In reality it first checks ``B && C`` then does ``||`` with ``A`` after that.
| A, B, and C are all just brackets with their own operations going on inside of them. Don't worry about it.