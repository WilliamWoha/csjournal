.. _s1-pf-intro:

Semester 1: Programming Fundamentals
====================================

On the right side of the page you'll find a table of sorts that, upon clicking any of the text there, will take you to that section of the page. The page is very long, it has the notes of the ENTIRE SEMESTER. Further organizing it wasn't possible, that's why it's like this.
If you're after a specific topic then just press Ctrl-F (or if in browser, then 'Find in Page') to search for it.

I don't want FAST to come after me and try to take this thing down so, none of their material will be uploaded here. I can however reference info from it, and upload and link files that don't belong to them.

Programming Fundamenttals has 4 Total Credit Hours. 3 for Theory, and 1 for Lab. That means for 16 weeks, there will be 3 hours a week for Theory and 1 hour a week for Lab. Yes, we do three hours but that's beside the point. Credit Hours are counted weirdly.

Outline for PF Theory:

*    4 Assignments. Total Absolutes: 12
*    1 Sessional-I. Total Absolutes: 10 
*    1 Sessional-II. Total Absolutes: 15
*    4 or more Quzzes. Total Absolutes: 10
*    1 Project. Total Absolutes: 13
*    1 Final Exam. Total Absolutes: 40

Outline for PF Lab:

*    14 or more Lab Tasks. Total Absolutes: 30
*    1 Sessional-I. Total Absolutes: 8
*    1 Sessional-II. Total Absolutes: 12
*    1 Project. Total Absolutes: 10
*    1 Final Exam. Total Absolutes: 40

Grading Polcy is Absolute Grading.

Textbooks:

*    Starting Out with C++: From Control Structures through Objects; Ninth Edition by Tony Gaddis
*    Starting Out with Programming, Logic, and Design; Third Edition by Tony Gaddis
*    Starting Out with C++; 8th Edition by Tony Gaddis

Software:

*    Ubuntu, version 20.04, installed via Dual Boot or Virtual Machine (They say it's not allowed but honestly a VM is better for most cases. It works perfectly fine and I use it. It's far far less of a hassle to install and takes less space)
*    G++ Compiler Suite in Ubuntu
*    Text Editor (Preferably GEdit) in Ubuntu

.. _s1-pft-l01:

Theory Lecture 01
-----------------

Week 1.

The most relaxing class. We did introductions, learnt about the course, what absolutes are, what GCR to join, which books and software we need, and were also warned about how difficult it was gonna be but took it lightly. Don't make our mistake, young reader, this institution will break you unless you're prepared. At the time of writing this (1st October 2022), it already broke my colleagues. In the first Sessional of Calculus, the total marks were 60. Our class average was 24/60. The Highest in Section A was 36 and in Section C was 40. You must be ready.

.. _s1-pfl-l01:

Lab Lecture 01
--------------

Week 1.

It was a lot of people there and a lot of noise but pay attention as EVERY SINGLE LAB CLASS for PF Lab is graded. You'll need a laptop or computer already. If you don't have one then you'll have to stay extra hours at FAST so you can use their labs. That might affect your situation with transport, but they don't care. You either do it or you don't get a grade. If you need a good machine for little cost, then get an old laptop and put an SSD in there.

You learn Ubuntu in this class. The Terminal is the thing that you'll use the most. The commands to remember are:

*    ``mkdir name``: Makes new folder in current directory with name of ``name``
*    ``touch name.ext``: Makes new file in current directory with name of ``name`` and extension ``.ext``
*    ``cd name``: Changes Directory to folder ``name``
*    ``cd ..``: Moves up one directory
*    ``cd``: Moves to root directory
*    ``ls``: Shows all files in directory
*    ``ls -l``: Shows all files in directory in detailed manner with read, write, and execute permissions.

Get used to them. You'll be using them a lot.

.. _s1-pft-l02:

Theory Lecture 02
-----------------

Week 1.
A lot of background information on what Fundamentals means and what Programming means, and then finally, Programming Fundamentals. Computer Organization is also important and then there was the history of Von-Neumann.

There are three types of languages:

*    Machine Language: Only language machine actually understands. This is the 0's and 1's you see. Very cumbersome for humans but ALL languages are deconstructed to this level via something that translates them for the computer.
*    Assembly Language: 1's and 0's with letters. It's very very close to Machine Language but is readable by humans. You can program in it but it will test your patience like no other. But hey, Chris Sawyer got 30 Million Dollars for it since he made a game called RollerCoaster Tycoon. So if you have the guts, then go for it. The translator for Assembly Language is called the Instructor.
*    High Level Language: Way closer to Human Language. Uses Common Math operations, and converted either in real time with Interpretors, or after compiling all at once with Compilers. C++ is a Compiled language. Compiler languages are much faster than Interpreted languages but troubleshooting can be a massive hassle as, if one part of the code doesn't work, the entire thing drops.

.. _s1-pft-l03:

Theory Lecture 03
-----------------

