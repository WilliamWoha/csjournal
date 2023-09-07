.. _s2-oop-t09:

9) More about Classes
---------------------

| The general rule of thumb is to keep Data Members private and to keep Functions public. Also, you can write ``public:`` and ``private:`` multiple times throughout the Class Definition, there's no order or anything to them, and even though by default the members are Private, it's still better to mention ``private:`` at the start of the Class as good practice.
|
| Everything written on the previous pages about Structures, including the Pointers, and Member Functions, all applies to Classes as well. Just practice those and you'll be set. So we'll be moving onto more details about how Classes work.

More about Member Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

| You've done Member Functions in Structures already. They're functions defined inside of the Structure with access to the variables which belong to the Structure. In classes, they do the same thing, but this time we're also working with Access Specifiers (Meaning we can set functions to public and private), and there's another feature: Out Of Line Declaration.

Functions and Access Specifiers
"""""""""""""""""""""""""""""""

| So similar to how we can set anything below a ``public:`` statement to be easily accessible outside the Class definition and anything below a ``private:`` statement to be inaccessible outside the Class for Member Variables, we can do the same for Member Functions. The general rule of thumb is to have the Member Variables be private and the Member Functions be public, like how on the previous page I demonstrated an example of having Getters and Setters. But you can still set functions to be private as well, it would just be a very specific use case. If a Member Function is set to Private then it can be called *only from within* the Class definition itself. You can use this for yourself however you please. The most common use case is to have multiple functions for updating specific values or doing specific task, and setting them to Private, and then having a public function that lets all of them be called and do the calculations later. It's upto you. At the time of writing I don't have any examples of it.

Out Of Line Function Declaration
""""""""""""""""""""""""""""""""

| This is a fun one, because this is where a lot of chaos and headaches begin for people who aren't used to using external files. I'll probably have to explain that...somehow. It varies from IDE to IDE and Compiler to Compiler. We'll come to that later, for now we'll get into what it is and why it's important.
|
| There's a way to write Functions outside of the Class they were declared in. If you remember Function Prototyping way back in Semester 1, where you wrote a Function's declaration in the start of the program and then wrote that Function's definition at the end of it, this is basically the Member Function equivalent of that. I don't actually remember if I mentioned it on that page so whether I did or didn't, but I'll still say it here: Function Prototyping is important because it lets you have multiple functions interact and be nested within each other without concern for order, since all of them are declared in advance.
|
| In the case of Classes, that same importance exists, but it just also helps to make things cleaner and more readable.
|
| In this specific situation, if a function's definition (or code) is written directly where it's declared, meaning within the Class itself, it's called an in-line declaration. If only the function's declaration is present there and the definition (or code) is written outside the Class itself, that's called an out-of-line declaration. In the code ahead, I've made it so the Getters are written as in-line and Setters are written as out-of-line, just to showcase both. You can use both, it's just a stylistic choice. But the better practice is to use out-of-line definitions because of the reasons defined above.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 6,9,12,13,16,19

    class Rectangle {
    private:
        double width;
        double length;
    public:
        double getLength() {
            return length;
        }
        double getWidth() {
            return width;
        }
        void setLength(double l);
        void setWidth(double w);
    };

    void Rectangle::setLength(double l) {
        length = l;
    }
    void Rectangle::setWidth(double w) {
        width = w; 
    }

| The way this works is the same way Function Prototyping and Function Definition works, except for one key difference: ``Rectangle::``. If we don't mention that specific keyword, the code will just think we're writing a regular function. ``Rectangle`` is the class we want to access, and the ``::`` operator is defined as the Scope Resolution Operator. We're using this operator to access the Class without being present between the {Curly Brackets} that define it. Writing ``Rectangle::`` is NECESSARY for the compiler to recognize that the function in question is the definition of a Member function instead of a regular function, and that it's specifically a Member Function of the ``Rectangle`` Class. The proper syntax is this:

.. code-block:: c++

    class ClassName {
        ReturnType Function1();
        ReturnType Function2();
    };
    
    ReturnType ClassName::Function() {
        // Code
        return ReturnType;
    }
    ReturnType ClassName::Function2() {
        // Code
        return ReturnType;
    }

| Using the Scope Resolution operator is what allows you to write the behaviour of a function later, and having all the functions defined at once. This works for both Public and Private Member Functions.

Const Functions
"""""""""""""""

| In some cases you want to define functions but want to explicitly make sure that they don't affect your existing values in any way at all. In shorter words, making them read-only. There's an easy way to do that, which is to set them as ``const``. This is only possible with Member Functions, and you want to make a habit of doing this when making getters or anything else read-only, as it's gonna happen for larger scale code and you don't want things to be changed.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 5,9

    class Rectangle {
    private:
        double width;
    public:
        double getWidth() const;
        void setWidth(double w);
    };

    double Rectangle::getWidth() const {
        return width;
    }
    void Rectangle::setWidth(double w) {
        width = w; 
    }

| It's important to note that you have to write ``const`` for both the in-line and out-of-line definitions, or else they'll be considered two different functions entirely. ``double getWidth() const;`` would be treated as its own separate function compared to ``double getWidth()``, despite having the same name, return type, and arguments. The reason for this is that there's a *very* niche use case where if you have two functions of the exact same name and arguments, differing by the presence of ``const`` (return type doesn't matter), having an Object be a const will call that const function, while having a regular object will call that regular function.

.. code-block:: c++
   :linenos:

    class Rectangle {
    public:
        double width;
        double getWidth() const;
        double getWidth();
    };
    double Rectangle::getWidth() const {
        cout << "I'm in const!" << endl;
        return width;
    }
    double Rectangle::getWidth() {
        cout << "I'm not in const!" << endl;
        return width;
    }

    int main()
    {
        const Rectangle r1 = { 4 };
        Rectangle r2 = { 5 };
        cout << r1.getWidth() << endl;
        cout << "=============" << endl;
        cout << r2.getWidth() << endl;
    }

| You'll see what I mean if you run that code above. Alright, that's enough for now. We move on to Constructors next, which is where things get more interesting for Classes.