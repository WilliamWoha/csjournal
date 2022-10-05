.. _s1-pft-extra1:

Things I wish I knew earlier
----------------------------

*    Practice typing speed. You will have a massive advantage which you'll need if you want to stay ahead in programming. If you're able to type without looking at the keyboard, then you're set.
*    For the first Sessionals, the other logic statements are easy to understand, but BITWISE requires a lot of practice. It may be easy to understand but there's a lot of situations that require you to think outside the box. Look up exercises and things you can do with BITWISE functions. Here's what we were asked in our first exams:
    *    Add two numbers using only BITWISE functions, without the use of IF statements and without the use of LOOPS
    *    Turn all bits to the right of the most significant bit into 1
    *    Find most significant bit of a number
    *    Turn all consecutive bits at the end of a number into 0's
    *    Input a position then flip a bit at that specific position
*    How to do the MOD function without Modulus:

.. code-block:: c++
   
   int a, b, c, d; // This many are unnecessary. This is just for explanation.
	a = 17 % 3;
   
   b = 17 / 3;
   c = b * 3;
   d = 17 - c;
   
    | At the end of this, the value of a will be the same as the value of d. To write the Modulus without MOD in one line:

.. code-block:: c++

	d = 17-((17/3)*3)
   
    | The way it works is that ``17/3`` is integer division, so it gets rid of any decimal values. The answer is 5.something but that's deleted so, it's 5. That's the key here. The extra part is deleted.
    | If you then multiplied that by the numerator, the expression would be ``5 * 3``, which is 15. It's not the original value of 17, but rather it's the closest whole number value.
    | Then you subtract it from the original value. That's ``17 - 15``. The result is 2, which is the remainder of the expression ``17 / 3``.
    | You can read through the steps again if confused. This ONLY WORKS because the integer data type doesn't store original values.

| I've written general notes and stuff in the :ref:`semester1` section.
