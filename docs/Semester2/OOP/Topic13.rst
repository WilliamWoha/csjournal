.. _s2-oop-t13:

13) Copy Constructors
---------------------

| This'll be fun. It's super simple in concept, until we get to the Heap.
|
| In :ref:`s2-oop-t07`, I mentioned that two Structures that have Pointers as Data Members will end up pointing to the same location in the Heap if we run the following code:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 14

    struct Array {
        int* ptr;
        int size;
    };
    int main() {
        Array a1 = {new int[5], 5};
        for(int i = 0; i < 5; i++)
            a1.ptr[i] = i+1;

        Array a2 = {new int[10], 10};
        for(int i = 0; i < 10; i++)
            a2.ptr[i] = i+1;
        
        Array a3 = a1;
    }

| We solve that today using the Copy Constructor. First I have to explain how the ``=`` operator, which we call the Assignment Operator, even works. It first sees if the left side can accept the Data Type provided on the right side, and if it passes that check, sets the values to be equal. In the case of Classes, it does 'Member Wise' assignment, which just means every member of the object on the left is given the values of every member of the object on the right. We've already covered this. The part that we didn't actually cover was how to avoid two Pointers belonging to classes pointing to the same location in Heap. We'll solve that using the Copy Constructor.
|
| The Copy Constructor is a Constructor used specifically to create a second object from an existing first object. However, like other Constructors, it can be modified to suit our needs. Here's the syntax for it:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 8

    class Circle {
    private:
        float x;
        float y;
        float r;
    public:
        Circle(float x1 = 0, float y1 = 0, float r1 = 0) {x = x1; y = y1; r = r1;}
        Circle(const Circle& copy) {
            // Copy Constructor Code
        }
    
| I wrote the Default Constructor there as well to give an idea. It's really just a Constructor where the Object is the Argument. And just like default Constructors, if a class doesn't have a Copy Constructor written by the programmer, it's written by the program directly. But one crucial piece of information to remember: The Copy Constructor is called for *any* function which passes an Object by value. This means if you do ``function(Circle copy)`` for any function, then it calls the copy constructor and doesn't modify the original value. The problem with this? If you use that same syntax for the Copy Constructor itself, it keeps calling itself, and becomes stuck in a recursive infinite loop. Passing by reference means you're not calling a constructor. But, since we don't want the original value to be modified, we also attach a ``const`` in the start of it. Make that a habit now, you'll see me using it way more frequently.

.. code-block:: c++
   :linenos:

    public:
        void func1(Circle c);
        void func2(const Circle& c);

| There's two major differences between them, and depending on the situation you'll use one or the other, but in most cases you'll be using the syntax of ``const Circle& c``.
*   Passing by value calls a Copy Constructor for that object, then that copy is used within the function. Modifying the object within the function doesn't affect the original object.
*   Passing by reference makes a pointer for that object, and sends that pointer into that function. Modifying the object within the function affects the original object.
| The only time you should pass by Value is if the object in question is cheaper than 8 bytes (assuming you're on a 64-bit system), because then you're using less data by making a Copy than you are by making a reference. Since a reference uses a pointer, and a pointer uses 8 bytes (in a 64-bit system. It uses 4 bytes in a 32-bit system), you should only use it if the data types in your object total more than 8 bytes. So in this case, we have 3 ``float`` data types, which equals 12 bytes. For this scenario, passing by ``const`` reference is cheaper. If, however, we only had one data type, or 3 ``bool`` or ``char`` variables instead, then passing by value would be cheaper.
|
| Of course there's also the scenario where you pass by reference where you *do* want to modify the original object, but that's rare. Still, you just remove the ``const`` keyword in that scenario.
|
| A Copy Constructor by default performs member-wise assignment of values from one Object to the other. It's triggered via one of three ways:

.. code-block:: c++
   :linenos:
   :emphasize-lines: 3, 4, 8

    Circle c1(1, 2, 5);
    Circle c2(3, 5, 3);
    Circle c3 = c1;
    Circle c4(c2);
    Circle* c6 = new Circle(c3);
    Circle c5;
    c5 = c1;
    func(Circle c) {}
    func(const Circle& c) {}

| Take note: ONLY in lines 3, 4, and 8 is a Copy Constructor called. Line 5 is just a version of Line 4 where it uses the Heap instead. It's also called in that line but the Syntax isn't new. The combination of lines 6 and 7 does NOT trigger a copy constructor! That's different, that's the assignment operator. That's gonna get covered in Operator Overloading. Line 9 *also* does not call a Copy Constructor, as it's passing the Object by reference, which is just in practice making a pointer.
|
| Line 3 *does* call a copy constructor, Line 4 *does* call a copy constructor, Line 5 *does* call a copy constructor, Line 8 *does* call a copy constructor, Lines 5 and 6 together *do NOT* call a copy constructor, and Line 9 *does NOT* call a copy constructor.
|
| Regarding Line 8, it's making a Copy Constructor because the Object is being passed by value instead of by Reference. I mentioned way earlier that passing by reference is simpler for Objects because if their complexity is high then it has to copy all of those values over and do a lot of data processing and moving, whereas a reference just has to make a pointer. This is why.
|
| You can treat the Copy Constructor just like a regular constructor and modify it to your needs. This is where we make the adjustment for the Heap to solve our initial problem as well, and make it so a *proper* copy of the Object is made. Copying all values from one Object to another is called a Shallow Copy, which is where we face our limitation. Copying all the values after going in and individually grabbind and assigning them, however, is called a Deep Copy. This is what we use when dealing with Dynamic Memory.
|
| There are two limitations of a Shallow Copy. The first is that either object's modification shows up for the other one, since they both point to the same Heap location. The second limitation is that if one Object's destructor is called, that location is freed. The other Object, however, still points to that location. It ends up having a Dangling Pointer. So the code snippet shown below is an example of how a Deep Copy is made when dealing with Dynamic Memory in Classes:

.. code-block:: c++
   :linenos:

    class Array {
    private:
        int* ptr;
        int size;
    public:
        int* getPtr() const { return ptr; }
        int getSize() const { return size; }
        Array(int* pointer = nullptr, int s = 0) { ptr = pointer; size = s; }
        Array(const Array& copy);
        void print() {
            for (int i = 0; i < size; i++)
                cout << ptr[i] << " ";
            cout << endl;
        }
        void randomize() {
            for (int i = 0; i < size; i++)
                ptr[i] = rand() % 100;
        }
    };
    Array::Array(const Array& copy) {
        if (copy.getSize() == 0 || copy.getPtr() == nullptr)
            return;
        size = copy.getSize();
        ptr = new int[size];
        for (int i = 0; i < size; i++)
            ptr[i] = copy.getPtr()[i];
    }
    int main() {
        srand(time(0));
        Array a1(new int[3], 3);
        a1.randomize();
        Array a2 = a1;
        cout << &a1.getPtr()[0] << endl; // Printing address of a1's heap location
        cout << &a2.getPtr()[0] << endl; // Printing address of a2's heap location
        a1.print();
        a2.print();
        a1.randomize();
        cout << endl;
        a1.print();
        a2.print();
    }

| And now you can see that the two Objects have entirely different locations in memory, but their ``print`` functions give the same values of the Arrays. You can even see how running ``randomize()`` on one of the Objects won't affect the other. If we hadn't made the appropriate changes to the Copy Constructor, ``a2.print()`` would still be pointing to the Heap location of ``a1``.
|
| One last thing to mention, if you end up making your own Copy Constructor, you have to add in all the code for individual Data Members yourself. If there were a few other variables, such as another ``int``, ``string``, ``float``, ``char``, or really anything, then it won't be copied over automatically. You'll have to specifically write the code to copy over the values from the copy. This was done because sometimes you want to copy over values but not every single one. It was better to have the choice. So if something isn't being copied over correctly, remember to actually write the code for copying it!
|
| And, this was added on a way later date. There's a third time a Copy Constructor can be called, but depending on the Compiler in question, it may (very likely) be ignored. Compilers are allowed to do so, but also not required to do so. It can be turned on or off as well. There's a concept in C++ called ``Copy Elision``, which falls under ``Return Value Optimization (RVO)``. This page https://stackoverflow.com/questions/12953127/what-are-copy-elision-and-return-value-optimization explains it in detail, but all you really need to know is, look at this code:

.. code-block:: c++
   :linenos:

    Circle func() {
        Circle temp;
        return temp;
    }
    int main() {
        Circle c1 = func();
    }

| When you return an Object, it calls a Copy Constructor. Or, well, it's supposed to, but calling the Copy Constructor can be extremely expensive on memory. For this reason, many compilers optimize the process by just returning that value directly instead of making a copy for it. So if you happen to add some ``cout`` statements to the Copy Constructor, they may or may not be called, depending on how that specific Compiler has decided to do optimizations. The link above will explain it better. https://stackoverflow.com/questions/14154290/why-isnt-the-copy-constructor-called also has an example.
