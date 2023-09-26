.. _s2-oop-t19:

19) Operator Overloading
------------------------

| Out of the frying pan and into the fire. It's crazy just how much functionality and freedom C++ gives you. Being able to make your own data type, having specific ways to Construct it, Destruct it, Copy it, Make Friends, and now perform specific operations on it. The only caveat is having to program all the functionality yourself, while Python just has all of this freedom built in, at the cost of computing time.
|
| Operator Overloading lets you perform specific tasks on Objects through the use of already existing operators within C++. It saves you from the headache of trying to use function names. It's the kind of thing where you spend a lot of time and effort on making the class as polished as possible, so the implementation of it for the user, whether it's you or someone else, is as easy and as efficient as possible. If you're the only one that's working on your code then readability can be thrown out the window as long as it works, but later on you're going to be working in teams, and asking for improvement or advice or trying to understand and cooperate with people about implementations, or might want to make it futureproof so the future you or whoever replaces you can understand what you actually did and make improvements. This is what makes readability so important. It's much much easier and much more readable to write ``c3 = c1 + (c2 * c3);`` than it is to write ``c3(c1.add(c2.mul(c3)));``. Operator Overloading is really just having easier syntax for class functionality. You already saw a preview of it if you ran the code near the end in :ref:`s2-oop-t15`. So, let's get started.
|
| Operator Overloading means to define additional meanings for existing operators. It lets different operators perform different functions. Most of the base Data Types have operators implemented already, such as ``*`` for multiplication, ``+`` for addition, ``>>`` for Bitwise Right Shift, and so on. In :ref:`s1-pf-t33` I gave plenty of examples of Operator Overloading, such as ``>>`` and ``<<`` being used for Bitwise Right Shift and Bitwise Left Shift, but also for input and output using ``cin`` and ``cout``, and ``a & b`` being the bitwise ANDing of ``a`` and ``b``, but ``&a`` being the address of memory where ``a`` is stored, and ``*`` being used for multiplication and also for pointer creation and pointer dereferencing. We want to define these operators and many others for user-defined data types. 
|
| We can't create new operators for our own uses, but considering just how many are already available, we don't really need to either. Be warned, though. Operator Overloading if done right can make things way simpler and easier, but if done wrong or the implementation isn't proper, then it makes the program even harder to understand.
|
| An operator can be overloaded through this syntax:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 1, 6, 9, 11, 14, 18

    ReturnType operator/(Argument 1, Argument 2); // This is a Function Prototype

    class ClassName {
        // Data Members
    public:
        ClassName operator+(Argument) {
            // Code
        }
        ClassName operator-(Argument);
    };
    ReturnType ClassName::operator-(Argument) {
        // Code
    }
    ReturnType operator*(Argument 1, Argument 2) {
        // Code
    }

    ReturnType operator/(Argument 1, Argument 2) {
        // Code
    }

| It uses a special keyword called ``operator``, followed by the symbol to overload. Above are all the possible ways to implement it:
*   As Member Function - In-Line (Line 6)
*   As Member Function - Out-Of-Line (Line 9)
*   As Independent Function - Without Prototype (Line 14)
*   As Independent Function - With Prototype (Line 1 and 18)
| If implemented as Member Functions then it's necessary that they're NOT static. Static Member Functions only work with Static Data Members. There's no point in having Operator Overloading if you're not making objects interact with each other.
|
| The symbol you use doesn't actually affect what the function is do. You could very easily program the ``*`` symbol to perform addition, and the ``+`` symbol to perform multiplication. It just depends on what you write within the function definition, but again, the purpose is to make implementation and coding easier. Try to make the symbols appropriate for the code.