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
| Other Syntax that you'll use for Program Execution:
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

    | ***34.6782

.. _s1-pfl-l03:

Lab Lecture 03
--------------

| Week 3.
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

.. _s1-pfl-l04:

Lab Lecture 04
--------------

| Week 4.
| Just did more practice of type casting. Read the above.

.. _s1-pft-l08:

Theory Lecture 08
-----------------

| Week 4.
| This is gonna be a long one because of something called the Keyboard Buffer. Get ready.

.. _s1-pft-t008:

Variable Assigning using itself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    | ``int sum = 30;``
    | ``sum = sum + 10;``
| Does that make sense to you?
| If you called ``sum`` after those two lines, you'd get a value of 40.
| When assigning (meaning in statements with ``=`` in them), the Compiler first works out the things on the right side, then assigns it to the variable on the left side. So for the line ``sum = sum + 10``, it first takes the value of ``sum`` from memory, does the required operations on it (in this case, addition of 10), and then assigns it. It just so happens to be that the assigning part happens to be at the original memory location.
| In these situations, aka the ones where the variable works on itself, we can do something called `Combined Assignments`.
*    ``sum = sum + 10`` is ``sum += 10``
*    ``sum = sum - 10`` is ``sum -= 10``
*    ``sum = sum * 10`` is ``sum *= 10``
*    ``sum = sum / 10`` is ``sum /= 10``
*    ``sum = sum % 10`` is ``sum %= 10``
| If we do ``cout << sum + 10``, will the value of ``sum`` change? No. That just calculates and then outputs, there's no assigning taking place.
| ``x += b + 5;`` is ``x = x + b + 5;``

.. _s1-pft-t009:

Keyboard Buffer (.get(), getline(), .ignore())
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Here's a funny thing about using ``#iostream <string>``. If you try to put data into a ``string`` variable via a ``cin`` statement, it won't store values past an escape sequence. Here's the program:

    | ``string name;``
    | ``cin >> "Enter name: ";``
| If I write John Cena into that, then try to check the value of ``name``, it will give me an output of ``John``.
| But there's this thing called the Keyboard Buffer. The thing is, this Buffer holds the data for all the keys pressed via the keyboard. ``John Cena`` is stored in the Keyboard Buffer, but the ``cin`` statement only read it until ``John``.
| Here's an even funnier thing:

    | ``string name, city;``
    | ``cout << "Please enter your full name: " << endl;``
    | ``cin >> name;``
    | ``cout << "Please enter your city: " << endl;``
    | ``cin >> city;``
    | ``cout << "Your full name is " << name << ", and your city is " << city << endl;``
| If you ran that code and entered John Cena into the first prompt for an input, then you wouldn't even get the second prompt, and the code would output: ``Your full name is John, and your city is Cena``. This is because of the Keyboard Buffer.
| "John Cena" is stored in the buffer, but the ``cin`` statement finds an escape sequence at the space present between John and Cena. So it stops there. But then another ``cin`` statement is called. Since it stopped at the space button, it then picks up from there and finds Cena, and just puts that into the second ``cin`` statement.
|
| The solution? Use a thing called ``getline(cin, var);``. It works the same way as ``cin >> var;``. You just write ``getline(cin, var);`` instead. But the difference is, this time no matter what you write, all of it will be stored into the variable. It only stops when the Enter key is pressed, and doesn't store the ``\n`` from that either.
|
| There's also ``.get()``. You write it as ``var = cin.get()``. This will read any key that is pressed and store it into the variable. Be it Enter, Space, Escape, Tab, anything. It reads all of it. It's used in games for checking for specific button key presses.

    | ``char key;``
    | ``cin >> key;``
    | ``if (key == '\n')``
    | ``{``
    
        | ``(Some Code to trigger something)``
    | ``}``
