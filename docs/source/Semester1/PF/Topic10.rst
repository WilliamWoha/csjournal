.. _s1-pf-t10:

10) BITWISE Operators
---------------------

| Ok so to understand today's class you need to know how the Binary number system works. If you don't know how that works, go back to :ref:`s1-pf-t01` and :ref:`s1-pf-t02`, you NEED to understand it. It's too much to explain here.

| These operators apply to the bits of the numbers instead of the actual values. If you know how Logic Gates work on bits, and Truth Tables, then you're already an expert on it.
*    ``&``: AND. Only 1 when both inputs are 1 (This statement is only true, if a is true AND b is true).
*    ``|``: OR. Outputs 1 when either is 1 (If a is true OR be is true, then this statement is true).
*    ``^``: XOR. Outputs 1 when inputs are different. 0 0, and 1 1, both output 0. 1 0, and 0 1, both output 1.
*    ``<<``: Left Shift. Moves all bits to the left. Data is truncated if bits exist at the very left end. Don't confuse this with the ``<<`` of ``cin``, the symbol is the same but the way you use it is different. You'll see examples later. If data isn't truncated, the effect is that the value gets multiplied by two (It's the same as moving all values in a number to the left then adding a 0 at the end. Literally the exact same thing. This is a number system after all. 452.0 vs 4520).
*    ``>>``: Right Shift. Moves all bits to the right. Data is truncated if bits exist at the very right end. Don't confuse this with the ``>>`` of ``cout``, the symbol is the same but the way you use it is different. You'll see examples later. If data isn't truncated, the effect is that the value gets divided by two (It's the same as moving all values in a number to the right then adding a 0 at the end. Literally the exact same thing. This is a number system after all. 23000 vs 02300).
*    ``~``: Bitwise Complement. Flips all bits. The formula for finding out new value, if ``a`` is the variable this is applied on, is -(a+1). This works both ways. If for example the value of ``a`` is 14, then ``~a`` would be -15. If instead the value of ``a`` is ``-15``, then the value of ``~a`` would be -(-15+1) which is -(-14) which is 14. This is a One's Complement form. If you want the actual negative value you need to actually add one to it. Look up how Two's Complement works.
|
| The practical applications of this are that these operations are `extremely` powerful memory efficient compared to arithmetic operations. If you want as few variables and load on the computer as possible, this is what you use.
| You can also use it to do individual bit work and save memory instead of having to use extra space. If you want to turn the first bit of a variable ``x`` into a 1, you just do ``x = x | 1``. If you want to do the second bit, it's ``x = x | 2``, or ``x = x | (1 << 1)``. Then let's say you want to do the 8th bit. That would be ``x = x | 256`` but you have to calculate that. It would be easier to just do ``x = x | (1 << 7)``. It's one less than the bit you want to flip as 1 is in the starting position already. ``x = x | 1`` is actually ``x = x | (1 << 0)``.

Practice Exercises
^^^^^^^^^^^^^^^^^^

| These ones are gonna feel brutal, but that's what our university put us through. The class average was something like an overall 40% score.
| And BITWISE is an *extremely* powerful tool. I was angry because it felt pointless and felt that modern computers were fast enough, but no, it can be so much faster. In `This YouTube Video <https://www.youtube.com/watch?v=c33AZBnRHks>`_, someone made a Python code which took 31 days to run. Another viewer of his cut that down to 15 minutes. And then more viewers kept reducing the time more and more, until it was down to 6.1 milliseconds, which is 0.0061 seconds. The record before this was of 470 milliseconds, which is 0.470 seconds. And it was done, with BITWISE.
|
| Not gonna tell you to do that, it's gonna take like forever to do it. But BITWISE has power. So here's your tasks. You can look them up on the internet if you want help but it's better if you try a pen and paper, use the Binary system, and see what you can do to solve it on your own.
|
*    Add two numbers using only BITWISE functions, without the use of IF statements and without the use of LOOPS
*    Turn all bits to the right of the most significant bit into 1
*    Find most significant bit of a number
*    Turn all consecutive bits at the end of a number into 0's
*    Input a position then flip a bit at that specific position
|
| There's more on the internet too. Just look them up and practice. If you master Bitwise, you can master anything, because this is one of the most difficult things to work with, but also one of the most powerful.