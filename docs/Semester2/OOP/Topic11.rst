.. _s2-oop-t11:

11) Destructors
---------------

| Destructors, Arrays, Copy Constructors, Static Members, this->, Member Initializer List, Const Members, Const Objects, and Friend Functions. Once all that's covered, the basics of Classes will be complete, then beyond that there's enhancing classes (Operator Overloading), then concepts where Multiple Classes are involved and they interact with each other. Class Relationships, Inheritance, and Polymorphism. Then the semester ends. Fortunately, those concepts are simple in practice and don't involve too much explaining.
|
| At the time of writing, I've already completed every single one of those, finished the semester project, and it got announced as the Best Project out of the entire batch. It got noticed so much that I got offered an internship at a game company but I turned it down because it was unpaid and it was for pay-to-win mobile apps instead of proper cinematic experiences. For the Semester Project we had to build a space shooter game and I built one with multiple levels, custom sprite sheets and animations, and boss fights. It took multiple sleepless nights to do within the allocated time limit.
|
| The concepts themselves are simple once you understand them, the pages just get very long because I have to actually thoroughly explain them enough that it makes sense.
|
| Alright, that's enough monologuing. Time for Destructors.
|
| You can probably guess it based on the name alone and the previous experience with Constructors. A Destructor is a Function that's automatically called when an Object is Destroyed. By Destroyed, I mean it's no longer a variable for us to use. This happens in two situations:
*   When the ``delete`` keyword is called for an Object which was made in the Heap
*   When the Scope ends and an Object is destroyed automatically
| The first one is pretty simple. Here's an example:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 14, 15

    class Circle {
    private:
        float x;
        float y;
        float r;
    public:
        Circle(float x1 = 0, float y1 = 0, float r1 = 0) {
            x = x1; y = y1; r = r1;
        }
    };
    int main() {
        Circle* ptr = new Circle;
        Circle* ptr2 = new Circle[5];
        delete ptr;
        delete[] ptr2;
    }

| In lines 14 and 15, the ``delete`` keywords are being applied to the Heap Objects. They are being freed from memory. This automatically calls the Destructor. Here's the second scenario where the Destructor is called:

.. code-block:: c++
   :linenos:

    class Circle {
    private:
        float x;
        float y;
        float r;
    public:
        Circle(float x1 = 0, float y1 = 0, float r1 = 0) {
            x = x1; y = y1; r = r1;
        }
    };
    void func() {
        Circle c1;
    }
    int main() {
        func();
        func();
        func();
        Circle c2;
    }

| In this specific scenario there's 3 Circle Objects being made within the Scope of ``void func()``, and when that Scope (Meaning when the function) ends, the Object is being destroyed. In the overall code, however, there's four Destructors being called, because ``c2`` is being made in ``int main()``, and when ``int main()`` ends, that Object is also destroyed.
|
| So it's super similar to a Constructor where the function is called automatically, it has no return type, and it can have Out-Of-Line declaration. However it's super different in the sense that it's meant to 'Destruct' the object, it's only called when the Object is being destroyed, it can't take any parameters, and there can only be one Destructor. You also always want to set this to ``public``. Here's the syntax for it:

.. code-block:: c++
   :linenos:

    // In-Line Declaration
    public:
        ~Circle() {
            // Destructor Code
        }

    // Out-Of-Line Declaration
    public:
        ~Circle();

    Circle::~Circle() {
        // Destructor Code
    }

| This is super important whenever you're working with Dynamic Memory, because, just like the Constructor, if there's no Destructor code written the Compiler just makes it for you as ``~Circle() {}``. This works completely fine for all forms of Local Variables. If you're not working with the Heap, this is all you need. It's when you *are* working with the Heap that it becomes so important. Take a look at this:

.. code-block:: c++
   :linenos:

    class Array {
    private:
        int* ptr;
        int size;
    public:
        Array(int* pointer = nullptr, int s = 0) {ptr = pointer; size = s;}
        ~Array() {}
    };
    void func() {
        Array a1(new int[3], 3);
        // Some other code using a1
    }

| When that function ends, we're no longer using the Variables that were made in it. Whatever we were doing with it, let's say it's done. We did what we wanted to do. Now the Function has ended, and it must be destroyed to free up space. So it does its thing and removes the variables from memory, and it does the same to the ``a1`` object as well. But that's where the problem of the Default Destructor lies. All it does is free up *non-heap* members. In this case, that's ``ptr`` and the ``size``. The actual memory that the ``ptr`` is pointing to is NOT being cleared properly. There's no ``delete[]`` command being called for it, so it's causing a memory leak. This is why we have to customize the Destructor, so we can call that command and free up that memory.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 14

    class Array {
    private:
        int* ptr;
        int size;
    public:
        Array(int* pointer = nullptr, int s = 0) {ptr = pointer; size = 0; }
        ~Array() {
            if (ptr == nullptr)
                return;
            cout << "Destructor Called!" << endl;
            delete[] ptr;
        }
    };
    void func() {
        Array a1(new int[3000000], 3000000);
        // Some other code using a1
    }
    int main() {
        for (int i = 0; i < 10; i++)
            func();
    }

| For the code above, I happened to observe Memory Usage in Visual Studio through Heap Snapshots, both with Line 14 commented, and written. When commented, each iteration of the loop added 12 Megabytes of data to the Heap, and at the end of it, 117 Megabytes were allocated. The leak just kept increasing. If there was more data this could very easily go into the Gigabytes range, and you'd think nobody's crazy enough to make an Array of size 3 Million but have you ever thought about how much data is in a single image? Every single individual pixel has coordinate and RGB Values, and there's millions of pixels in just one image. Just the presence of ``delete[] ptr`` in Line 14 in the Destructor is what saved that Memory Leak from happening, and made it so only 58 Kilobytes were used at the end of it, since all of it was cleared.
|
| If you're confused about having to only delete the ``ptr`` and not the ``size``, that's because it's handled automatically. I only recently found out that local variables are formally called ``Automatic Variables``. It's allocated and de-allocated automatically when it enters and leaves the Scope. We only have to do this for non-Automatic Variables. I already knew that, I just didn't know they were called Automatic Variables. Also I'll just call them local variables instead because it's way more familiar.
|
| Lastly I just want to mention that the order in which the Destructor is called (if there's multiple Objects) is the reverse of the order in which it was created.

.. code-block:: c++
   :linenos:

    int main() {
        Circle c1;
        Circle c2;
        Circle c3;
    }

| For Constructors, the order would be ``c1 > c2 > c3``, and for Destructors, it would be ``c3 > c2 > c1``. I bring this up because my uni has asked questions before on which destructor would be called when, and this isn't too much to worry about now but it's a crucial thing to focus on later when doing Inheritance. And another thing I forgot to mention: Global Scope Objects will have their constructors be called before any other function, including ``int main()``, and will have their destructors be called when ``int main()`` ends. Local Scope Objects will have their Constructors be called when they're created within a Scope, and their Destructors will be called when they exit a scope. My uni gave me some curveball questions testing this by having both Global and Local objects with ``cout`` statements then asking what the output would be. Experiment around with this.