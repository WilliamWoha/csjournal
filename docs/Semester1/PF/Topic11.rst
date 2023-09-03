.. _s1-pf-t11:

11) Overflow and Underflow
--------------------------

| This one's simple to understand but it can still catch you off guard in a question.
|
| Let's declare a variable called ``a``, with this line: ``short int a;``. The range of this value would be from ``-32768`` to ``32767`` (It's one less on the positive side as 0 is also included there). Overflow happens when the value tries to store a value greater than the max range, and Underflow happens when the value is smaller than the minimum range.
| Here's what actually happens. Let's say you declare ``short int a = 32767``. In bit form this would be ``0111 1111 1111 1111``. If you add one to it, the value becomes ``1000 0000 0000 0000``, which is equal to ``-32768``. That doesn't make sense because it's actually equal to 32768 as far as the Binary System is concerned, but this is actually how Two's Complement works. If it doesn't make sense then all you have to understand is that the first bit being 0 means the number is positive, and the first bit being 1 means the number is negative. In this case, it goes from the highest positive value to the highest negative value. Adding 1 to the max value turned it into the min value. If you do it for an unsigned short int instead, it would go from ``1111 1111 1111 1111``, which is 65536, which is the max value of an unsigned short int, then add 1 to it, it becomes ``1 0000 0000 0000 0000``. But the problem is that the 1 at the very beginning is truncated as there aren't enough bits to store it. So it just becomes ``0000 0000 0000 0000``, which is the smallest value.
| Overflow means adding more to the variable than it can handle, causing it to loop around to the smallest value. Kind of like a clock.
| It doesn't just work with 1, it works with any value, as long as it's actually ASSIGNING. If you do:

.. code-block:: c++

	short int a;
	a = 32767;
	cout << a + 100 << endl;

| Then you'd get 32867 in the console. If instead you did ``a = 32867;`` and then ``cout << a << endl;``, THEN you'd get the Overflow, and the value you'd get would be -32669, which is (32767+1), which is -32768, then +99 which is -32669.
|
| Underflow is all of that just the other way around.
