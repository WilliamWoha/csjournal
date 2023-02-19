.. _s1-pf-t30:

30) Passing Variables by Reference
----------------------------------

| Apparently I didn't have my register with me in this class because I just wrote down that we did "Matrix Multiplication and Passing by References. And also passing 1D and 2D Arrays to functions". So I'll try my best to explain those concepts, but I may be missing a couple of details here and there that may get asked about in my exams.

.. code-block:: c++
   :linenos:
   :emphasize-lines: 7
   
    #include <iostream>
    using namespace std;
    void fun(int n)
    {
        n = 5;
    }
    void fun2(int &n)
    {
        n = 10;
    }
    int main()
    {
        int n = 20;
        cout << n << endl;
        fun(n);
        cout << n << endl;
        fun2(n);
        cout << n << endl;
    }

| There's 3 ``cout`` statements for the ``n`` variable. Try and guess the outputs of each of those. You might get stuck on the third one, since that's the new thing we're doing today.
|
| If you guessed that the output of the first two lines would be 20, then you've learnt quite a bit. Well done lad! If you weren't able to get that then don't worry, you just learn and improve. You can always visit previous topics again if you wanna practice more.
| 
| The output of the third line will be 10. If you managed to get that then you've probably already done this topic before. If you managed to get that without knowing about this topic then....I have no words.
|
| Alright, onto the topic itself. Passing by Reference means passing the actual variable to the function instead of the function making a replica and modifying that instead. As you saw in the example above, even though in ``fun`` the line said ``n = 5``, the value in ``int main()`` was not affected, and the output was 20 in the second ``cout`` statement. However, in ``fun2``, the value was passed by Reference. This means that any changes made to that variable within that function, will in fact be modifying the actual value, as if it was there.

How the Computer Memory Works
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| I explained this slightly during :ref:`s1-pf-t07`, but we're gonna get into much more detail now. Read this next block of text carefully, and if you don't understand it, then read it multiple times. It's *CRUCIAL* that you understand this for Pointers.
|
| When you declare a variable, such as ``int n = 5``, then the program creates a location in the memory, and it stores the value 5 into it. It doesn't do this when the program is saved. It only does this when the Program is being run. It also does this in the computer's RAM so it doesn't slow down. Anyways, imagine the memory (RAM) to be a very very long road, and on one side of the road are houses, all neatly lined up. On the other side of the road there's nothing. It's a one sided neighborhood. Each of those houses has an Address, and each house also has stuff inside of it. There's basically infinite houses, but not all of them are occupied. If we, the programmer, decide we want to use the House so we can put stuff into it, then the Program prepares that house. If you do ``int n``, then a house is prepared, and any time you do something with ``n``, the stuff inside the house is changed. Doing ``int n`` means whatever the situation of the house was initially, will be kept as is, and the house will change only when needed. Doing ``int n = 5`` however, means that the house is immediately cleaned and then told to keep a value of 5.
| Now you have an understanding of how Memory works. Linear addresses to locations. Each House Address is actually a Memory Location (or more formally known as a Memory Address), and the stuff inside the house is the value present at that Memory Address.
| When a variable is sent to a function, the computer creates an identical house (variable) at another (memory) address. Anything that function does to the house (variable), will not be done to the original house. However, when you instead pass a value by reference, the function doesn't create another house. Instead, you're giving the function the address to the original house, and whatever the function does, is being done to the actual original house.
| 
| From this point on I won't talk in terms of houses and roads, and will now use the actual terms of Variables and Memory Addresses. I really hope this was understood. If not then there's videos explaining them in more detail with diagrams. If I find any then I'll link them.
|
| Before getting to the final explanation of the code, I just need to explain the ``&`` symbol. Then, everything should become clear.
|
.. code-block:: c++
   :linenos:
   :emphasize-lines: 6,7

    #include <iostream>
    using namespace std;
    int main() 
    {
        int a = 5;
        int& b = a;
        int& c = b;
        b = 10;
        cout << a << endl;
        c = 20;
        cout << a << endl;

        return 0;
    }

| If you run that code, you'll find the output of the ``cout`` statements to be ``10`` and ``20``. The variable ``a`` isn't being modified in any of the statements, yet outputting the value of ``a`` gives different values. The reason is because of the declaration of ``&b`` and ``&c``. The ``&`` symbol in this case is a way of declaring a nickname. "Peter Parker" and "Spiderman" are the same person but with different names and different looks. We'll ignore personality since that comparison doesn't exist in Computers. Same variable, but two different names and two different looks. Anything that happens to ``b`` will be reflected to ``a``. In the same way, anything that happens to ``c`` will be reflected to ``b``, which is a nickname of ``a``. I don't know if the term ``nickname`` is the actual computer term, but that's what my teacher used, and it makes it easy to remember.
|
| Just like that, when you're passing by reference in a function, you're creating another variable which happens to be a reflection, or a nickname, of the original one.
|
| This was a longer page than usual but I really really hope it made sense because if not, then Pointers will become far far more difficult. This all has to be understood.
|
| To those of you who know the second use of the ``&`` symbol, which has to do with Pointers, I'll repeat what I said earlier: "If something isn't explained yet then I'll get to it later. One thing at a time."



