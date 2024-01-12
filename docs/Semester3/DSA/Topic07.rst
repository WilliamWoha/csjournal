.. _s3-dsa-t07:

7) Lists
--------

| In everyday life, we use lists to note things down and remember them. It's a collection of items of the same type, and the list can grow and shrink on demand. This is the ADT of a list, and there's two ways to implement a list in C++: using an array or using a linked list. The array implementation is the simplest, but it has a fixed size. The linked list implementation is more complex, but it can grow and shrink on demand. We'll start with the array implementation.
|
| The key features of a list are as such: Elements can be inserted, accessed, or deleted, no matter where they are on the list. You can add an item to the end of the list, to the middle, at the start, you can overwrite existing items, you can cut off (or in programming terms, delete) existing items, and the list (pun intended) goes on. A list is a sequence of zero or more elements of a given type, and is said to have ``n`` elements. If ``n`` is ``0`` then the list is empty, and if it's not ``0`` then the list has items on it.
|
| Lists also have more properties but those are just common sense things like having a list of lists or having 1 item or 0 items on the list or being able to join two lists together or splitting the list into sublists.
|
| Now that we've defined the list, we want to define in Pseudocode what kind of operations we want it to be able to do in Programming:
*   Create the list
*   Destroy the list
*   Find the size of the list
*   Check if the list is empty
*   Check if the list is full (Array based implementation only)
*   Insert an item at a given position in the list
*   Delete an item at a given position in the list
*   Retrieve an item at a given position in the list
*   Replace an item at a given position in the list
*   Clear the list
| And you can add more operations to that if you want such as Sort the list or Merge the list or Print the list, it's up to you. The ADT is the blueprint we're meant to use to implement the Data Structure in C++, or Python, or any language, but since we've studied C++ that's what we'll use. The first year of the degree was just to establish a foundation of a programming language, and everything we study from here on out can apply to *any* language. It's a Bachelor's of Computer Science not a Bachelor's of C++. There's no point in knowing the language if you don't know how to use it to solve problems and innovate.
|
| Now that we've defined the ADT, we can start implementing it in C++.

.. code-block:: c++
   :linenos:

    template <typename T>
    class List {
    public:
        List();
        ~List();
        int size() const;
        bool isEmpty() const;
        bool isFull() const;
        void insert(const T& item, int pos);
        void remove(int pos);
        T retrieve(int pos) const;
        void replace(const T& item, int pos);
        void clear();
    };

| The code above is just a template for the list, and it's not complete. We'll need to implement the functionality, and that's where the fun begins.
|
| In terms of implementation, there are two approaches to making a List: Array based and Pointer based (also called a Linked List). The Array based implementation is the simplest, but it has a fixed size. The Linked List based implementation is more complex, but it can grow and shrink on demand. We'll start with the Array based implementation.
|
| First, the advantages: Accessing elements of the list will be *extremely* fast because it's in the form of an array. The disadvantagegs however, are plentiful. The first and biggest one being that an array based implementation will have a fixed size unless you use a vector, and in that situation it copies all the elements from the old array to the new one which is an extremely expensive operation. As for the second requires some explanation, so here goes: The main operations we have are for inserting and deleting items from the list, and that's also where you'll see on the code below the most amount of work being done. The other operations are just simple checks or assignments. One of the rules of the List ADT is that you have to be able to insert and delete anywhere on the list, meaning the order of the data must be preserved after the operation. An insert operation for an array can just be putting the item at the end of it, but here we want to insert at a specific position *and* make it so that new insertion fits it without breaking the order. So if you have ``a b c d`` at locations ``0 1 2 3`` and you want to insert ``e`` between 1 and 2 then the order MUST result in ``a b e c d``, which is why the loop. It's *shifting* the elements, like in insertion sort, and this is a very expensive operation for something as simple as inserting. The same goes for deleting an item. If you want to delete ``b`` from the list above, then you have to shift the elements to the left, and that's also an expensive operation. The reason why it's expensive is because you have to shift ``n`` elements, and if you have a list of 1000 elements then you have to shift 1000 elements.
|
| An array based implementation would look like this:

.. code-block:: c++
   :linenos:

    template <typename T>
    class List {
    private:
        T* items;
        int capacity;
        int count;
    public:
        List(int capacity);
        ~List();
        int size() const;
        bool isEmpty() const;
        bool isFull() const;
        void insert(const T& item, int pos);
        void remove(int pos);
        T retrieve(int pos) const;
        void replace(const T& item, int pos);
        void clear();
    };
    template <typename T>
    List<T>::List(int capacity) {
        this->capacity = capacity;
        this->items = new T[capacity];
        this->count = 0;
    }
    template <typename T>
    List<T>::~List() {
        delete[] this->items;
    }
    template <typename T>
    int List<T>::size() const {
        return this->count;
    }
    template <typename T>
    bool List<T>::isEmpty() const {
        return this->count == 0;
    }
    template <typename T>
    bool List<T>::isFull() const {
        return this->count == this->capacity;
    }
    template <typename T>
    void List<T>::insert(const T& item, int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Not a valid position." << endl;
            return;
        }
        if (this->isFull()) {
            cout << "Error! List is full." << endl;
            return;
        }
        for (int i = this->count; i > pos; i--) {
            this->items[i] = this->items[i - 1];
        }
        this->items[pos] = item;
        this->count++;
    }
    template <typename T>
    void List<T>::remove(int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Not a valid position." << endl;
            return;
        }
        for (int i = pos; i < this->count - 1; i++) {
            this->items[i] = this->items[i + 1];
        }
        this->count--;
    }
    template <typename T>
    T List<T>::retrieve(int pos) const {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Not a valid position." << endl;
            return T();
        }
        return this->items[pos];
    }
    template <typename T>
    void List<T>::replace(const T& item, int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Not a valid position." << endl;
            return;
        }
        this->items[pos] = item;
    }
    template <typename T>
    void List<T>::clear() {
        this->count = 0;
    }

| Now, there *is* another method for using arrays which supposedly completely gets rid of the need to shift elements, and it's called a Free List, where you have another array that keeps track of the order and the free spaces in the array, but it still suffers from having a fixed size and it's a hassle to implement. If I get the energy I'll put up an explanation and some code showing how it works but until then, this is the best I can do. Try to implement it yourself as it *did* get asked about in an exam for me.