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

.. code-block:: c++
   :linenos:
   :emphasize-lines: 1,2,3,8
   
    #include <iostream>
    using namespace std;
    int main() {
        // Write
        // Your
        // Code
        // Here
        return 0;
    }

| Now you're probably wondering what all of that is. So lets get to work:

*    ``#include <iostream>`` is called a 'Preprocessor Directive'. It's written at the top and basically prepares the rest of the program for these commands. #include means, that specific library has to be included. We're gonna look at other libraries later.
*    ``using namespace std;`` means using names for objects and variables from the standard library. Don't focus on what it does for now, just know that you have to write it.
*    ``int main()`` is a Function. You'll learn Functions in OOP but for now just understand that, ALL of your code that you write, is to be written inside of this. If written outside or if you don't mention this line, it WILL NOT work. It has to be written between the {curly brackets}.
*    ``return 0;`` is also a part of the Function. Just know that you have to write it at the absolute very end for now. This isn't always important, as the program works completely fine without it, but I've lost marks on quizzes for forgetting to write it so, it's better if you do.
| There's still more stuff to actually cover, but that above is just the template. MAKE SURE to memorize it, you will need it for the rest of the semester.
| Other Syntax that you'll use for Program Execution:
*    ``cout``: Used to output to the Console. Written in format of ``cout << "Hello World!";``
*    ``endl``: Written at the end of a cout statement so that anything that comes after is done in a new line. Written in format of ``cout << "Hello World!" << endl;``
| Do make sure to write a semicolon at the end of every single thing you write. The only time you don't, is for # lines, and after the ``}`` which is found below ``return 0;``.
