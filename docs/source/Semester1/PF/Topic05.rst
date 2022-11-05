.. _s1-pf-t05:

5) Intro to C++
---------------

| Well, we're jumping straight into this then.
| I've already explained the Binary System and Flowcharts on the previous pages. That knowledge won't immediately be tested but those concepts will show up again.
|
| Yes, there are PLENTY of Programming Languages. Python, Java, JavaScript, C++, C#, VisualBasic, and more. There's also things like HTML and CSS but those aren't programming languages, they're mostly used for Web Development stuff.
| This is programming. And I'm doing C++ because that's what my university is teaching me.
|
| Personally I do know C++, VisualBasic, and Python, but I know C++ the best among all of those, and since my university is also teaching me this, that's why I'm doing this specific language. Everything you read till before now can be applied to *any* language at all, but from here on out, it will be C++ specific things. If you're not interested in C++ then there's hundreds of courses for other languages that are both paid and free and they're by people with far more experience than me, and you can find them across the internet on sites like YouTube or Udemy or Codecademy.
|
| I'll still write the info here as a reading resource in case it comes in use to anyone.
|
| So, let's begin with C++.
|
| The *MOST IMPORTANT* thing to remember is Syntax. Syntax means structure, and structure is *CRUCIAL* in a Programming Language.
| Assuming you've installed VSCode from :ref:`s1-pf-req0`, open it. Otherwise, install it.
| Syntax: This is THE MOST important thing to remember. It's crucial that you memorize this as if you mess this up, even with one letter, your entire program will be unable to work.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 1,2,3,11
   
    #include <iostream>
    using namespace std;
    int main() 
    {
        //
        // Write
        // Your
        // Code
        // Here
        //
        return 0;
    }


| Now you're probably wondering what all of that is. So lets get to work:

*    ``#include <iostream>`` is called a 'Preprocessor Directive'. It's written at the top and basically prepares the rest of the program for these commands. #include means, that specific library has to be included. There are other # commands, and also other things you can 'include' with #include, but we'll look at those later..
*    ``using namespace std;`` means using names for objects and variables from the standard library. Don't focus on what it does for now, just know that you have to write it.
*    ``int main()`` is a Function. You'll learn Functions later but for now just understand that, ALL of your code that you write, is to be written inside of this. If written outside or if you don't mention this line, it WILL NOT work. It has to be written between the {curly brackets}.
*    ``return 0;`` is also a part of the Function. Just know that you have to write it at the absolute very end for now. This isn't always important, as the program in most cases works completely fine without it, but I've lost marks on tests for forgetting to write it, so it's better to make a habit of doing it.
| There's still more stuff to actually cover, but that above is just the template. MAKE SURE to memorize it, you will need it for the rest of the semester.

.. code-block:: c++
   :linenos:
   
    #include <iostream>
    using namespace std;
    int main() 
    {
        cout << "Hello World!" << endl;
        cout << "I love Programming!" << endl;
        return 0;
    }

| Copy that code above, paste it into VSCode, and then Right Click and click Run Code. In the bottom, you'll see the Output of the code. The output being:

.. code-block:: c++

	Hello World!
	I love Programming!


| More Syntax:
*    ``cout``: Used to output to the Console. Written in the format of ``cout << "Hello World!";``
*    ``endl``: Written at the end of a cout statement so that anything that comes after is done in a new line. Written in format of ``cout << "Hello World!" << endl;``.
| If the same code above was written without '<< endl' at the end, it would give this output:

.. code-block:: c++

	Hello World!I love Programming!


| Do make sure to write a semicolon at the end of every single thing you write. The only time you don't, is for # lines, and after the ``}`` which is found below ``return 0;``.
| The spaces you see where you write the code aren't necessary. In fact you can write the whole thing in just two lines

.. code-block:: c++
   :linenos:

    #include <iostream>
    using namespace std;int main() {cout<<"Hello World!"<<endl;cout<<"I love Programming!"<<endl;return 0;}

| The result is the exact same. But it's FAR more readable with proper lines and gaps, which is why it's just good coding practice and it's something to make a habit of.