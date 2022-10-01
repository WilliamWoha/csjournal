.. _s1-pf-intro:

Semester 1: Programming Fundamentals
====================================

| On the right side of the page you'll find a table of sorts that, upon clicking any of the text there, will take you to that section of the page. The page is very long, it has the notes of the ENTIRE SEMESTER. Further organizing it wasn't possible, that's why it's like this.
| If you're after a specific topic then just press Ctrl-F (or if in browser, then 'Find in Page') to search for it.
|
| I don't want FAST to come after me and try to take this thing down so, none of their material will be uploaded here. I can however reference info from it, and upload and link files that don't belong to them.
| Programming Fundamenttals has 4 Total Credit Hours. 3 for Theory, and 1 for Lab. That means for 16 weeks, there will be 3 hours a week for Theory and 1 hour a week for Lab. Yes, we do three hours but that's beside the point. Credit Hours are counted weirdly.
| Outline for PF Theory:

*    4 Assignments. Total Absolutes: 12
*    1 Sessional-I. Total Absolutes: 10 
*    1 Sessional-II. Total Absolutes: 15
*    4 or more Quzzes. Total Absolutes: 10
*    1 Project. Total Absolutes: 13
*    1 Final Exam. Total Absolutes: 40

| Outline for PF Lab:

*    14 or more Lab Tasks. Total Absolutes: 30
*    1 Sessional-I. Total Absolutes: 8
*    1 Sessional-II. Total Absolutes: 12
*    1 Project. Total Absolutes: 10
*    1 Final Exam. Total Absolutes: 40

Grading Polcy is Absolute Grading.

| Textbooks:

*    Starting Out with C++: From Control Structures through Objects; Ninth Edition by Tony Gaddis
*    Starting Out with Programming, Logic, and Design; Third Edition by Tony Gaddis
*    Starting Out with C++; 8th Edition by Tony Gaddis

| Software:

*    Ubuntu, version 20.04, installed via Dual Boot or Virtual Machine (They say it's not allowed but honestly a VM is better for most cases. It works perfectly fine and I use it. It's far far less of a hassle to install and takes less space)
*    G++ Compiler Suite in Ubuntu
*    Text Editor (Preferably GEdit) in Ubuntu

.. _s1-pft-l01:

Theory Lecture 01
-----------------

| Week 1.
| The most relaxing class. We did introductions, learnt about the course, what absolutes are, what GCR to join, which books and software we need, and were also warned about how difficult it was gonna be but took it lightly. Don't make our mistake, young reader, this institution will break you unless you're prepared. At the time of writing this (1st October 2022), it already broke my colleagues. In the first Sessional of Calculus, the total marks were 60. Our class average was 24/60. The Highest in Section A was 36 and in Section C was 40. You must be ready.

.. _s1-pfl-l01:

Lab Lecture 01
--------------

| Week 1.
| It was a lot of people there and a lot of noise but pay attention as EVERY SINGLE LAB CLASS for PF Lab is graded. You'll need a laptop or computer already. If you don't have one then you'll have to stay extra hours at FAST so you can use their labs. That might affect your situation with transport, but they don't care. You either do it or you don't get a grade. If you need a good machine for little cost, then get an old laptop and put an SSD in there.

| You learn Ubuntu in this class. The Terminal is the thing that you'll use the most. The commands to remember are:

*    ``mkdir name``: Makes new folder in current directory with name of ``name``
*    ``touch name.ext``: Makes new file in current directory with name of ``name`` and extension ``.ext``
*    ``cd name``: Changes Directory to folder ``name``
*    ``cd ..``: Moves up one directory
*    ``cd``: Moves to root directory
*    ``ls``: Shows all files in directory
*    ``ls -l``: Shows all files in directory in detailed manner with read, write, and execute permissions.

| Get used to them. You'll be using them a lot.

.. _s1-pft-l02:

Theory Lecture 02
-----------------

| Week 1.
| A lot of background information on what Fundamentals means and what Programming means, and then finally, Programming Fundamentals. Computer Organization is also important and then there was the history of Von-Neumann.