| You want it to only work when Enter is pressed, but ``cin`` won't store Enter. So the solution? Replace ``cin >> key;`` with ``key = cin.get()``. If you press Enter, then ``\n`` will be stored into ``key``.
| If you just write ``cin.get();`` then it won't store the key, but instead works like a "Press Any Key to Continue" button.
| 
| There's an even funnier problem though.

    | ``int number;``
    | ``char ch;``
    | ``cout << "Enter number: " << endl;``
    | ``cin >> number;``
    | ``cout << "Enter Character: " << endl;``
    | ``cin.get(ch);``
    | ``cout << "Thank you." << endl;``
| This code has a problem.
| You won't get the opportunity to store a character into the ``cin.get()``.
| In the first ``cin``, if you write 324 then press Enter, the buffer would have these characters in it:
| ``3`` ``2`` ``4`` ``\n``
| ``\n`` is an escape sequence and is one character. ``cin`` reads until that point and stores the numbers into the variable, but ``\n`` isn't removed, it's still there. That gets stored into ``cin.get(ch)``. You don't get the prompt.
|
| The solution? Another command. ``cin.ignore(cond1, cond2)``. This is mentioned now instead of way back with John Cena because it only solves the problem of the rest of the Keyboard Buffer going into the next ``cin`` statement. It didn't solve the problem of Space not being stored.
| ``cin.ignore(cond1, cond2)`` will ignore characters in the Keyboard Buffer until either Condition 1 is fulfilled, or Condition 2 is fulfilled. Condition 1 is a number value, and Condition 2 is a character check. ``cin.ignore(20,'\n')`` will ignore characters in the Keyboard Buffer until a ``\n`` is found, or until 20 spaces.

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

.. _s1-pfl-l05:

Lab Lecture 05
--------------

| Week 5.
| It was just more practice of Type Coerciion. Read :ref:`s1-t007` for details. There was a specific problem called Problem 04 which we were told to leave for now as none of us could figure it out. We had to take the individual digits of a number and keep adding them until we got to a one digit answer, but the catch is that we're not allowed to use the MOD ``(%)`` operator to actually separate the digits.
| I'll write the answer here if I find it later.

.. _s1-pft-l10:

Theory Lecture 10
-----------------

| Week 5.
| Here's the syllabus of the Sessionals:
*    Data Types (Typecasting, Overflow/Underflow)
*    Variables and Constants
*    ``<cmath>`` functions
*    Operators (Bitwise, Arithmetic, Logical, Relational)
*    IF/ELSE
| Actually at the time of writing this we just finished the Sessionals 5 days ago (October 2nd, 2022, Sunday 8:15AM). We get the results tomorrow, I'll write any extra info or questions or whatever can help. We have another Sessional on Tuesday (October 4th, 2022) and I have no idea how that's gonna go. Best advice I can give for now is, practice your typing.

.. _s1-pft-t011:

Overflow and Underflow
^^^^^^^^^^^^^^^^^^^^^^

| Let's declare a variable called ``a``, with this line: ``short int a;``. The range of this value would be from ``-32768`` to ``32767`` (It's one less on the positive side as 0 is also included there). Overflow happens when the value tries to store a value greater than the max range, and Underflow happens when the value is smaller than the minimum range.
| Here's what actually happens. Let's say you declare ``short int a = 32767``. In bit form this would be ``0111 1111 1111 1111``. If you add one to it, the value becomes ``1000 0000 0000 0000``, which is equal to ``-32768``. Adding 1 to the max value turned it into the min value. If you do it for an unsigned short int instead, it would go from ``1111 1111 1111 1111``, which is 65536, which is the max value of an unsigned short int, then add 1 to it, it becomes ``1 0000 0000 0000 0000``. But the problem is that the 1 at the very beginning is truncated as there aren't enough bits to store it. So it just becomes ``0000 0000 0000 0000``, which is the smallest value.
| Overflow means adding more to the variable than it can handle, causing it to loop around to the smallest value. Kind of like a clock.
| It doesn't just work with 1, it works with any value, as long as it's actually ASSIGNING. If you do:

    | ``short int a;``
    | ``a = 32767;``
    | ``cout << a + 100 << endl;``
