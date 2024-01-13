.. _s3-dsa-t08:

8) Linked Lists
---------------

| Continuing from the previous page, where we defined these specific functions for the List:

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

| I showed an array based implementation, and now we'll be looking at a Node and Pointer based implementation, which has its own advantages and disadvantages but we'll get to those later.
|
| You may have already seen this in action or even implemented it but just in case this is your first time hearing of a Linked List, I'll explain how it works.
|
| A Linked List is a Data Structure that consists of a series of Nodes, and each node holds two things: a value, and a pointer to the next node in the list. You can think of it like a series of houses, and to get to a specific house first you go to the house you do know, and ask the person there "Hey where can I find this house?" He'll either say "It's that way", or he'll say "I don't know, ask this other house". If he says "It's that way", great! You've found the house. But if not, you have to ask that other house, and that second house can also say "It's that way" or "I don't know, ask this other house". This keeps going until you either find the house you're looking for, or you find out that it doesn't exist.
|
| This house analogy is something I'll be using to explain other types of linked lists as well, such as circular linked lists and doubly linked lists, but one thing at a time. For this first category, which is just a general linked list, each house is unique and you can only go to the next house, you can't go back to the previous house. This is called a Singly Linked List and this is what we'll be implementing.
|
| So let's get started with the code. First we need to define a Node class, which will hold the value and the pointer to the next node. This acts as our house, and the pointer to the next node acts as the directions to the next house. If the pointer to the next node is ``nullptr``, that means there's no next house and you've reached the end of the list.

.. code-block:: c++
   :linenos:

    template <typename T>
    class Node {
    public:
        T value;
        Node<T>* next;
        Node(const T& item, Node<T>* next = nullptr) {
            this->value = item;
            this->next = next;
        }
    };

| Now we want to use this to make the List. Unlike the Array based implementation, one of the main drawbacks of the Linked List approach is that you can't just get to a specific index (aka house) in the list. You always start at the first house and make your way down. You as the programmer might know that the house exists but the computer won't. Here's what the complete code for a Linked List would look like but if you want to try it out yourself, I recommend you try to implement it yourself first with the function prototypes already listed above.

.. code-block:: c++
   :linenos:

    template <typename T>
    class List {
    private:
        Node<T>* head;
        int count;
    public:
        List();
        ~List();
        int size() const;
        bool isEmpty() const;
        // no isFull() this time because we can always add more Nodes to the end
        void insert(const T& item, int pos);
        void append(const T& item);
        void remove(int pos);
        void remove(const T& item);
        T retrieve(int pos) const;
        void replace(const T& item, int pos);
        void clear();
    };
    template <typename T>
    List<T>::List() {
        this->head = nullptr;
        this->count = 0;
    }
    template <typename T>
    List<T>::~List() {
        this->clear();
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
    void List<T>::insert(const T& item, int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Invalid position." << endl;
            return;
        }
        if (pos == 0) {
            Node<T>* newNode = new Node<T>(item, this->head);
            this->head = newNode;
        }
        else {
            Node<T>* temp = this->head;
            for (int i = 0; i < pos - 1; i++) {
                temp = temp->next;
            }
            Node<T>* newNode = new Node<T>(item, temp->next);
            temp->next = newNode;
        }
        this->count++;
    }
    template <typename T>
    void List<T>::append(const T& item) {
        this->insert(item, this->count);
    }
    template <typename T>
    void List<T>::remove(int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Invalid position." << endl;
            return;
        }
        if (this->head == nullptr) {
            cout << "Error! List is empty." << endl;
            return;
        }
        if (pos == 0) {
            Node<T>* temp = this->head;
            this->head = this->head->next;
            delete temp;
        }
        else {
            Node<T>* temp = this->head;
            for (int i = 0; i < pos - 1; i++) {
                temp = temp->next;
            }
            Node<T>* toDelete = temp->next;
            temp->next = toDelete->next;
            delete toDelete;
        }
        this->count--;
    }
    template <typename T>
    void List<T>::remove(const T& item) {
        if (this->head == nullptr) {
            cout << "Error! List is empty." << endl;
            return;
        }
        Node<T>* temp = this->head;
        Node<T>* prev = nullptr;
        int pos = 0;
        while (temp != nullptr) {
            if (temp->value == item) {
                prev->next = temp->next;
                delete temp;
                return;
            }
            prev = temp;
            temp = temp->next;
            pos++;
        }
        cout << "Error! Item not found." << endl;
    }
    template <typename T>
    T List<T>::retrieve(int pos) const {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Invalid position." << endl;
            return T();
        }
        Node<T>* temp = this->head;
        for (int i = 0; i < pos; i++) {
            temp = temp->next;
        } 
        return temp->value;
    }
    template <typename T>
    void List<T>::replace(const T& item, int pos) {
        if (pos < 0 || pos > this->count) {
            cout << "Error! Invalid position." << endl;
            return;
        }
        Node<T>* temp = this->head;
        for (int i = 0; i < pos; i++) {
            temp = temp->next;
        }
        temp->value = item;
    }
    template <typename T>
    void List<T>::clear() {
        Node<T>* temp = this->head;
        while (temp != nullptr) {
            Node<T>* toDelete = temp;
            temp = temp->next;
            delete toDelete;
        }
        this->head = nullptr;
        this->count = 0;
    }