| There are three types of languages:
*    Machine Language: Only language machine actually understands. This is the 0's and 1's you see. Very cumbersome for humans but ALL languages are deconstructed to this level via something that translates them for the computer.
*    Assembly Language: 1's and 0's with letters. It's very very close to Machine Language but is readable by humans. You can program in it but it will test your patience like no other. But hey, Chris Sawyer got 30 Million Dollars for it since he made a game called RollerCoaster Tycoon. So if you have the guts, then go for it. The translator for Assembly Language is called the Instructor.
*    High Level Language: Way closer to Human Language. Uses Common Math operations, and converted either in real time with Interpretors, or after compiling all at once with Compilers. C++ is a Compiled language. Compiler languages are much faster than Interpreted languages but troubleshooting can be a massive hassle as, if one part of the code doesn't work, the entire thing drops.

.. _s1-pft-l03:

Theory Lecture 03
-----------------

| Week 2.
| Logic and Problem Solving. It explained about flowcharts and pseudocode, and why they're used. Pseudocode is widely used as it is easy to read, has no strict syntax, and lets the Programmer focus on the logic first. That's literally it, it just explained those three things again. If you know them, great. Othewrise, just google them. I'm not explaining here.

.. _s1-pfl-l02:

Lab Lecture 02
--------------

| Week 2.
| More about Problem Solving with Algorithms and Flowcharts. Then we made some flowcharts and did a Scratch assignment.

.. _s1-pft-l04:

Theory Lecture 04
-----------------

| Week 2.
| Now we're doing the good stuff. Welcome to C++.

.. _s1-t001:

Intro to C++
^^^^^^^^^^^^

| History: It has a lot. But this doesn't matter in your exams.
| Syntax: This is THE MOST important thing to remember. It's crucial that you memorize this as you'll lose marks if you miss a single detail.

    | ``#include <iostream>``
    | ``using namespace std;``
    | ``int main() {``
        
        |
        | ``(code)``
        |
        | ``return 0;``
    | ``}``
| Now you're probably wondering what all of that is. So lets get to work:

*    ``#include <iostream>`` is called a 'Preprocessor Directive'. It's written at the top and basically prepares the rest of the program for these commands. #include means, that specific library has to be included. We're gonna look at other libraries later.
*    ``using namespace std;`` means using names for objects and variables from the standard library. Don't focus on what it does for now, just know that you have to write it.
*    ``int main()`` is a Function. You'll learn Functions in OOP but for now just understand that, ALL of your code that you write, is to be written inside of this. If written outside or if you don't mention this line, it WILL NOT work. It has to be written between the {curly brackets}.
*    ``return 0`` is also a part of the Function. Just know that you have to write it at the absolute very end for now. This isn't always important, as the program works completely fine without it, but I've lost marks on quizzes for forgetting to write it so, it's better if you do.
| There's still more stuff to actually cover, but that above is just the template. MAKE SURE to memorize it, you will need it for the rest of the semester.
Other Syntax that you'll use for Program Execution:
*    ``cout``: Used to output to the Console. Written in format of ``cout << "Hello World!";``
*    ``endl``: Written at the end of a cout statement so that anything that comes after is done in a new line. Written in format of ``cout << "Hello World!" << endl;``
| Do make sure to write a semicolon at the end of every single thing you write. The only time you don't, is for # lines, and after the ``}`` which is found below ``return 0;``.

.. _s1-pft-l05:

Theory Lecture 05
-----------------

| Week 3.
| Yes I know there's some syntax not written in the above section, we'll get to it later. One thing at a time. If something isn't written it means the university will explain it later. And right now we've just done the main template for every C++ program, and cout statements. And believe me, even this is gonna be enough for now.
| There's these things called Escape Sequences. When you output a string, for example, ``cout << "Hello World!" << endl;``, then ``Hello World!`` is the output that appears in the console. If you write two lines, one below another:
| ``cout << "Hello" << endl;``
| ``cout << "World!" << endl;``
| You get the output of:
| Hello
| World!
| But what if we wanted to do it in only one line? That's where Escape Sequences come in.

.. _s1-t002:

Escape Sequences
^^^^^^^^^^^^^^^^

| Two lines had to be written so 'Hello' and 'World!' were in different lines. But there's a way to do it in only one line:
| ``cout << "Hello \n World!";``
| This would output:

    | Hello
    
        | World!
