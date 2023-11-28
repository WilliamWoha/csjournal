.. _s3-dsa-t02:

2) Function Templates
---------------------

| This is normally covered under OOP, but I guess our pace was slow so they're forced to cover this under Data Structures now. Templates aren't an actual Data Structure, and they have way more to do with Classes and Functions. It's only being written in Semester 3 because I myself am studying it in Semester 3.
|
| Templates come in two types: Function Templates, and Class Templates. They exist when we want to generalize code for multiple data types and reduce repetition.
|
| Consider the following example:

.. code-block:: c++
   :linenos:

    int max(int x, int y) {
        if(x > y)
            return x;
        else
            return y;
    }
    float max(float x, float y) {
        if(x > y)
            return x;
        else
            return y;
    }
    double max(double x, double y) {
        if(x > y)
            return x;
        else
            return y;
    }

| Three different function overloads for a function that does the exact same thing every single time. If you didn't look at the Function Arguments you wouldn't even notice that they're different pieces of code.
|
| Not only is the code repetitive, it's also extra work to manage. If these were functions to print the values of an array instead, and you wanted to change the outputs, so that instead of ``1 2 3 4 5`` it prints ``1, 2, 3, 4, 5``. You'd have to make the changes in the code for every single function overload. It's just a lot of work, and it's unnecessary.
|
| We want to reduce repeated code, and we want to make programs generic. In C++, generic programming is done through the use of templates. Templates are a Compile Time mechanism in which the Compiler generates different copies of the same body of code, with the only difference being the data type used. So with the three functions above, instead of having all these different functions for different data types, we can just use Templates to create one function, and the compiler will handle the rest depending on the data type used.
|
| In templates, we use what is called a ``placeholder`` data type. A ``placeholder`` data type represents a Data Type that is not known when the Template is written, but will be provided later.
|
| We call them ``templates`` because, just like the dictionary definition, the function or class acts like a template and can be used with different data types. The data type to use is determined when the template is *used* in the program, not when the template is written. This means template code can even be used for data types which don't even exist yet! This makes templatized code both flexible and futureproof.
|
| Templates can apply both to Functions and to Classes. Here's the syntax for a Function, to deal with our example given above:

.. code-block:: c++
   :linenos:

    template <typename T>
    T max(T x, T y) {
        if(x > y)
            return x;
        else
            return y;
    }

| Here, we're using the words ``template <typename T>`` to tell the Compiler that we're defining a Placeholder Variable named ``T`` which is *only* valid for the next Class or Function that follows. It won't have a valid scope beyond that. This means the ``template parameter declaration`` (which is the formal name for ``template <typename T>``) needs to be done for every single function that you want to generalize.
|
| You can also write ``template <class T>`` but ``typename`` is a newer word and is used more often.
|
| ``T`` doesn't need to have a complex name. It's tradition to just use ``T`` but you can have it be any name at all, just like a variable.
|
| Unfortunately, *using* the function isn't as simple as it would be in something like Python. Although the function is templatized now, you can't just do ``max(value1, value2)`` now. The Compiler needs to know what specific data type it has to define for ``T``, and it can't do so automatically.
|
| Originally, you used ``max(value1, value2)``. Now, since the function is templatized, you have to do ``max<data_type>(value1, value2)`` instead. An example has been written below.

.. code-block:: c++
   :linenos:

    template <typename T>
    T max(T x, T y) {
        if(x > y)
            return x;
        else
            return y;
    }
    int main() {
        cout << max<int>(5, 10) << endl;
        cout << max<float>(10.5, 5.3) << endl;
    }

| There is good news though. Sometimes, the Compiler *is* able to do ``max(value1, value2)`` if there's enough information for it to make a proper deduction on the data type. If you do ``max(5, 10)``, or ``max<>(5, 10)``, the compiler sees that an actual data type hasn't been provided, so it will attempt to deduce an actual data type from the *arguments* to see which function to generate. In this case, it sees that ``max<T>`` with arguments ``(int, int)`` would translate to ``max<int>(int, int)``. But it's better to just write ``max<int>`` instead as then you know which version is being generated.
|
| A template might not handle all data types correctly. In the example above what would happen if you sent ``max("Hello", "World")``? The code is valid, and it would compile, and may even give a result back, but it may not be what you want. You can specialize specific template portions by overloading the function in this way:

.. code-block:: c++
   :linenos:

    template <typename T>
    T max(T x, T y) {
        if(x > y)
            return x;
        else
            return y;
    }
    template <>
    const char* max<const char*>(const char* x, const char* y) {
        // Code to compare x and y, by whatever standards you wish.
    }

| This is also useful to know for a function which compares two classes but an operator overload for said class may not exist.
