.. _s1-pft-l07:

Theory Lecture 07
-----------------

| Week 4.
| So there's these things called Operators. There's four categories of them. Arithmetic, Logical, Relational, and Bitwise. Lets start with the easy one.

.. _s1-t005:

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
| ``18 / 7`` is 2 with a remainder of 4. Ignore decimals for now. If you did ``int a;`` and then ``a = 18/7;``, the value of ``a`` would be 2. The rest of the data would be lost since it's an ``int`` data type. If you did ``a = 18%7;``, the value of ``a`` would be 4. The MOD operator keeps only the remainder.
| This can be useful in a number of ways. For example, doing any number MOD 2 would either give 0 or 1. If it's 0 then it's even and if it's 1 then it's odd.
| MOD can apply only on two integers. Not on more than that.
| If ``x`` and ``y`` are two integers and you're doing ``x%y``, but ``x`` and ``y`` can both be either positive or negative, then the result of ``x%y`` will have the sign of ``x``. If ``x`` is negative, the result will be negative, regardless of if ``y`` is negative or positive.
| You can use MOD for digit separation too. Here's how it works:
*    We have a number, ``3451``.
*    ``3452 % 10`` is 2.
*    ``3452 % 100`` is 52. ``52 / 10`` is 5.2 but since it's an integer, data is lost, and we get 5.
*    ``3452 % 1000`` is 452. ``452 / 100`` is 4.52 but since it's an integer, data is lost, and we get 4.
*    ``3452 % 10000`` is 3452. ``3452 / 1000`` is 3.452 but since it's an integer, data is lost, and we get 3.
| In the first line, we get 2. In the second, 5. In the third, 4. In the fourth, 3. These results are the individual numbers that make up the entire number.

.. _s1-t006:

Precedence
^^^^^^^^^^

| What if multiple arithmetic operators are used in one statement? It has to follow an order. So here it is:
*    ``( )``
*    ``/ , % , *``: If in same line, left to right
*    ``+ , -``: If in same line, left to right
| So ``(3+2)*6`` would give 30 and ``3+2*6`` would give 15
| ``6*4+3-2/5`` would give 32 (as 2/5 would be 0)

.. _s1-t007:

Type Coercion (Type Casting)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Coercion means conversion. You can convert between data types. There's multiple ways to do so. It either falls under Type Promotion or Type Demotion.

.. code-block:: c++
	float a = 3.2;
	int b = 10;

| ``(a / b)``, ``(b / a)``, ``(a * b)``, ``(a + b)``, and ``(a - b)`` would all give an output in float form. All of them "Promote" the int to a float then do an operation on it (MOD won't work, MOD needs two integers). The compiler does it automatically, you don't have to do it. This is what we call Automatic Type Coercion.
| Data Type Ranking determines whether the conversion is promoting or demoting. It goes as follows: Long Double, Double, Float, Unsigned Long Long Int, Long Long Int, Long Int, Unsigned Int, Int. So in simple terms, Double, then Float, then Int, with Int being lowest rank and Double being the highest rank.

.. code-block:: c++
	int answer = a*b;

| ``a`` is float, and ``b`` is int. ``b`` gets promoted to float, and then the math operation is done. ``a * b`` is calculated. This is then saved to ``answer``, but the value gets demoted into ``int`` as the declaration of ``answer`` was in ``int``. Decimal Place values are truncated.
| 
| To do the conversion manually, there's two ways:
*    ``static_cast<data type>(value)``: Static Cast. In ``<data type>`` you write the data type you want to convert to, such as ``float``. In ``value``, you write the variable name or the direct value you want to convert.
*    ``type(value)`` or ``(type)value``: Write the data type in ``type``, and the variable name or direct value you want to convert in ``value``.
| If you do ``float(7/10)`` the result would be 0. If you instead do ``float(7)/10`` then you get 0.7. It solves in the brackets first so make sure you're converting BEFORE the division.
| The same logic applies to ``(float)7/10`` and ``static_cast<float>(7)/10``.

