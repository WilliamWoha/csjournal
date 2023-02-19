.. _s1-pf-t35:

35) How Memory Works in C Programs
----------------------------------

| Every image on the internet I found was in this orientation. But our teachers explained it with this flipped, because that made sense to humans more. But it doesn't matter what orientation you understand this layout in. As long as you actually understand how it works. So let's begin.
|
.. figure:: images/memoryLayoutC.jpg
    :scale: 80%
    :alt: A Diagram showing Memory Layout in C++

| The site I borrowed this from (https://www.geeksforgeeks.org/memory-layout-of-c-program/) explained everything very well. In fact they explained it a little bit too well. You could go there and read it. I'll limit myself to only whatever I was taught in uni by my teachers, and a little bit extra if I think it's important. In our case we just learnt the names of those locations and focused specifically on the Heap and the Stack.
|
| This is CRUCIAL. Understand this. It's necessary for the entire next semester because I'm typing this right now on 19th of February 2023 and it's already been a month into OOP. There's so much emphasis on knowing this. Let's begin.
|

Text
^^^^
| The lowest addresses in Memory have Program Code and Constants. This is where the Program itself is stored. Loaded Libraries, Compiled Instructions, etc.

Initialized Data
^^^^^^^^^^^^^^^^
| This holds Static and Global Variables that have been declared with a value.

BSS (Uninitialized Data)
^^^^^^^^^^^^^^^^^^^^^^^^
| This holds Static and Global Variables that have been declared but not changed. So by default, they're set to 0 instead of some kind of Garbage Value.

Stack
^^^^^
| This is what a Recursive Function uses. And if it goes beyond the limit, then there's a Stack OverFlow. This is also where all non-dynamic, non-global, and non-static variables are declared. Without ``main()``, the program can't run. And ``main()`` is a function, and hence a part of the Stack. Pointers and Variables are both kept here, and the Stack fills up as more Variables and more Functions (and especially Recursive functions) are called.

Heap
^^^^
| The Heap handles Dynamic Memory. This is what Pointers allow you to do. Dynamic Programming. I'll explain this in detail later.

| First the program has to be compiled. Memory reservations and Syntax Errors are checked. When the program is run, meaning when Runtime is occurring, then it only *carries out* the instructions. But that doesn't apply to the Heap. In Dynamic Memory Allocation, or DMA for short, the reservation of memory is instead done at Runtime. This is how you get dynamic arrays. The Heap handles all of this, and grows upward accordingly.
|
| There's two specific Pointers to keep in mind here. One which is at the top of the Stack, and one which is at the top of the Heap. If they meet, then the computer runs out of memory. This is known as a Stack Overflow (If the Stack is expanding), or a Heap Overflow (If the Heap is expanding), and the more RAM a computer has, the more memory it can provide to both of these things.