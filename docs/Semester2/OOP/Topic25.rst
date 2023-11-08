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

| Constructors and Destructors of the Base Class are NOT inherited. Derived Classes have their own Constructors and Destructors. When an object of a Derived Class is created, first the Base Class's constructor is called, and after it's made, the Derived Class's constructor is called.
|
| The destructor works in the reverse manner of the Constructor. The constructor goes from Base to Derived, but the Destructor is first called for the Derived Class, then for the Base Class.
|
| The Base Class's Constructor and Destructor are *always* called when an Object of a Derived Class is created or destroyed.

.. code-block:: c++
   :linenos:

    class Base {
    public:
        Base() {
            cout << "Base Constructor Called." << endl;
        }
        Base(int a) {
            cout << "Parameterized Constructor Called." << endl;
        }
        ~Base() {
            cout << "Base Destructor Called." << endl;
        }
    };
    class Derived: Base {
    public:
        Derived() {
            cout << "Derived Constructor Called." << endl;
        }
        ~Derived() {
            cout << "Derived Destructor Called." << endl;
        }
    };
    int main() {
        Derived obj;
        cout << endl;
    }

| Run that and you'll see the pattern.
|
| You can pass arguments to a Base Class Constructor as well, which is the reason I wrote a Parameterized Constructor for ``Base`` above. You have to specify the arguments on the heading of the Derived Constructor.

.. code-block:: c++
   :linenos:

    class Rectangle {
    public:
        float side1;
        float side2;
        Rectangle() {
            side1 = 0;
            side2 = 0;
        }
        Rectangle(float side1, float side2) {
            this->side1 = side1;
            this->side2 = side2;
        }
    };
    
    class Square : public Rectangle {
    public:
        Square(int side) : Rectangle(side, side) {}
        Square() {}
    };
    
    int main() {
        Square obj(5);
        cout << obj.side1 << ", " << obj.side2 << endl;
        Square obj2;
        cout << obj2.side1 << ", " << obj2.side2 << endl;
    }

| This is useful because it allows you to choose which Constructor to call from the Derived Class. You could run the default one, or modify arguments or make your own arguments and call it. Keep in mind, however, if you're calling the Base Constructor of your choice you MUST do it via the Member-Initializer list. It can't be called otherwise. Or, well, it'll be called but it won't modify the actual values of your Object.

.. code-block:: c++

    Square(int side) {
        Rectangle(side, side)
    }

| This will work. But if you output the values of ``side1`` and ``side2``, it'll give 0 and 0. It didn't modify the actual values of the ``Square`` class during the Construction.

Method Overriding
^^^^^^^^^^^^^^^^^

| Method Overriding (or Function Overriding) lets you replace functions that belong to a Base Class. This is a situation where we're trying to have a Derived Class have its own functionality with the same function compared to the Base Class. On the end of the previous page I explained how instead of having ``BobPunch()`` or ``PandaKick()`` you can just have the same function of ``Punch()`` or ``Kick()`` do different things depending on which Object is calling it. This is how it's done. We'll go into detail with this example later when doing ``Polymorphism`` because we'll also have dealt with Abstract Classes by then. For now, we'll keep to a much simpler example.

.. code-block:: c++
   :linenos:

    class Base {
    public:
        void print() {
            cout << "From Base." << endl;
        }
        void print2() {
            cout << "From Base (Print2)" << endl;
        }
    };
    class Derived: public Base {
    public:
        void print() {
            cout << "From Derived." << endl;
        }
    };
    int main() {
        Derived obj;
        obj.print();
        obj.print2();
        obj.Base::print();
    }

| Method Overriding works in kind of the opposite way of Method Overloading. In Method Overloading, you're changing the ``Signature`` of the function (meaning the Data Types in its arguments) so it can be called with the same name but different arguments. Here, you're changing what the function is actually doing, while keeping the same name and same arguments. As shown above, even though we called ``obj.print()``, it calls the ``print()`` that belongs to ``Derived``, and *only* that function. It doesn't even consider the ``print()`` that exists in ``Base``, unless we explicitly tell it to call that function using ``obj.Base::print()``. I wrote ``obj.print2()`` as another sample function, it doesn't really do anything here.
|
| This is going to matter *tremendously* in Polymorphism, but it's too much to cover for now. Just understand that Function Overriding will make the Derived class call its own code, but it can still call the code of the Base if you use ``Base::`` to access it.

Single-Level, Multi-Level, and Multi-Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| There's three types of Inheritance: 
*   Single Inheritance
*   Multi-level Inheritance
*   Multi-Inheritance

.. code-block:: c++
   :linenos:

    class CommunityMember {
    };
    class Employee: public CommunityMember {
    };
    class Student: public CommunityMember {
    };
    class Alumnus: public CommunityMember {
    };
    class Faculty: public Employee {
    };
    class Staff: public Employee {
    };
    class Administrator: public Faculty {
    };
    class Teacher: public Faculty {
    };
    class AdministratorTeacher: public Administrator, public Teacher {
    };

| Here's a UML Diagram presenting this scenario:
|
.. raw:: html
    :file: images/inheritance_2.svg
|
*   ``Employee``, ``Student``, and ``Alumnus`` are Single-Inheritance
*   ``Faculty``, ``Staff``, ``Administrator``, and ``Teacher`` are Multi-Level Inheritance
*   ``AdministratorTeacher`` is Multi-Inheritance
|
| Single-Inheritance is what we've been dealing with this whole time. One Base Class, and one Derived Class.
|
| Multi-Level Inheritance is just extending the chain. There's a Base Class, then there's a Derived Class. This Derived Class in Multi-Level inheritance acts as the base class, for another Derived Class. It follows the same rules as Single-Level Inheritance. Another example for this can be with a class ``Coordinate``, which is inherited by a class ``Line``, which is inherited by a class ``Polygon``. It can go as long as you need it to or as short as you need it to.
|
| Multi-Inheritance is where things get interesting. It's not used that often but still exists for a reason. Here's how it works:

The Diamond Problem
^^^^^^^^^^^^^^^^^^^

Virtual Inheritance
^^^^^^^^^^^^^^^^^^^
