.. _s1-pfl-l03:

Lab Lecture 03
--------------

| Week 3.
| Now you actually learn how to make the C++ program via the Compiler in Ubuntu. Navigate to the directory where it's stored in the Terminal, then to compile it (and it's important that this is in order. Remember this line, you're gonna use it a lot) write:

.. code-block::
	g++ -o name2 name.cpp

| Where ``name.cpp`` is your C++ compiled file, and name2 is the name of the Compiled Program. There's no file type associated to it (Don't worry about it for now). This command just generates a file called ``name2`` in the same directory, and this is the comiled program. To run said program, in the Terminal you just write ``./name2`` (NOT ``./name2.cpp``). Make sure you're still in the same directory or else it won't work.
| If the compilation was successful and these instructions were done correctly, your program should now run in the terminal.
| Memorize these steps. You have to do them EVERY TIME you wanna test the code. First Save it in the text editor (aka in the ``.cpp`` file), then run the command to compile, then execute.
