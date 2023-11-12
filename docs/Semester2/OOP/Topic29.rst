.. _s2-oop-t29:

29) Abstract Classes and Pure Virtual Functions
-----------------------------------------------

| This is it. This is the end. The final chapter. And yes, I know, there's other things as well such as ``dynamic_cast`` but they're optional. You can look into that yourself on ``learncpp``. I think my university doesn't teach it because they said we're trying to get the hand of how to use a language in the first year, and then in later years we'll do more "Computer Science" stuff, like Data Structures and OS construction, which can be done through any language.
|
| On the previous pages we established how a Virtual Function works and how Polymorphism allows pointers and reference variables to execute functions that belong to derived classes, which lets code be generalized. We can take this a step further using Pure Virtual Functions. The concept is simple, it's just Virtual Functions except it exists specifically to make the Base class into a blueprint.
|
| Say for example, we have a ``Shape`` class, and we inherit from that to make ``Circle``, ``Rectangle``, ``Triangle``, ``Octagon``, and so on. We can use these classes to make objects however we want. The only extra thing we want to do here, is forbid the programmer from making an object of the ``Shape`` class. Meaning, we *only* want ``Shape`` to be used for Inheritance, and not for actual Objects being made.
|
| One way to do this would be to have the Constructor of the ``Shape`` class be protected, but there's a second, more easier way to do this: Pure Virtual Functions.

.. code-block:: c++
   :linenos:

    class Base {
    public:
        virtual string function1() { // Regular virtual function
            return "SHAPE";
        }
        int function2() { // Regular function
            cout << "FUNCTION2" << endl;
            return 5;
        }
        virtual float function3() = 0; // Pure Virtual Function
        char function4() = 0; // Compile Error, Pure functions MUST be virtual.
    };

| A Pure Virtual Function is basically a way to say, "This entire class exists ONLY to be inherited from, and the implementation of this function will be done by the derived classes." Focus on the wording here, *"This entire CLASS"*. If any class has a single Pure Virtual Function, then it becomes an Abstract Class, and the compiler will *NOT* let you make *ANY* objects of it. This also means, if you derive from this function, you *HAVE* to give that function a definition, or else that class also becomes an Abstract Class, and you can't make any objects for it.

.. code-block:: c++
   :linenos:

    class Character {
    private:
        string name;
        float health;
        int charNumber;
        // Whatever else is relevant
    public:
        virtual void punch() = 0;
        virtual void kick() = 0;
        virtual void moveLeft() = 0;
        virtual void moveRight() = 0;
        virtual void jump() = 0;
        virtual void crouch() = 0;
    }
    class Bob: public Character {
    public:
        virtual void punch() {
            // Code for Bob to punch
        }
        virtual void kick() {
            // Code for Bob to kick
        }
        virtual void moveLeft() {
            // Code for Bob to move left
        }
        virtual void moveRight() {
            // Code for Bob to move right
        }
        virtual void jump() {
            // Code for Bob to jump
        }
        virtual void crouch() {
            // Code for Bob to crouch
        }
    }    
    class Panda: public Character {
    public:
        virtual void punch() {
            // Code for Panda to punch
        }
        virtual void kick() {
            // Code for Panda to kick
        }
        virtual void moveLeft() {
            // Code for Panda to move left
        }
        virtual void moveRight() {
            // Code for Panda to move right
        }
        virtual void jump() {
            // Code for Panda to jump
        }
        virtual void crouch() {
            // Code for Panda to crouch
        }
    }

| Now you can just use one ``Character*`` pointer and use that to do something like ``Character->punch()`` or ``Character->kick()`` and everything will work like you want it to. Really the only extra pieces of code you'd be dealing with would be for the declaration of ``Character``'s data type, but once that's done you're reducing the code way more. And even that part is handled by one 'list' that does the mapping for you.

.. code-block:: c++
   :linenos:

    Character* assignCharacter(int selection) {
        switch (selection) {
            case 1:
                return new Bob;
            case 2:
                return new Panda;
            case 3:
                return new Akuma;
            // Add more cases for other characters as needed
            default:
                return nullptr;
        }
    }
    int main() {
        int selection = -1;
        cout << "Select Character: ";
        cin >> selection;
        Character* player = assignCharacter(selection);
    }

| Also remember to put a ``virtual`` behind the destructor for the Base Class.
|
| That's it. You've finished OOP. See you in Semester 3!