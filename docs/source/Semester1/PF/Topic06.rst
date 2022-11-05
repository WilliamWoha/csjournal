.. _s1-pf-t06:

6) Escape Sequences, IoManip, and Comments
------------------------------------------

| Yes I know there's some syntax not written on the previous page, we'll get to it later. One thing at a time. If something isn't written it means it's gonna be explained later. All we've done for now is the main template for every C++ program, and cout statements. And believe me, even this is gonna be enough for now.
| There's these things called Escape Sequences. When you output a sentence, for example, ``cout << "Hello World!" << endl;``, then ``Hello World!`` is the output that appears in the console. If you write two lines, one below another:

.. code-block:: c++

	cout << "Hello" << endl;
	cout << "World!" << endl;

| You get the output of:

.. code-block:: c++

	Hello
	World!

| But what if we wanted to do it in only one line? That's where Escape Sequences come in.

Escape Sequences
^^^^^^^^^^^^^^^^

| Two lines had to be written so 'Hello' and 'World!' were in different lines. But there's a way to do it in only one line:

.. code-block:: c++

	cout << "Hello \n World!";

| This would output:

.. code-block:: c++

	Hello
	 World!

| I'll explain the extra space there later. The ``\n`` is the Escape Sequence. The Backslash, ``\``, is what's used to trigger it. Within any "code which is written in speech marks", if a ``\`` is written, it's not gonna be there. An Escape Sequence is used to trigger something within the text. ``\n`` will trigger a new line. ``\t`` will trigger Tab, which aligns with columns. ``\"`` is used to write speech marks where it's not possible. This happens where, if for example you want to output:
| I "love" Programming!
| You'd think it's as simple as writing ``cout << "I "love" Programming!";``, but no. the program can only work with one pair of speech marks at once. So here, the actual code to get the output above would be ``cout << "I \"love\" Programming!";``. Just like that if you also wanna output the actual backslash, you just write it twice. ``cout << "\\\\";`` would output ``\\``.
| ``\`` only reads the character in front of it. So writing "\\\\n" would in fact just output ``\n``. You'd see ``\n`` in the Console Output, this line doesn't actually mean that the Escape Sequence of ``\n`` (which is a New line) is triggered.
| An important thing to note is, Even though you're pressing two keyboard buttons for an Escape Sequence, it only counts as one character to the program. ``cout << "Hello";`` is five characters, while ``cout << "\n"`` is only one.
| Now, remember that extra space? That's because the code was ``cout << "Hello \n World!";``. There's a space between ``\n`` and ``World!`` which causes that gap to happen, as ``\n`` causes a new line, then there's a space, then there's ``World!``. The space is also a character. If you want it to be in line, the code would be ``cout << "Hello \nWorld!";``. And, though less readable for humans, ``cout << "Hello\nWorld!";`` would be the true solution.

#include <iomanip>
^^^^^^^^^^^^^^^^^^

| You remember ``#include <iostream>`` right? <iostream> is in fact a Library. A library is a set of extra features and functions. You can include more libraries too, such as <iomanip>. This is another library you should get used to. <iomanip> stands for Input/Output Manipulation. You include it in the code by writing it the same way you would write it for iostream.

.. code-block:: c++

	#include <iomanip>
	
| Do make sure you import the other libraries as well. Realistically, in a code you wouldn't write that alone. You'd write this:

.. code-block:: c++
   :linenos:

	#include <iostream>
	#include <iomanip>
	using namespace std;
	int main() {
		// code
		return 0;
	}
	
| Here's some commands to know about:
*    ``setw(num)``: Sets output in characters. If number of characters is too many, it will cut off. If number of characters is not enough, it will fill empty locations via another character (By default it will leave spaces, but the character can be changed with setfill() ). Written in format of ``cout << 30.5/6 << setw(4);``. Do note, this doesn't apply to the entire ``cout`` statement, but rather only the neighboring thing separated by ``<<``, so you can use multiple in one ``cout`` statement.
*    ``setfill('char')``: Chooses what characters to use for extra spaces, if any are left from ``setw()`` being too high.
*    ``setprecision(num)``: Chooses number of significant figures to output. Decimals are not counted. If too high of a number is entered, it will give the full number. If too low of a number is entered, such that it can't cover all decimal places, then it will use scientific notation, like 2.4e5. If the number is high enough to cover all decimal places then it will output that amount of significant figures. It will do rounding for the last number.
| All of these are written to the left of the thing they are to affect. You can remember this easily by remembering that code outputs left to right, so it has to come first. ``cout << setw(10) << setfill('*') << setprecision(6) << 34.678156`` would output:

.. code-block:: c++

    ***34.6782

Comments
^^^^^^^^

| One thing I didn't mention yet is what ``//`` means. This isn't an Escape Sequence. Escape Sequences are triggered by BackSlashes ``\``. This is a ForwardSlash ``/``. Writing two of them inside of C++ makes the program do something called a Comment.
| A Comment is text which isn't gonna be read by the machine. It's only there as a way for the person reading the code, whether they be the creator of the code or not, to be able to read it. It's kind of like sticky notes.
| You can write anything in comments, it can be as long as you want, and it has no Syntax restrictions. But remember: The program will NOT read it.
| Also, it only lasts until the next line. So if you press enter, then type code, that code will be read unless you write a pair of ``//`` again.

.. code-block:: c++
   :linenos:

	#include <iostream>
	#include <iomanip>
	using namespace std;
	int main() {
		cout << "Hello \n World!"; // \n and World! have extra space between them.
		// Output would end up being:
		// Hello
		//  World!
		// If line was instead cout << "Hello \nWorld!"; then it would be
		// Hello
		// World!
		//
		// Remember that these comments are completely useless to the program. The outputs aren't calculated. They were just written by me directly as an estimate.
		cout << "Hello \nWorld!"; // \n and World! have no extra space, so the output will be lined up.
		return 0;
	}

| You don't have to write THE ENTIRE logic of the code or entire paragraphs. Just use them like sticky notes. Use Comments to write something that would be useful to know if you were reading the code again.

Practice Exercises
^^^^^^^^^^^^^^^^^^

| Now that C++ has been introduced I can actually give you something to work with!
| 1) Write a C++ Program that outputs your Name and Date of Birth
| 2.1) Write a C++ Program to create this pyramid using slashes:

.. code-block:: c++

    	   /\\
	  /  \\
	 /    \\
	/      \\

| 2.2) Make your code from 2.1) run in only one cout statement (A very specific Escape Sequence will be used to make this possible!).
| 2.3) Make your code from 2.1) run using setw() statements (You can't use any spaces!).
|
| Answers are on :ref:`answers`.
