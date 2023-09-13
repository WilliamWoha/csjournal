.. _s2-oop-t15:

15) this-> Pointer
------------------

| This is gonna be a bit strange and we're only covering the concept of it here. This is going to be *extremely* important later in Operator Overloading, so make sure to understand it.
|
| A Class is a blueprint. An object is an implementation of said blueprint. When an Object is created, either in the Heap or the Stack, it occupies memory. If it's made in the Stack it'll be accessed via the variable name, and if it's in the Heap it'll be accessed via dereferencing the pointer. Either way, it has a memory address, and you can store that address into a pointer. But there's a specific pointer that every implementation of an Object has, and it's created whenever the Object is created. It's specific to each object, and points to only that object, whether it's in the Heap or Stack. It's called the ``this`` pointer, and it serves two purposes:
*   Same Name Arguments
*   Function Cascading
| Here's the syntax for it:

.. code-block:: c++
   :linenos:

    class Circle {
        float x;
        float y;
        float r;
    public:
        Circle(float x = 0, float y = 0, float r = 0) {
            this->x = x;
            this->y = y;
            this->r = r;
        }
    };
    int main() {
        Circle c1;
        Circle* c2 = new Circle;
    }

| The pointer's specifically only accessible within Member Functions. You can't modify the value for it, as it's a constant pointer, and you can't access it through the ``.`` or the ``->`` operators, meaning doing ``c1.this`` or doing ``c2->this`` isn't possible. It's also unnecessary since ``this->``, ``c1.``, and ``c2->`` all do the same thing, which is accessing the Object's Members.
|
| Notice how the Constructor has variables of the same name as those defined as Data Members for the Class. ``this->`` allows the Compiler to understand that the variable in question is the private member, and not the variable passed through the argument. It doesn't matter whether you use this method, or variables with different names, but using ``this->`` is better practice as it's easier to find the variable names and makes the program overall more readable.
|
| The second, way more important use of ``this->`` is Function Cascading. Function Cascading is the process of calling multiple functions of a single object at once, and you may not realize it but you've already been doing it with a lot of situations.

.. code-block:: c++
   :linenos:

    int b = 5;
    int a(b.operator+(3).operator/(1.5).operator*(6));

| You'll study this in way more detail in Operator Overloading, but the line above is just the real version of this:

.. code-block:: c++
   :linenos:

    int b = 5;
    int a = b + 3 / 1.5 * 6;

| If you need something more readable then there's also this example from python:

.. code-block:: python
   :linenos:

    name = 'JoHn CeNa'
    name2 = name.lower().capitalize().replace('cena', 'lennon')
    print(name2)

| Function Cascading means to call multiple functions one after another, and using the result of one function as the input or basis for the next function. In this case, it's calling ``b``'s plus operator with the argument of ``3``, and when that's calculated, it gets an object back. This resulting object is then calling ``.operator/()``, with the argument of ``1.5``. Once that's also calculated, it returns another resulting object, and that object then calls ``.operator*()``, with the argument of ``6``. Once that's all calculated, it finally returns an object, then calls the Copy Constructor to copy values from this temporarily generated Object into ``a``. For this reason, as you might have guessed, it's important for those functions to actually return an object, and that's what ``this`` allows you to do: Return a modified version of a temporary object. Here's how you'd practically implement it:

.. code-block:: c++
   :linenos:

    class Complex {
        float real;
        float imag;
    public:
        Complex(float real = 0, float imag = 0) {
            this->real = real;
            this->imag = imag;
        }
        float getReal() const {
            return real;
        }
        float getImag() const {
            return imag;
        }
        Complex operator+(const Complex& num) {
            real += num.getReal();
            imag += num.getImag();
            return *this;
        }
        Complex operator-(const Complex& num) {
            real -= num.getReal();
            imag -= num.getImag();
            return *this;
        }
        Complex operator*(const Complex& num) {
            // General form of multiplying two numbers is
            // (a+bi)(c+di) = (ac-bd) + i(ad+bc)
            // The minus is probably just there to deal with the i squared.
            float r1 = real; // To remember original value. Otherwise it gets re-written.
            real = (real * num.getReal()) - (imag * num.getImag());
            imag = (r1 * num.getImag()) + (imag * num.getReal());
            return *this;
        }
        void print() {
            cout << real << ", " << imag << "i" << endl;
        }
    };
    int main() {
        Complex c1(1, 2);
        Complex c2(4, 5);
        Complex c3(7, 0);
        Complex c4(0, 3);
        Complex c5 = (Complex() + c1 + c2 - c3) * c4;
        c1.print();
        c2.print();
        c3.print();
        c4.print();
        c5.print();
    }

| This also gives a general idea to operator overloading but I'm not going in-depth for it right now, I just did it to explain the value of ``this``. You can run that code and see the values. There's something to note here though, the reason I used ``Complex()`` in Line 43 is because that's currently the only way to prevent changes in the class. If you remove that specific part and turn it into ``Complex c5 = (c1 + c2 - c3) * c4;``, then you'll notice that ``c1`` will have different values than the ones declared in Line 38. We'll go into way more detail for Operator Overloading later, really all you need to understand is that ``this->`` points to an Object, and is the key in Cascading Functions, whether they be operators or not (though Operator Function Cascading is definitely the most powerful use case for this feature).