| Thus concludes the implementation of a functioning Linked List, but there's a small problem. If we compare the complexities of the functions in the Array based implementation and the Linked List based implementation, they're not the same.
*   ``size()``: O(1) vs O(1) (Both return a variable that remembers the size)
*   ``isEmpty()``: O(1) vs O(1) (Both do a check on the variable that remembers the size)
*   ``isFull()``: O(1) vs N/A (isFull() doesn't exist for the Linked List as more nodes can always be added to the end of the list)
*   ``insert()``: O(n) vs O(n) (For the array, we have to shift all the elements after the position we're inserting at, and for the linked list, we have to traverse the list until we get to the position we're inserting at)
*   ``append()``: O(1) vs O(n) (For the array, we just insert at the end, and for the linked list, we have to traverse the list until we get to the end)
*   ``remove()``: O(n) vs O(n) (For the array, we have to shift all the elements after the position we're removing at, and for the linked list, we have to traverse the list until we get to the position we're removing at)
*   ``retrieve()``: O(1) vs O(n) (For the array, we just return the element at the position, and for the linked list, we have to traverse the list until we get to the position)
*   ``replace()``: O(1) vs O(n) (For the array, we just replace the element at the position, and for the linked list, we have to traverse the list until we get to the position)
*   ``clear()``: O(1) vs O(n) (For the array, we just set the size to 0 or call ``delete``, and for the linked list, we have to traverse the list and delete each node)

| But there's a way to speed this up in favor of the Linked List. If we add a ``tail`` variable to the List class, we can keep track of the Last Node in the list, and this will speed up ``append`` from O(n) to O(1) because only one dereference is needed to get to the end of the List. This is how a Linked List *should* be implemented, and the reason I didn't write it in the code above is because I want you to practice and improve your own skills too. Try to look at Data Structures and see if there's ways to optimize them. This is a simple example. Also, in the code for ``void List<T>::remove(const T& item)``, I saw someone implement that by first finding the ``pos`` of the Node where the value is, then calling ``remove(pos)``, which is a VERY inefficient way of doing this because in its worst case it means going through the entire linked list *twice*. Always think about ways to speed things up.
|
| If ``tail`` is implemented, the extremely fast ``append`` function, alongside the flexibility of being able to add more Nodes without worrying about the size of the List, is why Linked Lists are still commonly used today. Yes, some operations of the linked list are slower than the array based implementation, but the data structure to implement depends on which operations are most frequent. In a list, ``append`` is used *very frequently* compared to other operations, and although the time complexity for ``insert`` and ``remove`` is the same, the number of operations needed is way less, because in the Array based version you have to shift entire blocks of data, which can be a lot of load on the CPU and RAM, but in a Linked List you just have to change the pointers of a few Nodes, which is much faster.
|
| I'll modify the page to include diagrams and if possible, animations of all the functions too, but for now, I hope it makes sense.