Week 2.

Logic and Problem Solving. It explained about flowcharts and pseudocode, and why they're used. Pseudocode is widely used as it is easy to read, has no strict syntax, and lets the Programmer focus on the logic first. That's literally it, it just explained those three things again. If you know them, great. Othewrise, just google them. I'm not explaining here.

.. _s1-pfl-l02:

Lab Lecture 02
--------------

Week 2.

More about Problem Solving with Algorithms and Flowcharts. Then we made some flowcharts and did a Scratch assignment.

.. _s1-pft-l04:

Theory Lecture 04
-----------------

Week 2.

Now we're doing the good stuff. Welcome to C++.

.. _s1-pft-t001:

Intro to C++
^^^^^^^^^^^^

History: It has a lot. But this doesn't matter in your exams.

Syntax: This is THE MOST important thing to remember. It's crucial that you memorize this as you'll lose marks if you miss a single detail.
    | ``#include <iostream>``
    | ``using namespace std;``
    | ``int main() {``
        |
        | ``(code)``
        |
        | ``return 0;``
    | ``}``

Now you're probably wondering what all of that is. So lets get to work:

*    ``#include <iostream>`` is called a 'Preprocessor Directive'. It's written at the top and basically prepares the rest of the program for these commands. #include means, that specific library has to be included.
*    ``using namespace std;`` means using names for objects and variables from the standard library. Don't focus on what it does for now, just know that you have to write it.
*    ``int main()`` is a Function. You'll learn Functions in OOP but for now just understand that, ALL of your code that you write, is to be written inside of this. If written outside or if you don't mention this line, it WILL NOT work. It has to be written between the {curly brackets}.
*    ``return 0`` is also a part of the Function. Just know that you have to write it at the absolute very end for now. This isn't always important, as the program works completely fine without it, but I've lost marks on quizzes for forgetting to write it so, it's better if you do.
There's still more stuff to actually cover, but that above is just the template. MAKE SURE to memorize it, you will need it for the rest of the semester.
Other Syntax that you'll use for Program Execution:
*    ``cout``: Used to output to the Console. Written in format of ``cout << "Hello World!";``
*    ``endl``: Written at the end of a cout statement so that anything that comes after is done in a new line. Written in format of ``cout << "Hello World!" << endl;``
Do make sure to write a semicolon at the end of every single thing you write. The only time you don't, is for # lines, and after the ``}`` which is found below ``return 0;``.

.. _s1-pft-l05:

Theory Lecture 05
-----------------

Week 3.

Yes I know there's some syntax not written in the above section, we'll get to it later. One thing at a time. If something isn't written it means the university will explain it later. And right now we've just done the main template for every C++ program, and cout statements. And believe me, even this is gonna be enough for now.
There's these things called Escape Sequences. When you output a string, for example, ``cout << "Hello World!" << endl;``, then ``Hello World!`` is the output that appears in the console. If you write two lines, one below another:

``cout << "Hello" << endl;``

``cout << "World!" << endl;``

You get the output of:

Hello

World!

But what if we wanted to do it in only one line? That's where Escape Sequences come in.

.. _s1-pft-t002:

Escape Sequences
^^^^^^^^^^^^^^^^

Two lines had to be written so 'Hello' and 'World!' were in different lines. But there's a way to do it in only one line:

``cout << "Hello \n World!";``

This would output:

Hello

 World!

I'll explain the extra space there later. The ``\n`` is the Escape Sequence. The Backslash, ``\``, is what's used to trigger it. Within any "code which is written in speech marks", if a ``\`` is written, it's not gonna be there. An Escape Sequence is used to trigger something within the text. ``\n`` will trigger a new line. ``\t`` will trigger Tab, which aligns with columns. ``\"`` is used to write speech marks where it's not possible. This happens where, if for example you want to output:

I "love" Programming!

You'd think it's as simple as writing ``cout << "I "love" Programming!";``, but no. the program can only work with one pair of speech marks at once. So here, the actual code to get the output above, would be ``cout << "I \"love\" Programming!";``. Just like that if you also wanna output the actual backslash, you just write it twice. ``cout << "\\\\";`` would output ``\\``.

``\`` only reads the character in front of it. So writing "\\\\n" would in fact just output ``\n``.

An important thing to note is, Even though you're pressing two keyboard buttons for an Escape Sequence, it only counts as one character to the program. ``cout << "Hello";`` is five characters, while ``cout << "\n"`` is only one.

.. _s1-pfl-l01:

Lecture 01:
-----------

| The most relaxing class. We just did introductions 

.. _s1-pft-t001:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l06:

Lecture 06:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l07:

Lecture 07:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l08:

Lecture 08:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l09:

Lecture 09:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l10:

Lecture 10:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^

.. _s1-pft-l11:

Lecture 11:
-----------

.. _s1-pft-t000:

(Topic learnt)
^^^^^^^^^^^^^^




