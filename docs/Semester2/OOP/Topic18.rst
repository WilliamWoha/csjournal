.. _s2-oop-t18:

18) Friend Functions
--------------------

| See, this one requires a proper explanation because it's kind of hard for it to make sense without practical examples. Friend Functions are functions that can access the Private members of a class without actually belonging to a class itself. In other words, the function is treated as if it were a member of the class. This is different from regular Member Functions because those *do* belong to the class. Member Functions require an existing object to be called, or if the function is static, then it needs to be called from the Class Name, but regular functions don't experience that challenge. It also makes it much, much easier to access private members if a function is too complicated or long or not worth the hassle of implementing directly into the class itself. 
|
| What you're basically doing with a friend function is giving a key to an already existing regular function, and using that key it can access the private data members of the class.
|
| A friend function can be a stand-alone function, or a member of another class, or even an entire class. Here's how you write it:

.. code-block:: c++
   :linenos:

    class Class {
        // Data Members
    public:
        // Member Functions
        friend returnType function(arguments);
    };

    returnType function(arguments);

| Friend functions should be used for limited use cases, or else too many functions with access to private data lessens the value of the Encapsulation and Data Hiding. The page is short for now but they're going to return. They're especially useful in Operator Overloading for integrating specific functionalities into Classes, such as being able to do ``cout << object << endl;`` by causing the ``ostream`` and ``istream`` insertion and extraction operators to be Friends.