| I'll explain the extra space there later. The ``\n`` is the Escape Sequence. The Backslash, ``\``, is what's used to trigger it. Within any "code which is written in speech marks", if a ``\`` is written, it's not gonna be there. An Escape Sequence is used to trigger something within the text. ``\n`` will trigger a new line. ``\t`` will trigger Tab, which aligns with columns. ``\"`` is used to write speech marks where it's not possible. This happens where, if for example you want to output:
| I "love" Programming!
| You'd think it's as simple as writing ``cout << "I "love" Programming!";``, but no. the program can only work with one pair of speech marks at once. So here, the actual code to get the output above, would be ``cout << "I \"love\" Programming!";``. Just like that if you also wanna output the actual backslash, you just write it twice. ``cout << "\\\\";`` would output ``\\``.
| ``\`` only reads the character in front of it. So writing "\\\\n" would in fact just output ``\n``.
| An important thing to note is, Even though you're pressing two keyboard buttons for an Escape Sequence, it only counts as one character to the program. ``cout << "Hello";`` is five characters, while ``cout << "\n"`` is only one.
| Now, remember that extra space? That's because the code was ``cout << "Hello \n World!";``. There's a space between ``\n`` and ``World!`` which causes that gap to happen, as ``\n`` causes a new line, then there's a space, then there's ``World!``. The space is also a character. If you want it to be in line, the code would be ``cout << "Hello \nWorld!";``. And, though less readable for humans, ``cout << "Hello\nWorld!";`` would be the true solution.

.. _s1-t003:

#include <iomanip>
^^^^^^^^^^^^^^^^^^

| You remember ``#include <iostream>`` right? This is another library you should get used to. This one's called ``iomanip``, which stands for Input Output Manipulation.
| Here's some commands to know about:
*    ``setw(num)``: Sets output in characters. If number of characters is too many, it will cut off. If number of characters is not enough, it will fill empty locations via another character (By default it will leave spaces, but the character can be changed with setfill() ). Written in format of ``cout << 30.5/6 << setw(4);``. Do note, this doesn't apply to the entire ``cout`` statement, but rather only the neighboring thing separated by ``<<``, so you can use multiple in one ``cout`` statement.
*    ``setfill('char')``: Chooses what characters to use for extra spaces, if any are left from ``setw()`` being too high.
*    ``setprecision(num)``: Chooses number of significant figures to output. Decimals are not counted. If too high of a number is entered, it will give the full number. If too low of a number is entered, such that it can't cover all decimal places, then it will use scientific notation, like 2.4e5. If the number is high enough to cover all decimal places then it will output that amount of significant figures. It will do rounding for the last number.
| All of these are written to the left of the thing they are to affect. You can remember this easily by remembering that code outputs left to right, so it has to come first. ``cout << setw(10) << setfill('*') << setprecision(6) << 34.678156`` would output:

    | ``***34.6782``

.. _s1-pfl-l01:

Lab Lecture 03
--------------

| Now you actually learn how to make the C++ program via the Compiler in Ubuntu. Navigate to the directory where it's stored in the Terminal, then to compile it (and it's important that this is in order. Remember this line, you're gonna use it a lot) write:
| ``g++ -o name2 name.cpp``
| Where ``name.cpp`` is your C++ compiled file, and name2 is the name of the Compiled Program. There's no file type associated to it (Don't worry about it for now). This command just generates a file called ``name2`` in the same directory, and this is the comiled program. To run said program, in the Terminal you just write ``./name2`` (NOT ``./name2.cpp``). Make sure you're still in the same directory or else it won't work.
| If the compilation was successful and these instructions were done correctly, your program should now run in the terminal.
| Memorize these steps. You have to do them EVERY TIME you wanna test the code. First Save it in the text editor (aka in the ``.cpp`` file), then run the command to compile, then execute.

.. _s1-pft-l06:

Theory Lecture 06
-----------------

| This whole time we've been doing ``cout``. Now it's time for actually inputting data. Welcome to variables, data types, and ``cin``.

.. _s1-t004:

Data Types
^^^^^^^^^^

