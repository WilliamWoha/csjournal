.. _s1-pf-t25:

25) Default Parameters and Overloading
--------------------------------------

| We've barely touched Functions and now we're already pushing them into Overdrive. Or, well, Overloading. Overdrive just sounded cooler but it's not a Computers term or C++ term as far as I know.
| First need to explain Default Parameters though.

Default Parameters
^^^^^^^^^^^^^^^^^^

| Sometimes you can have Functions where you want to, just in case, have a default value to use in case the Argument isn't passed for it.
| I don't have too many notes on this but it is still important and useful. I just haven't gotten the chance to use it much myself yet.

.. code-block:: c++
   :linenos:

    #include <iostream>
    using namespace std;

    int sum(int a, int b)
    {
        return (a + b);
    }

    int main() 
    {
	cout << sum() << endl;
        return 0;
    }

| The code above would give an error. There's no arguments passed to ``sum()``, when it needs two of them. So there's two ways around this:
|
| First way is to pre-define the value in the Prototype.

.. code-block:: c++
   :linenos:

    #include <iostream>
    using namespace std;

    int sum(int a = 10, int b = 20);

    int main() 
    {
	cout << sum() << endl;
        return 0;
    }

    int sum(int a, int b)
    {
        return (a + b);
    }

| In the code above, ``sum()`` has no Arguments in it. But at least the code doesn't break. Now if it's called, it'll give a value of 30. Though that was only for concept. More realistically you'd set it to 0.

.. code-block:: c++
   :linenos:

    #include <iostream>
    using namespace std;

    int sum(int a = 10, int b = 20)
    {
        return (a + b);
    }

    int main() 
    {
	cout << sum() << endl;
        return 0;
    }

| This is the same thing as the code before it, except it's in the Definition instead of the Declaration.
|
| If you were to call it with ``sum(100, 50)``, you'd get 150 as the result. If you were to call it with just ``sum(100)``, then you'd get 120 as the result. The ``100`` is going into the Parameter of ``int a``. But there's no way to make it go into the parameter of ``int b``. You can't do ``sum( , 100)``. It just gives an error.
| This is why if you're doing Default Parameters, you have to also make sure that the possibly replaceable values are **ALL** on the Parameters on the Left side, otherwise they can't be replaced.

Function Overloading
^^^^^^^^^^^^^^^^^^^^

| Two functions of the same name aren't allowed, unless you do some trickery with Overloading.

.. code-block:: c++
   :linenos:

    int sum(int a, int b);
    int sum(int a, int b);

| This is an example of something that will cause a problem because it's just the exact same thing. And you can change the Return Type of one of them too, but it won't do anything, because the signatures aren't unique.
| The Signature is the part that's after the Return Type, so that means the Name and the Parameters.
|
| The objective is to make sure a Signature is unique, but I just wrote that Parameters are also included in that. So you might have realized that you can make another Function with the same name, as long as the Parameters are different. And you'd be correct! That's Function Overloading.

.. code-block:: c++
   :linenos:

    int sum(int a, int b);
    int sum(int a, int b, int c);
    int sum(float a, int b);
    int sum(int a, float b);
    int sum(float a, float b);

| EVERY single line of code you see up there, is allowed. This is how Overloading works.
| The reason why Overloading exists is so different inputs get you different outputs.
| Later you'd have to write the Definitions Code for every single one of those Function Declarations, and they could be the exact same, or slightly different. You can't make it so every single one of those Declarations goes into the same Definition.
| Here's how it would be used:

.. code-block:: c++
   :linenos:

    // Declarations done above
    int sum(int a, int b)
    {
        return a+b;
    }
    int sum(int a, int b, int c)
    {
	return a+b+c;
    }
    int sum(float a, float b)
    {
	return a+b;
    }

| Ok that float one should also have a Return Type of ``float`` but I kept it to ``int`` for the point of explaining.
| What this all allows us to do is to use the same function call, in this case ``sum()``, for multiple different scenarios, and depending on the Arguments entered, it would go into whichever one is suitable!
|
| ``sum(4, 5)`` would go into the first one.
| ``sum(4, 5, 6)`` would go into the second one.
| ``sum(4.4, 5.5)`` would go into the third one.
|
| And every single one of those is the same function name, which makes things much more convenient when calling the function.
