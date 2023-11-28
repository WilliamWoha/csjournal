.. _s3-dsa-t03:

3) Class Templates
------------------

| This part is super important to Data Structures, because all of the ways we implement a Data Structure are supposed to be generalized for any piece of data.
|
| A class template, just like a function template, allows classes to change the data types present in them. For example, an ``std::vector`` is declared by ``vector<data_type> vectorName``. An ``std::vector`` if you don't know, is an array which can change its size, and since it's a general purpose array, it needed to be compatible with any data type stored in it. Since it's templatized, you can do that. ``vector<int> arr1`` is how you declare a dynamic array to store integers, ``vector<float> arr2`` is how you declare a dynamic array to store floats, and so on.
|
| Templatizing a class uses the same syntax as templatizing a function, and all other logic is the same as that of a function, except it's applied to a class instead.

.. code-block:: c++
   :linenos:

    template <typename T>
    class Vector {
    private:
        T* arr;
        int size;
    public:
        Vector(unsigned int size = 0) {
            if(size <= 0) {
                arr = nullptr;
                size = 0;
                return;
            }
            this->size = size;
            arr = new T[size];
        }
        int getSize() {
            return size;
        }
        bool isEmpty() {
            return size == 0;
        }
    }

| Something to note here: If you declare your member functions as in-line, then you can just do everything normally and just replace whatever data type you normally used with ``T``. But there's extra things to do if you declare your code to be out of line. Here's the difference:

.. code-block:: c++
   :linenos:

    template <typename T>
    class Vector {
    private:
        T* arr;
        int size;
    public:
        Vector(unsigned int size = 0);
        int getSize();
        bool isEmpty();
    }

    template <typename T>
    Vector<T>::Vector(unsigned int size) {
        if(size <= 0) {
            arr = nullptr;
            size = 0;
            return;
        }
        this->size = size;
        arr = new T[size];
    }
    template <typename T>
    int Vector<T>::getSize() {
        return size;
    }
    template <typename T>
    bool Vector<T>::isEmpty() {
        return size == 0;
    }

| That's just how the syntax works. When doing out of line, instead of doing ``Class::function(arguments)``, you just have to do ``Class<T>::function(arguments)`` instead, then you can carry on as normal.
|
| There's more to it but it's specialized cases which you can just look into yourself on cppreference or learncpp. This much is enough for us to deal with Data Structures.
