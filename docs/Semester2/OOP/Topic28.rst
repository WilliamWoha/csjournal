.. _s2-oop-t28:

28) Virtual Destructors
-----------------------

| When you do ``Base* ptr = new Derived;``, it allocates new memory by calling upon the default constructors. Constructors aren't a concern here, Destructors are. And as far as Inheritance is concerned, you should *always* make your destructors Virtual. Consider this code: 

.. code-block:: c++
   :linenos:

    class Base {
    public:
        ~Base() {
            cout << "Calling ~Base()" << endl;
        }
    };
    class Derived: public Base {
        int* arr;
        int size;
    public:
        Derived(int size) {
            this->size = size;
            this->arr = new int[size]{};
            for(int i = 0; i < size; i++)
                arr[i] = i;
        }
        ~Derived() {
            cout << "Calling ~Derived()" << endl;
            delete[] arr;
        }
    };
    int main() {
        Base* ptr = new Derived(5);
        delete ptr;
    }

| You get the output ``Calling ~Base()``. That's it. Deleting ``ptr`` only calls the destructor for ``Base`` since it's a ``Base`` pointer. It's acting like a regular function here. But since we want the ``Derived`` destructor to also be called so we don't face a memory leak, we make the Destructor Virtual. Just make ``~Base()`` into ``virtual ~Base()`` and you're good to go. It'll output ``Calling ~Derived()`` and then ``Calling ~Base()``.
|
| The rule is, whenever you're dealing with inheritance, you should make the destructors virtual.