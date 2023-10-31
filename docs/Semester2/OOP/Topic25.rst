.. _s2-oop-t25:

25) All About Inheritance
-------------------------

| Now that we've established what Inheritance is from the previous page, we learn here how to actually use and implement it.

.. code-block:: c++
   :linenos:

    class Shape { // Base Class
        // Code
    };
    class Circle: public Shape { // Derived Class
        // Code
    };

| All data members and member functions of the base class are inherited by the derived class, with the exception of Constructors, Destructors, and the ``=`` operator, unless it's overloaded. The Derived Class (or Child Class) "inherits" functionality from the Base Class (or Parent Class). Here's an example:

.. code-block:: c++
   :linenos:

    class Animal {
    public:
        void eat() {
            cout << "I can eat!" << endl;
        }
        void sleep() {
            cout << "I can sleep!" << endl;
        }
    };
    class Dog: public Animal {
    public:
        void bark() {
            cout << "I can bark!" << endl;
        }
    };
    int main() {
        Dog dog1;
        // Base Class Functions
        dog1.eat();
        dog1.sleep();
        // Derived Class Functions
        dog1.bark();
    }

| The line ``class Derived: public Base {`` is what tells the compiler to carry out Inheritance here. It's inheriting from the class ``Animal`` with the ``public`` access specifier. This can also be set to ``private`` and ``protected``, and we'll look at all three of those below. ``protected`` is a new one as it's exclusively used for Inheritance.
|
| One thing to keep in mind, Inheritance doesn't exactly work by making copies. It relies on the existence of the Base class. If the Base class had Data Members in it, then the Derived Class doesn't just make a replica of those, it instead first makes a Base Class by calling its constructor, then follows rules to access those Data Members. For this reason, as you'll see ahead, if a Data Member is set to Private in the Base class, it's inaccessible even to the Derived Class, and that Derived Class also has to use Getters and Setters to access it.

Class Access
^^^^^^^^^^^^

| We've already dealt with ``public`` and ``private`` Data Members and Member Functions (or Methods), and how ``public`` members make the data in question accessible to any other part of the code, while ``private`` restricts access and requires the use of ``getters`` and ``setters`` or other functions to interact with. One thing to keep in mind, this inheritance depends on *both* how the Base Class declares it, and how the Derived Class inherits it. It'll make sense soon. Here's how all of those specifiers work in the case of Inheritance:

Access Specifiers within the Class Definition
"""""""""""""""""""""""""""""""""""""""""""""

| For any member in the Base Class, be it a Data Member or Member Function:
*   If it is defined as ``public``, then the Derived Class also declares them as public. As an example, if we have a public ``int`` in the Base Class, then the Derived Class will inherit that ``int``, and since the access specifier is set to public, that ``int`` will be publicly accessible. The Base Class has direct access to it, the Derived Class has direct access to it, and Objects have direct access to it.
*   If the member is defined as ``private``, however, then that data will remain ``private``, no matter what. Derived Classes do NOT have direct access to the ``private`` members of the Base classes. They have to use other functions, such as getters and setters, to interact with them. If a class sets something as private, it's completely off limits to every other part of the code except the Class itself and Friend functions.
*   If the member is defined as ``protected``, then the data will be accessible for the derived class, but only for the derived class. Objects won't have direct access. It's a mix of Public and Private.

.. code-block:: c++
   :linenos:

    class Base {
    public:
        int x;
    protected:
        int y;
    private:
        int z;
    };

    class PublicDerived: public Base {
    // x is public
    // y is protected
    // z is not accessible from PublicDerived
    };

    class ProtectedDerived: protected Base {
    // x is protected
    // y is protected
    // z is not accessible from ProtectedDerived
    };

    class PrivateDerived: private Base {
    // x is private
    // y is private
    // z is not accessible from PrivateDerived
    };

| That code above should be enough to explain all of the scenarios. Read through it thoroughly. You'll notice that if you inherit a ``public`` member as ``protected``, it'll just become ``protected``. Once it becomes ``protected`` you can't turn it back into ``public``. It's a non-reversible change unless you change the way the Derived Class inherits the member altogether.
|
| In most cases you'll just be inheriting in ``public`` form and defining the Access within the Base Class, as it's more readable, and more secure, because if you want to perform Data Hiding but have set your members to ``protected``, other parts of the code could just inherit it and have direct access. That's why ``public`` and ``private`` are still the preferred option. Just keep to this tradition of inheriting with ``public`` unless you know what you're doing.

Constructors and Destructors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

Method Overriding
^^^^^^^^^^^^^^^^^

Single-Level, Multi-Level, and Multi-Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Diamond Problem
^^^^^^^^^^^^^^^^^^^

Virtual Inheritance
^^^^^^^^^^^^^^^^^^^
