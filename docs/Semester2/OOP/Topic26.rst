.. _s2-oop-t26:

26) Intro to Polymorphism
-------------------------

| I'd put a joke here or a pun but there's not much to say. Message me one on Discord or something if a good one comes to mind.
|
| Polymorphism comes from the word "Polymorph", and it's made from the Greek Words "Poly" meaning Many, and "Morph" meaning forms. That should be enough to explain that Polymorphism means "Taking on many forms".
|
| In C++ this is an extremely powerful tool because it lets you have extremely reusable and extensible code.
|
| Before we can get into how to actually use it, we need to dive into how pointers and reference variables interact with Base and Derived Classes.

.. code-block:: c++
   :linenos:
    
    class Base {
    protected:
        int value;
    public:
        Base(int a): value(a) {}
        void printValue() {
            cout << "BASE - " << value << endl;
        }
    };
    class Derived: public Base {
    public:
        Derived(int a): Base(a) {}
        void printValue() {
            cout << "DERIVED - " << value << endl;
        }
    };
    int main() {
        Derived thing(5);
        Derived& thing2 = thing;
        Derived* thing3 = &thing;
        thing.printValue();
        thing2.printValue();
        thing3->printValue();
    }

| If you run the code, it'll output this:

.. code-block::

    DERIVED - 5
    DERIVED - 5
    DERIVED - 5
    
This is normal, it works like regular variables and Objects. This however, get more interesting if we make *Base* Pointers and Reference Variables instead.

.. code-block:: c++
   :linenos:

    int main() {
        Derived thing(5);
        Base& thing2 = thing;
        Base* thing3 = &thing;
        thing.printValue();
        thing2.printValue();
        thing3->printValue();
    }

| If you run this code, it'll output this:

.. code-block::

    DERIVED - 5
    BASE - 5
    BASE - 5

| Which is different from the above output. This is because ``thing2`` and ``thing3`` are declared as *Base* Reference and *Base* Pointer respectively. Although the code runs, both of them can only see the Base part of the Derived Class. This also means you can't actually do ``thing2.Derived::printValue()``. They can't see the Derived Portion. It's like it doesn't exist for them.
|
| You might be wondering what the purpose of this is. Why should we should bother with having ``Base`` pointers and references if we can just declare a ``Derived`` variable directly?
|
| Imagine a base class, ``Animal`` and many Derived Classes of this, such as ``Cat`` and ``Dog``. Now consider this piece of code:

.. code-block:: c++
   :linenos:

    string Cat::speak() {
        return "Meow";
    }
    string Dog::speak() {
        return "Woof";
    }
    string Cat::speak() {
        return "Caw";
    }
    void Speak(const Cat& cat) {
        cout << cat.getName() << " says " << cat.speak() << endl;
    }
    void Speak(const Dog& dog) {
        cout << dog.getName() << " says " << dog.speak() << endl;
    }
    void Speak(const Crow& crow) {
        cout << crow.getName() << " says " << crow.speak() << endl;
    }

| If you had many other classes, you'd have to repeat that code. And if the functions were bigger, this would get way bigger and way more complicated, and most importantly, *redundant*. It's repeated code, and it's pointless.
|
| Now look at this:

.. code-block:: c++
   :linenos:

    string Animal::speak() {
        return "";
    }
    void Speak(const Animal& animal) {
        cout << animal.getName() << " says " << animal.speak() << endl;
    }

| We've reduced, what is *thousands* of lines of repetitive code, to less than a page, because instead of writing individual functions for every single animal, we just generalized the code and let the compiler handle it. And here's the great thing about Polymorphism and why it's so powerful:
|
| You can send Derived Classes into functions which take Base Classes as arguments.
|
| There's a small challenge with this, as you might expect. As we saw earlier in the page, if we do ``base->function()`` then it can only see until the base function's members. It'll call ``Animal::speak()``. In this case, if we have ``cat.speak()`` return ``"Meow"``, or ``dog.speak()`` return ``"Woof"``, and have ``animal.speak()`` return ``""`` (no sound because we don't know what it speaks), then it wouldn't output the correct lines.
|
| One solution to this is to have a Data Member which stores the sound, initialize it for each Object, then to call on that Data Member. But this can be expensive on memory. So we'll do it with something better: Virtual Functions.