.. _s1-pf-t23:

23) Functions
-------------

| You might think that this is being taught too early if you already know about it. But this is something that took me 10 minutes to understand, while I've already spent hours on Pointers and still have no idea what those things are.
|
| And also, I'm just following the order of teaching which my university is following, so, we're doing Functions.
|
| This is something that takes us all the way back to :ref:`s1-pf-t05`. The first block of C++ code you saw. I'll rewrite it here.

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

| I wrote on that page to just understand that you just have to remember some of the stuff there as it is, and don't question the why. Well, now we learn more about it.


.. code-block:: c++
   :linenos:
   
    int main() 
    {
        return 0;
    }

| This, is a function. In Maths, a Function is defined as something that takes an input and gives an output. In C++ it works very similarly, though you can do way more with it.
|
| Functions are a programming style, just like loops. They don't solve a specific problem, and a problem can be solved without them as well.
| Functional Programming can also be called Modular Programming. This is to deal with things in parts, and more importantly, to re-use parts of code if needed.
|
| The first and most important function you worked with was ``main()``. Other than that, you might have used ``pow()``, ``get.line()``, ``setw()``, and more. These are all built-in functions. In some of them (like ``pow()``), you can enter values and then they do specific things. Now, you'll be making your own functions and doing things with them.
|
| There's three things involved with functions:
*    (Optional) Function Declaration/Prototyping
*    (Compulsory) Function Definition
*    (Compulsory) Function Calling

.. code-block:: c++
   :linenos:
   :emphasize-lines: 4,5,6,7,11,12,13
   
    #include <iostream>
    using namespace std;

    void myFunc()
    {
        cout << "Hello World!" << endl;
    }

    int main() 
    {
	myFunc();
	myFunc();
	myFunc();
        return 0;
    }

| The code above is an example of a Function and also using it. The Custom Function is called ``myFunc``, and it's being called in ``int main()``. The output would be three lines of ``Hello World!``.
|
| So let's get to explaining:
| A function is declared by the format: ``return type | name | arguments``.
*    Return Type is a Data Type. It can either be ``int, float, double, bool, char, string, void``. The new one among those is ``void``. Return Type means that when the Function is done doing its thing, then it *returns* a value. Exactly how the Maths functions work. They return a value, and *only* one value. That's why we write ``return 0;`` at the end of ``int main()``. If there's no value to return, however, then you use ``void``, as shown in the example above. If a function does not have a Return Type, then a Variable can't be assigned the value of it. You can do ``a = pow(4, 5)``, but if the ``pow()`` function used the ``void`` Return Type, then you wouldn't be able to do that. You also have to make sure that the data type matches. You can't define a function as an ``int`` and then return ``2.0``, for example.
*    Name means the name of the Function. In the example above, it's called ``myFunc``. It follows the same naming style as regular Variables.
*    Arguments are values given to the function from the outside. Remember how ``pow()`` needs values? So you'd write something like ``pow(5, 3)`` to get 5\ :sup:`3` \. ``5`` and ``3`` are Arguments. They'll be talked about on the next page.

| In the code above, ``void myFunc()`` is the line where the Function is defined, and ``myFunc();`` is the line where the Function is called. But if you move the Definition of the Function to be after ``int main()``, it'll give an error. It's like calling a Variable before it was declared.
| So the solution is either to keep the Function Definition before ``int main()``, or to do something called a Function Declaration so you can put the actual Definition anywhere you want. Function Declaration is also called Prototyping. It was the Optional thing involved with Functions.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 3,14,15,16
   
    #include <iostream>
    using namespace std;
    void myFunc(); // Function Declaration

    int main() 
    {
	myFunc();
	myFunc();
	myFunc();
        return 0;
    }

    void myFunc() // Function Definition
    {
        cout << "Hello World!" << endl;
    }
    
