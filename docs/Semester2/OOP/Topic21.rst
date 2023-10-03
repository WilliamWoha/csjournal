.. _s2-oop-t21:

21) Overloading Default Data Types
----------------------------------

| This is just a more in-depth explanation of overloading operators in a way that lets you use them with other data types, but externally. I showed on the previous page the overloading of ``operator>>`` and ``operator<<`` for input and output using ``cin`` and ``cout``, and that you can implement the operator overload externally as well.

.. code-block:: c++
   :linenos:

    ComplexInt operator+(const ComplexInt& a, const ComplexInt& b) {
        ComplexInt temp;
        temp.setReal(a.getReal() + b.getReal());
        temp.setImag(a.getImag() + b.getImag());
        return temp;
    }

| You might be wondering what the advantage of implementing it externally is compared to writing it as a Member Function. Well it serves a lot of purposes, actually. The first, is that this is the *only* way to overload the Default Data Types of C++, such as ``float``, ``int``, ``char``, ``bool``, etc. On the previous page I showed an example of overloading ``operator+`` so it could also accept ``int`` as an argument. When you do ``c1 + 5`` it does ``c1.operator+(5)`` and runs code. The challenge with this, is doing it the other way around. Writing ``(c1 + 5)`` is fine, but if you write ``(5 + c1)`` it gives an error, because it's trying to run ``int.operator+(c1)``, which doesn't exist, because we haven't implemented any overloads within the ``int`` Class. I don't actually know if ``int`` is a class or not but in this case we're treating it like one. What we can do instead, is implement the operator overload externally to deal with this situation.

.. code-block:: c++
   :linenos:

    ComplexInt operator+(int a, const ComplexInt& b) {
        ComplexInt temp;
        temp.setReal(a + b.getReal());
        temp.setImag(0 + b.getImag());
        return temp;
    }

| And that's it! Now you can write ``(5 + c1)`` and get a ``ComplexInt`` in return. This further lets you do chaining, such as doing ``(5 + c1) * c4``.
|
| This only works, however, if the Object in question has functions to let you implement functionality like this. In the case of our ComplexInt ``b``, it had getters to obtain the values, and for ``temp``, it had setters to set new values. If these aren't available for the class, or they're private, then the only way to implement functionality like this is to make the function a friend function. In that situation you can access private members of the class like you belonged there.


.. code-block:: c++
   :linenos:

    class ComplexInt {
    private:
        // Stuff
    public:
        // Stuff
        friend ComplexInt operator+(int a, const ComplexInt& b);
    }

    ComplexInt operator+(int a, const ComplexInt& b) {
        ComplexInt temp;
        temp.real = a + b.real;
        temp.imag = b.imag;
        return temp;
    }

| It depends on the data you're working with. You can choose to implement it however you want. You can even completely ignore this and just remember to not write the code in a format that is invalid, though if you're making a Class general purpose and to be used by yourself or other people in the future you'll want to implement additional functionality. It's just good practice to do so. This is also the technique to use for implementing compatibility with *any* custom class.
|
| As far as I know, currently, there's no way to change the Data Type you're returning. Having the name and arguments be the same but the return type be different doesn't trigger an overload, as an overload is only triggered when the compiler can differentiate when to go into which function. So you're stuck with this limitation. As of typing, I don't currently know a way around this limit. I'll update the page if anything comes up.