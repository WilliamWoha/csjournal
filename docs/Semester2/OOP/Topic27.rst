.. _s2-oop-t27:

27) Virtual Functions
---------------------

| This is where the fun begins.
|
| Make sure to read the previous page for context on what Virtual Functions exist for. We established that if you had a ``Base`` pointer or reference which was assigned a ``Derived`` class, it could only access the ``Base`` portion of that Derived Class, and we want to be able to call the ``Derived`` function instead. We do that through Virtual Functions.
|
| A Virtual Function is a special type of member function that, when called, finds the most-derived version of the function *that matches the Object Data Type*. This last part is important because a lot of people believe that ``virtual`` just applies to the start or the end.

.. code-block:: c++
   :linenos:

    class Base {
    protected:
        int value;
    public:
        Base(int a): value(a) {}
        virtual void printValue() {
            cout << "BASE - " << value << endl;
        }
    };
    class Derived1: public Base {
    public:
        Derived1(int a): Base(a) {}
        virtual void printValue() {
            cout << "DERIVED1 - " << value << endl;
        }
    };
    class Derived2: public Derived1 {
    public:
        Derived2(int a): Derived1(a) {}
        virtual void printValue() {
            cout << "DERIVED2 - " << value << endl;
        }
    };
    class Derived3: public Derived2 {
    public:
        Derived3(int a): Derived2(a) {}
        virtual void printValue() {
            cout << "DERIVED3 - " << value << endl;
        }
    };
    int main() {
        Base* ptr1 = new Derived1(5);
        ptr1->printValue();
        Base* ptr3 = new Derived3(15);
        ptr3->printValue();
        Base* ptr2 = new Derived2(10);
        ptr2->printValue();
        Base* ptr4 = new Base(20);
        ptr4->printValue();
    }

| This code will output:

.. code-block:: c++

    DERIVED1 - 5
    DERIVED3 - 15
    DERIVED2 - 10
    BASE - 20

| It does this through the use of something called a "Virtual Table". Don't bother with what that is unless you're confident in how everything works first.
|
| The way it works is, it tries to call a function, but if it has ``virtual`` written next to it, it tries to see if there's a Function Override for it which inherits further. If so, it goes to the next option. It keeps doing this until it is either at the end of the chain, or the object's data type matches. So for ``ptr1`` it only goes down to the ``printValue()`` for ``Derived1``, for ``ptr2`` it only goes down to ``Derived2``, and for ``ptr3`` it goes all the way down to ``Derived3``.
|
| If you add ``virtual`` to any level, then it would apply ``virtual`` to *all* other Child Classes with Override functions. The code above works the exact same if you remove ``virtual`` from all functions except the ``Base`` one, but if you remove it from there as well then it will just call ``Base::printValue()``. It's just good tradition to put ``virtual`` on all of them.
|
| Also, if you make an inheritance chain, ``Base <- Derived1 <- Derived2 <- Derived3``, it's important for the functions to be Overriding every step of the way. Otherwise it will stop at earlier points in the chain, unless there's a direct link. For example, in the code above, if you remove the Override for ``printValue()`` in ``Derived2``, then it prints this:

.. code-block:: c++

    DERIVED1 - 5
    DERIVED3 - 15
    DERIVED1 - 10
    BASE - 20

| If you try to call a virtual function through a member directly, it just calls its own member function.

.. code-block:: c++
   :linenos:

    Derived1 obj1(5);
    obj1.printValue();
    Derived2 obj2(10);
    obj2.printValue();

| Which is why this next part is important to remember:
|
| Virtual Function Resolution only works when a member function is called through a pointer or reference to an Object. And specifically when it's a Base pointer/reference to a Derived Object.
|
| Finally, returning to the word Polymorphism. Polymorphism means "Many Forms". In programming, this is done at two places:
*   Compile-time Polymorphism
*   Run-time Polymorphism
| Compile-time Polymorphism includes things like Function Overloading (``add(int, int)``, ``add(double, double)``, ``add(ComplexInt, ComplexInt)``), and Template Resolutions (Semester 3). This just means the Compiler will see and change forms as the code needs when it's compiled.
| 
| Run-time Polymorphism includes Virtual Function Resolution, which is what we've covered on this page. This is Polymorphism resolved at runtime, meaning the Compiler will check which form to take *while* the code is running.
|
| Now we'll wrap up on this.
|
| Under normal scenarios, the return type of ``virtual`` functions must match, or else the compiler will give an error. So in the example above, if you change one of the ``printValue()`` to something other than ``void``, it'll give an error.
|
| Don't call Virtual Functions from within Constructors and Destructors because first every class has to be made, *then* the ``virtual`` portion and the inheritance is checked. If you call it within a constructor, it's not complete yet. It just calls the base version.
|
| The downsides of Virtual Functions are that it takes longer to run compared to a regular function, and that in the Virtual Table, the compiler needs an extra pointer for each virtual function. It's not *that* big of a deal but if you're after absolute performance then it can make a difference.
|
| Also, learn about the ``override`` specifier through here: https://www.learncpp.com/cpp-tutorial/the-override-and-final-specifiers-and-covariant-return-types/. I wasn't taught this, and learnt it later. I could go into details about it, but this site teaches it better.