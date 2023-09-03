.. _s1-pf-t24:

24) Parameters and Arguments
----------------------------

| Having fun?
| I sure am
| 
| not.
|
| I never realized just how much content was involved until I tried recreating it and re-explaining it.
| Moving on.
|
| The one thing we didn't talk about on the previous page was the Arguments. I wrote that it would be discussed on the next page. Well, here we are.
| When you write ``pow(5, 3)``, you're giving ``5`` and ``3`` to the function as values. It's then using those values to give you a result. In this case, 125 would be the result from that.
| The values which are passed to Functions are called Arguments.
|
| Parameters are what the Function then uses further within itself.
|
| We'll do something later called Local and Global Variables, so for now all you need to look at is this:


.. code-block:: c++
   :linenos:
   :emphasize-lines: 4,11
   
    #include <iostream>
    using namespace std;

    void square(int x)
    {
        cout << x*x << endl;
    }

    int main() 
    {
	square(5);
        return 0;
    }

| In ``int main()``, the Function is called. Before that, it was defined. So there's no error there. But this time, we want to forward a value to the Function, and that value is provided within ``int main()``. In this case, the value is ``5``.
| Notice how the brackets of *this* function declaration aren't empty. That's because a parameter is defined there.
|
| To explain what's happening: We defined a function, and in the brackets, we defined something called Parameters. If a Function is called, and a value is passed to it, then it needs to bring that value back to itself. It does that using Parameters. Parameters are basically specific variables that store values which are given when it's called.
| Arguments are the actual values being passed. So in this case, ``5`` is an argument.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 4,11
   
    #include <iostream>
    using namespace std;

    void sum(int x, int y)
    {
        cout << x+y << endl;
    }

    int main() 
    {
	sum(5, 10);
        return 0;
    }

| In this code, there's two Perimeters: ``int x``, and ``int y``, during the Function Definition.
| Two arguments are passed: ``5``, and ``10``. Those Arguments are stored in ``x`` and ``y``, and then used in the Function.
|
| You might be wondering why the Function Return Types are set to ``void`` even though some code is clearly being executed and calculations are being done.
| The thing is, the specific keyword of ``return`` means to give a value *back*. So if you do ``a = pow(3, 5);``, then ``pow(3, 5)`` is calculated, and then the result of it is returned to ``a``. This is not the same as, calculating the result within the function, and then writing ``cout << result << endl;``. There's no value being given back. It's just executing code.
