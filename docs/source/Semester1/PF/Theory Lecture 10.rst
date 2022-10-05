.. _s1-pft-l10:

Theory Lecture 10
-----------------

| Week 5.
| Here's the syllabus of the Sessionals:
*    Data Types (Typecasting, Overflow/Underflow)
*    Variables and Constants
*    ``<cmath>`` functions
*    Operators (Bitwise, Arithmetic, Logical, Relational)
*    IF/ELSE
| Actually at the time of writing this we just finished the Sessionals 5 days ago (October 2nd, 2022, Sunday 8:15AM). We get the results tomorrow, I'll write any extra info or questions or whatever can help. We have another Sessional on Tuesday (October 4th, 2022) and I have no idea how that's gonna go. Best advice I can give for now is, practice your typing.

.. _s1-pft-t011:

Overflow and Underflow
^^^^^^^^^^^^^^^^^^^^^^

| Let's declare a variable called ``a``, with this line: ``short int a;``. The range of this value would be from ``-32768`` to ``32767`` (It's one less on the positive side as 0 is also included there). Overflow happens when the value tries to store a value greater than the max range, and Underflow happens when the value is smaller than the minimum range.
| Here's what actually happens. Let's say you declare ``short int a = 32767``. In bit form this would be ``0111 1111 1111 1111``. If you add one to it, the value becomes ``1000 0000 0000 0000``, which is equal to ``-32768``. Adding 1 to the max value turned it into the min value. If you do it for an unsigned short int instead, it would go from ``1111 1111 1111 1111``, which is 65536, which is the max value of an unsigned short int, then add 1 to it, it becomes ``1 0000 0000 0000 0000``. But the problem is that the 1 at the very beginning is truncated as there aren't enough bits to store it. So it just becomes ``0000 0000 0000 0000``, which is the smallest value.
| Overflow means adding more to the variable than it can handle, causing it to loop around to the smallest value. Kind of like a clock.
| It doesn't just work with 1, it works with any value, as long as it's actually ASSIGNING. If you do:

.. code-block:: c++
	short int a;
	a = 32767;
	cout << a + 100 << endl;

| Then you'd get 32867 in the console. If instead you did ``a = 32867;`` and then ``cout << a << endl;``, THEN you'd get the Overflow, and the value you'd get would be -32669, which is (32767+1), which is -32768, then +99 which is -32669.
|
| Underflow is all of that just the other way around.

.. _s1-pft-t012:

IF/ELSE
^^^^^^^

| At last we come to the HOLY GRAIL.
| Ok so the easiest way to understand it is, "If this happens then do this, otherwise do this". That's literally it. You just have to write that in code form.
| The key to understand this is Relational Operators and Logical Operators (You were probably wondering when we'd get to those huh?).
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

| The reason that the Equals comparison sign is ``==`` and not ``=`` is because ``=`` is used for ASSIGNING. So if you just did one equals sign in an IF statement it would give an error.
|
| Here's something new. Let's say you have a statement called ``int n = 0;``
| Then you make an if statement of ``if (n)``. Would that statement trigger? Nope. But that's not because of the lack of comparison, it's just because n is 0. If you instead did ``int n = 1;`` or ``int n = 5;`` or ``int n = -3``, and then did ``if (n)``, then that statement would in fact trigger, because it's just checking that it's not 0. ``if (n)`` is the same as writing ``if (n != 0)``. ``if (!0)`` would also be true.
|
| One more thing to know about this (and I'm typing this now AFTER the sessionals. I didn't know it before) is that there's a priority for these operators and you need to know which one is carried out when.
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