| There's 6 Data Types in C++:
*    Integer (Declared by ``int``)
*    Float (Declared by ``float``)
*    Double (Declared by ``double``)
*    Boolean (Declared by ``bool``)
*    Character (Declared by ``char``)
*    String (Declared by ``string``)
| Out of the 6 above, 5 are already in ``<iostream>`` and part of the foundation of C++. String is the odd one out. To use it, you need to import the ``<string>`` library.

    | #include <string>
| Integers are Whole Numbers only, Float and Double are Decimal Numbers.
| Character holds the data of a single character in ' ', and String holds the data of multiple characters in " ".
| Boolean has only two options: It is either True or False.
|
| Computers don't recognize letters, their memory holds numbers. So they convert them using the ASCII table. Here's what you need to remember: ``A`` has the integer value of 65, ``a`` has the integer value of 97. REMEMBER THEM. YOU GET ASKED QUESTIONS ON THEM.
| 
| Each data type takes location in memory by varying amounts. Int takes 4 bytes, which is 32 bits, and has a range of ``-2147483648`` to ``2147483647``. Short int takes only two bytes, hence having a range of ``-32768`` to ``32767``. Long int has 8 bytes, and Long Long int has 16 bytes. You can use ``cout << sizeof(int)`` to find the number of bytes they take.
| Float takes 8 bytes, Double takes 16 bytes, Bool takes one byte, Char takes one byte, and String is...we don't talk about that.
| You can transfer values from one variable to another but if the first one was bigger in size than the second then some data is truncated, aka lost. We'll deal with that later.
|
| To do a declaration, write ``type name;``. So for example, ``int a;``, ``float num;``, ``char c = 'p'``, ``string a,b,c;``, ``int a=2;``, ``int x=y=z=4;``, ``float num1=2, num2=3.5;`` are all valid declarations. The later ones you can figure out on your own.
| You don't have to immediately declare a value. You can just assign it later. The way to do so would be ``var = value``. So if you have ``int a;`` and then ``a = 3``, and if you did ``cout << a << endl;``, you'd get an output of 3. The ``=`` is what assigns values.

.. _s1-pft-l07:

Theory Lecture 07
-----------------

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
*    ``/,%,*``: If in same line, left to right
*    ``+,-``: If in same line, left to right

| So ``(3+2)*6`` would give 30 and ``3+2*6`` would give 15
| ``6*4+3-2/5`` would give 32

.. _s1-t007:

Type Coercion (Type Casting)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Coercion means conversion. You can convert between data types. There's multiple ways to do so. It either falls under Type Promotion or Type Demotion.

    | ``float a = 3.2;``
    | ``int b = 10;``
| ``a / b``, ``b / a``, ``a * b``, ``a + b``, and ``a - b`` would all give an output in float form. All of them "Promote" the int to a float then do an operation on it (MOD won't work, MOD needs two integers). The compiler does it automatically, you don't have to do it. This is what we call Automatic Type Coercion.
| Data Type Ranking determines whether the conversion is promoting or demoting. It goes as follows: Long Double, Double, Float, Unsigned Long Long Int, Long Long Int, Long Int, Unsigned Int, Int. So in simple terms, Double, then Float, then Int, with Int being lowest rank and Double being the highest rank.

    | ``int answer = a*b;``
| ``a`` is float, and ``b`` is int. ``b`` gets promoted to float, and then the math operation is done. ``a * b`` is calculated. This is then saved to ``answer``, but the value gets demoted into ``int`` as the declaration of ``answer`` was in ``int``. Decimal Place values are truncated.
| 
| To do the conversion manually, there's two ways:
*    ``static_cast<data type>(value)``: Static Cast. In ``<data type>`` you write the data type you want to convert to, such as ``float``. In ``value``, you write the variable name or the direct value you want to convert.
*    ``type(value)`` or ``(type)value``: Write the data type in ``type``, and the variable name or direct value you want to convert in ``value``.
| If you do float(7/10) the result would be 0. If you instead do float(7)/10 then you get 0.7. It solves in the brackets first so make sure you're converting BEFORE the division.

.. _s1-pft-l08:

Lecture 08:
-----------

.. _s1-t008:

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




