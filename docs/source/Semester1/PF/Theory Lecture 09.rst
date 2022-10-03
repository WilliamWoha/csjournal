.. _s1-pft-l09:

Theory Lecture 9
----------------

| Week 5.
| Ok so to understand today's class you need to know how the Binary number system works. If you don't know how that works, look up a youtube video of it or something, you NEED to understand it. It's too much to explain here.

.. _s1-pft-t010:

Bitwise Operators
^^^^^^^^^^^^^^^^^

| These operators apply to the bits of the numbers instead of the actual values. If you know how Logic Gates work on bits, and Truth Tables, then you're already an expert on it.
*    ``&``: AND. Only 1 when both inputs are 1 (This statement is only true, if a is true AND b is true).
*    ``|``: OR. Outputs 1 when either is 1 (If a is true OR be is true, then this statement is true).
*    ``^``: XOR. Outputs 1 when inputs are different. 0 0, and 1 1, both output 0. 1 0, and 0 1, both output 1.
*    ``<<``: Left Shift. Moves all bits to the left. Data is truncated if bits exist at the very left end. Don't confuse this with the ``<<`` of ``cin``, the symbol is the same but the way you use it is different. You'll see examples later. If data isn't truncated, the effect is that the value gets multiplied by two (It's the same as moving all values in a number to the left then adding a 0 at the end. Literally the exact same thing. This is a number system after all. 452.0 vs 4520).
*    ``>>``: Right Shift. Moves all bits to the right. Data is truncated if bits exist at the very right end. Don't confuse this with the ``>>`` of ``cout``, the symbol is the same but the way you use it is different. You'll see examples later. If data isn't truncated, the effect is that the value gets divided by two (It's the same as moving all values in a number to the right then adding a 0 at the end. Literally the exact same thing. This is a number system after all. 23000 vs 02300).
*    ``~``: Bitwise Complement. Flips all bits. The formula for finding out new value, if ``a`` is the variable this is applied on, is -(a+1). This works both ways. If for example the value of ``a`` is 14, then ``~a`` would be -15. If instead the value of ``a`` is ``-15``, then the value of ``~a`` would be -(-15+1) which is -(-14) which is 14. This is a One's Complement form. If you want the actual negative value you need to actually add one to it. Look up how Two's Complement works.
| The practical applications of this are that these operations are `extremely` memory efficient compared to arithmetic operations. If you want as few variables and load on the computer as possible, this is what you use.
| You can also use it to do individual bit work and save memory instead of having to use extra space. If you want to turn the first bit of a variable ``x`` into a 1, you just do ``x = x | 1``. If you want to do the second bit, it's ``x = x | 2``, or ``x = x | (1<<1)``. Then let's say you want to do the 8th bit. That would be ``x = x | 256`` but you have to calculate that. It would be easier to just do ``x = x | (1<<7)``. It's one less than the bit you want to flip as 1 is in the starting position already. ``x = x | 1`` is actually ``x = x | (1<<0)``.
| You can check how many bits are on by doing ``x & (Max Value)`` where ``Max Value`` is just the maximum value the data type can hold. This works because any bit which is 1, would be itself if you do AND 1. If it's 0, it would be itself if you do AND 0. Doing AND 1 is the same as multiplying with 1.
| And finally, we had a Sessional and there was a question where you had to specifically `flip` a bit at a specific position. The answer to that was just ``x = x^(1<<bitposition)``. That's it.

