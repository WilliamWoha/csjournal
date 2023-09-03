.. _s1-pf-t08:

8) MATHS Operators
------------------

| The thing is, there's actually 4 types of Operators. Arithmetic, Logical, Relational, and Bitwise. I titled this page as "Maths Operators" so it was easy to find and also because "Arithmetic" just sounds fancy but also unnecessary.
| I'll still say Arithmetic Operators for the rest of the page though.
| 
| Logical and Relational Operators will be done with :ref:`s1-pf-t12`.

Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^

| These just apply to numbers. They are:
*    ``+``: Plus Sign (Addition)
*    ``-``: Minus Sign (Subtraction)
*    ``*``: Asterisk (Multiplication)
*    ``/``: Forward Slash (Division)
*    ``%``: Percentage Sign (Modulus)
| You know the first four already so I'm not gonna bother with them. The one thing you should know is, for division, there's no rounding. The data is just lost. If you do ``5 / 5`` you get 1 but if you do ``4 / 5`` or ``3 / 5`` or something where the decimal answer would be less then 1, your result is gonna be 0. This is different if you did ``4.0 / 5`` as then one of the values is float, and it's not a pure integer division. Then you get an answer in a float (meaning in decimal) instead of a 0.
| Modulus, or MOD for short, is the new one. The simple explanation is:
| ``18 / 7`` is 2 with a remainder of 4. Ignore decimals for now. If you did ``int a;`` and then ``a = 18 / 7;``, the value of ``a`` would be 2. The rest of the data would be lost since it's an ``int`` data type. If you did ``a = 18 % 7;``, the value of ``a`` would be 4. The MOD operator keeps only the remainder.
| Other examples:
*    118 % 25 is 18.
*    15 % 10 is 5.
*    16 % 2 is 0.
*    17 % 2 is 1.
*    50 % 100 is 50.

| This can be useful in a number of ways. For example, doing any number MOD 2 would either give 0 or 1. If it's 0 then it's even and if it's 1 then it's odd.
| MOD can apply only on two integers. Not on more than that.
| If ``x`` and ``y`` are two integers and you're doing ``x % y``, but ``x`` and ``y`` can both be either positive or negative, then the result of ``x % y`` will have the sign of ``x``. If ``x`` is negative, the result will be negative, regardless of if ``y`` is negative or positive.
| You can use MOD for digit separation too. Here's how it works:
*    We have a number, ``3452``.
*    ``3452 / 1`` is 3452. ``3452 % 10`` is 2.
*    ``3452 / 10`` is 345.2, but since it's integer division, data is lost, and we get 345. ``345 % 10`` is 5.
*    ``3452 / 100`` is 34.52, but since it's integer division, data is lost, and we get 34. ``34 % 10`` is 4.
*    ``3452 / 1000`` is 3.452, but since it's integer division, data is lost, and we get 3. ``3 % 10`` is 3.
| In the first line, we get 2. In the second, 5. In the third, 4. In the fourth, 3. These results are the individual numbers that make up the entire number: 3452.

Precedence
^^^^^^^^^^

| What if multiple arithmetic operators are used in one statement? It has to follow an order. So here it is:
*    ``( )``
*    ``/ , % , *``: If in same line, left to right
*    ``+ , -``: If in same line, left to right
| So ``(3 + 2) * 6`` would give 30 and ``3 + 2 * 6`` would give 15
| ``6 * 4 + 3 - 2 / 5`` would give 27 (as 2 / 5 would be 0 because of integer division)

Type Coercion (Type Casting)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Coercion means conversion. You can convert between data types. There's multiple ways to do so. It either falls under Type Promotion or Type Demotion.

.. code-block:: c++

	float a = 3.2;
	int b = 10;

| ``(a / b)``, ``(b / a)``, ``(a * b)``, ``(a + b)``, and ``(a - b)`` would all give an output in float form. All of them "Promote" the int to a float then do an operation on it (MOD won't work, MOD needs two integers). The compiler does it automatically, you don't have to do it. This is what we call Automatic Type Coercion.
| Data Type Ranking determines whether the conversion is promoting or demoting. It goes as follows: Long Double, Double, Float, Unsigned Long Long Int, Long Long Int, Long Int, Unsigned Int, Int. So in simple terms, Double, then Float, then Int, with Int being lowest rank and Double being the highest rank. I haven't explained Long and Unsigned yet but all you need to know is that they're different variations of existing Data Types. Long just means "takes up more memory for increasing range" (which is why Int ranges till 2 billion and Long Int ranges till 9 quintillion which is 9 followed by 18 zeroes), and Unsigned just means "only positive". You don't have to memorize these specifics and this order. The order is just Double > Float > Int. All you have to understand is, if an operation uses different Data Types, then it will promote the numbers to the highest rank to do the calculation. That's why 4/5 gives 0 (as they're both integers) but 4.0/5 gives 0.8 (as 4.0 is a float, the 5 is promoted and the calculation is done to give a Float as a result).

.. code-block:: c++

	int answer = a * b;

| ``a`` is float, and ``b`` is int. ``b`` gets promoted to float, and then the math operation is done. ``a * b`` is calculated. This is then saved to ``answer``, but the value gets demoted into ``int`` as the declaration of ``answer`` was in ``int``. Decimal Place values are cut off.
| 
| To do the conversion manually, there's two ways:
*    ``static_cast<data type>(value)``: Static Cast. In ``<data type>`` you write the data type you want to convert to, such as ``float``. In ``value``, you write the variable name or the direct value you want to convert.
*    ``type(value)`` or ``(type)value``: Write the data type in ``type``, and the variable name or direct value you want to convert in ``value``.
| If you do ``float(7/10)`` the result would be 0. If you instead do ``float(7)/10`` then you get 0.7. It solves in the brackets first so make sure you're converting BEFORE the division.
| The same logic applies to ``(float)7/10`` and ``static_cast<float>(7)/10``.

Practice Exercises
^^^^^^^^^^^^^^^^^^

| I don't really have a Practice thing to give since this is just dependent on Maths, though if I think of any I'll write them.
| Instead, you can have this, which is a brain teaser for the next concept:

.. code-block:: c++
   :linenos:
	
	int a;
	cout << "Enter number: " << endl;
	cin >> a;
	cout << "The number you entered is: " << a << endl;
	a = 6;
	cout << "The value has been changed to: " << a << endl;
	cout << "The double of the value is: " << a+6 << endl;
	cout << "The half of the value is: " << a-3 << endl;
	cout << "The value is: " << a << endl;

| Read that code above, see if it makes sense. I want you to try and guess the output for Line #9.
| Would it be "The value is: 9"?
| Or would it be "The value is: 6"?
|
| If you're confused by what the question is, then it's just this: Will the value of ``a`` change with the cout statements used after it?
|
| Write the answer on a pen and paper then move on to the next page to see if you were right!




