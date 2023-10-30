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
| One thing to keep in mind, an inherited class inherits *all* objects from the Base Class, even private ones, which are specifically designed to never be directly accessible outside of the class. Even though they're private, they're inherited, and the code expects you to use the Base Class's getters and setters, or whatever other function, to interact with it.

Class Access
^^^^^^^^^^^^

| We've already dealt with ``public`` and ``private`` Data Members and Member Functions (or Methods), and how ``public`` members make the data in question accessible to any other part of the code, while ``private`` restricts access and requires the use of ``getters`` and ``setters`` or other functions to interact with. One thing to keep in mind, this inheritance depends on *both* the Base Class and the Derived Class. It'll make sense soon. Here's how all of those specifiers work in the case of Inheritance:

Access Specifiers within the Class Definition
"""""""""""""""""""""""""""""""""""""""""""""

| For this specific scenario, we'll be assuming that the ``public`` specifier is used for Inheriting. This is the most common form of Inheritance. We'll be looking into other forms as well but you won't use them anywhere near as often as you use this.
|
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

| The thing to note about ``protected`` is that it stays as the type ``protected`` when you do Inheritance, instead of being turned into ``public``. This matters because if you do Inheritance on multiple levels, you can keep access to it.

.. code-block:: c++
   :linenos:

    class Base {
    protected:
        int x;
    };
    class Derived1: public Base {
    };
    class Derived2: protected Derived1 {
    };
    class Derived3: public Derived2 {
    public:
        void printX() {
            cout << "X: " << x << endl;
        }
        void setX(int x) {
            this->x = x;
        }
    };

Constructors and Destructors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Method Overriding
^^^^^^^^^^^^^^^^^

Single-Level, Multi-Level, and Multi-Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Diamond Problem
^^^^^^^^^^^^^^^^^^^

Virtual Inheritance
^^^^^^^^^^^^^^^^^^^
