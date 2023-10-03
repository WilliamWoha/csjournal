.. _s2-oop-t22:

22) Conversion between Data Types
---------------------------------

| We'll be overloading the Typecast operators now. Super rare to use but in case you needed the option, it's there.
|
| If you're converting from an existing data type into your custom one, you just make it so the Constructor accepts that existing data type in a Constructor Call, and that's it.
|
| Converting from your custom data type back into a native one or a different one is where the magic happens. Here's an example:

.. code-block:: c++
   :linenos:

    int a = 5.5;

| See, even though we're not doing a typecast directly, it's doing so automatically. The line above is the exact same as writing this:

.. code-block:: c++
   :linenos:

    int a = int(5.5);

| The compiler recognizes the syntax and automatically does the conversion. But that's something we call 'implicit' conversion. If we want to force something, or provide a different conversion first, we use 'explicit' conversion, which is where we mention what we're converting to. Here's the syntax for it:

.. code-block:: c++
   :linenos:

    public:
        operator int() {
	    // Stuff
	    return value;
	}
	operator float() {
	    // Stuff
	    return value;
	}

| This function does not need a return type. Conversion functions don't have arguments, and the return type is defined as the conversion type automatically. However you want to do the conversion depends on you, but be mindful of what you're returning and what it represents. If it's not immediately readable, you're better off either not implementing this if it doesn't make sense, or implementing it as a function instead. And also, you can only return the data type you're converting to. Doing ``float(set)`` for example, won't return a set where all the values are converted to float. It returns a singular float number, and if that number doesn't mean anything, then the operator has no reason to exist.
|
| You can use the same syntax to convert one Class to another, if needed. But you can try that yourself, I have *never* used it and I don't think anyone will need to either. It's very, very niche.
|
| That ends Operator Overloading. Now, there's just Class Relationships (Association, Aggregation, Composition), Inheritance, and Polymorphism left. We're reaching the end.