| Then you'd get 32867 in the console. If instead you did ``a = 32867;`` and then ``cout << a << endl;``, THEN you'd get the Overflow, and the value you'd get would be -32699, which is (32767+1), which is -32768, then +99 which is -32669.
|
| Underflow is all of that just the other way around.

.. _s1-pft-t012:

IF/ELSE
^^^^^^^

| At last we come to the HOLY GRAIL.
| Ok so the easiest way to understand it is, "If this happens then do this, otherwise do this". That's literally it. You just have to write that in code form.
| The key to understand this is Relational Operators and Logical Operators (You were probably wondering when we'd get to those huh?).
| Here's Relational Operators:
*    ``>=``: Greater than or equal to
*    ``<=``: Less than or equal to
*    ``>``: Greater than
*    ``<``: Less than
*    ``==``: Equal to
*    ``!=``: Not Equal to
| And now here's some Logical Operators:
*    ``&&``: AND
*    ``||``: OR
*    ``!``: NOT
| Here's how the syntax works.

    | ``if (condition) {``
    
        | ``(code)``
        | ``(more code)``
    | ``}``
| It can also be written as:

    | ``if (condition)``
    | ``{``
    
        | (code)
        | (more code)
    | ``}``
| There's no actual semicolon to write for the ``if`` statement itself. Just for the lines between it which are regular code. The brackets around ``condition`` are NECESSARY. No matter how big the statement is, there has to be one set of brackets holding it all together.
| The indentation (which means the gap for the code between the if statement) isn't necessary but is highly recommended for making code readable. It's just good practice to do.
| Then there's ELSE statements. Which mean, if the original IF condition isn't filled, then execute this code. "If this happens then do this, OTHERWISE do this". The ELSE statement is just the otherwise part of that sentence. And else just means the opposite of the if statement. You don't write a condition for it.

    | ``if (condition)``
    | ``{``
    
        | (code)
        | (more code)
    | ``}``
    | ``else``
    | ``{``
    
        | (code)
        | (more code)
    | ``}``
| Here's an example:

    | ``if (num % 2 == 0)``
    | ``{``
    
        | ``cout << "The number is an even number." << endl;``
    | ``}``
    | ``else``
    | ``{``
    
        | ``cout << "The number is an odd number." << endl;``
    | ``}``
| The reason that the Equals comparison sign is ``==`` and not ``=`` is because ``=`` is used for ASSIGNING. So if you just did one equals sign in an IF statement it would give an error.
|
| Here's something new. Let's say you have a statement called ``int n = 0;``
| Then you make an if statement of ``if (n)``. Would that statement trigger? Nope. But that's not because of the lack of comparison, it's just because n is 0. If you instead did ``int n = 1;`` or ``int n = 5;`` or ``int n = -3``, and then did ``if (n)``, then that statement would in fact trigger, because it's just checking that it's not 0. ``if (n)`` is the same as writing ``if (n != 0)``. ``if (!0)`` would also be true.
|
| One more thing to know about this (and I'm typing this now AFTER the sessionals. I didn't know it before) is that there's a priority for these operators and you need to know which one is carried out when.
| The highest to lowest priority goes as such:
*    Arithmetic Operators ``( + - / * % )``
*    Bitwise Shift Operators ``( << >> )``
*    Relational Operators ``( > >= < <= )``
*    Equality Operators ``( == != )``
*    Bitwise AND Operator ``( & )``
*    Bitwise XOR Operator ``( ^ )``
*    Bitwise OR Operator ``( | )``
*    Logical AND Operator ``( && )``
*    Logical OR Operator ``( || )``
| Yeah so I made the mistake of not knowing that the Logical AND is above the Logical OR, so in a question that asked ``A || B && C`` I assumed it was going left to right. In reality it first checks ``B && C`` then does ``||`` with ``A`` after that.
| A, B, and C are all just brackets with their own operations going on inside of them. Don't worry about it.

.. _s1-pft-l11:

Theory Lecture 11
-----------------

| Week 6, but this is the second class of the week and not the first. That one was lost due to Sessionals. I have no idea what they'll do to recover that.

.. _s1-pft-t013:

Selection Structures (elseif)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| So remember the statement I made earlier? "If this happens, then do this. Otherwise do this". Let's modify that a bit. "If this happens, do this, but if this happens, do this, and if neither of those happen, then do this". That's IF, ElseIF, and ELSE in a nutshell.
| Elseif is used when more than two conditions have to be checked. Let's assume we have two numbers, a and b.

    | ``if (a>b)``
    | ``{``
    
        | ``cout << a << " is greater." << endl;``
    | ``}``
    | ``elseif (b>a)``
    | ``{``
    
        | ``cout << b << " is greater." << endl;``
    | ``}``
    | ``else``
    | ``{``
    
        | ``cout << "Both are equal." << endl;``
    | ``}``
| There's three conditions there. One being, ``a > b``, the second being ``a < b``, and the third being ``a == b``. Now you could do this any way you want, and even put the ``a == b`` statement at the start and leave the other two in an ``elseif`` and ``else``. The choice is yours.
| You can have wayyyy more elseif statements too, for checking more conditions.
| Here's a little tip about IF statements though. Those ``{ }`` brackets you see? They're only used if there's more than one line of code to execute. Otherwise, you can be completely fine with something like this:

    | ``if (marks >= 90 && marks <= 100)``
    
        | ``cout << "A grade." << endl;``
    | ``elseif (marks >= 80 && marks < 90)``
    
        | ``cout << "B grade." << endl;``
    | ``elseif (marks >= 70 && marks < 80)``
    
        | ``cout << "C grade." << endl;``
    | ``elseif (marks >= 60 && marks < 70)``
    
        | ``cout << "D grade." << endl;``
    | ``else``
    
        | ``cout << "Failed." << endl;``
| And yes this is exactly how you do correction statements. You just write ``if (marks > 100 || marks < 0)`` at the start and get the code to output a statement saying that this isn't an acceptable answer.
| Anyways. That about covers that. The only thing left is Nested IF statements, and then my 9 hours of typing can come to a rest and PF will have been caught up. Then I'll do weekly updates on this or something.

.. _s1-pft-t014:

Nested Selections
^^^^^^^^^^^^^^^^^

| Ok so if you already know this then great but if you don't already know this then it's a rather simple concept but once you get it, it's super easy.
| "If Pizza Hut is open, go there. If they have the Medium Combo, then get the Medium Combo, otherwise get the Small Combo. If Pizza hut isn't open, go to Dominoes. If they have the Weekend Deal, get the Weekend deal. Otherwise, get a Buy 1 Get 1 Free Deal. If neither is open, come back home."
| Here's how that would be written in code.

    | ``if (Pizza hut is open)``
    
        | ``if (Medium Combo is there)``
        
            | ``Get Medium Combo``
        | ``else``
        
            | ``Get Small Combo``
            
    | ``elseif (Pizza hut is closed && Dominoes is open)``
    
        | ``if (Weekend Deal is there)``
        
            | ``Get Weekend Deal``
        | ``else``
        
            | ``Get Buy 1 Get 1 Free Deal``
    | ``elseif (Pizza Hut is closed && Dominoes is closed)``
    
        | ``Go home``
| That's about it. You should be able to understand that. If not then watch a YT video on it, I'm tired.
| You may have noticed that the last statement is an ``elseif`` and not an ``else``. That's because the two conditions before it were: ``Pizza hut is open``, ``Pizza hut is closed AND Dominoes is open``. If we did an ELSE statement here, that would also include the situation of both Pizza Hut and Dominoes being open. You're not supposed to go home if they both happen to be open.
| ELSE is the equivalent of checking the opposites of the previous IF statements.

.. _s1-pft-l11:

Theory Lecture 11
-----------------
| Week 7
| To be continued...
 
