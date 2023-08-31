.. _s2-oop-t04:

4) Wrapping up Pointers
-----------------------

| We're not done with Pointers. Not even the slightest. We're just done with Pointers as far as C++ without OOP is concerned. They'll return in OOP and they will be brutal.
| Anyways the only thing that remains is using Pointers with Function Arguments and Return Types, Deleting Multi-dimensional Pointer Arrays, and changing the size of Pointer Arrays.

.. code-block:: c++
   :linenos:

    int*** subjects = new int**[a];
    for(int i = 0; i < a; i++)
    {
        subjects[i] = new int*[b];
        for(int j = 0; j < b; j++)
            subjects[i][j] = new int[c];
    }

| This was the code for making a 3D Pointer Array. To clear it, you just go in the opposite order.

.. code-block:: c++
   :linenos:

    for(int i = 0; i < a; i++)
    {
        for(int j = 0; j < b; j++)
            delete subjects[i][j];
        delete subjects[i];
    }
    delete subjects;
    subjects = nullptr;

|
| You still need to practice with it. That's the only way to get good.
|
| I'm not gonna go in depth about using Pointers in Functions but all you need to know is, where you'd write ``int`` you'd just write ``int*`` instead. That applies to arguments and return types both. And you can pass pointers by reference as well to modify the existing one if you want.
|
| Lastly, changing the size of a Pointer Array. This one is a bit complicated to grasp at first but once understood it'll all make sense.
|
| Let's say you have a dynamic array of size 5, accessed via a pointer ``ptr``, and you want to add a 6th value to it. The only problem is that it's an array of size 5. You'd have to declare another array of size 6 to accommodate that 6th value, and then copy all the previous values to it, then use the 6th memory location for storing that 6th value.

.. code-block:: c++
   :linenos:

    int* ptr = new int[5];
    for(int i = 0; i < 5; i++)
        ptr[i] = i+1;
    // ptr is now an array of size 5 with the values [1, 2, 3, 4, 5]
    int num = 10;
    int* ptr2 = new int[6];
    for(int i = 0; i < 5; i++)
        ptr2[i] = ptr[i];
    ptr2[5] = num;
    // ptr2 now has the values [1, 2, 3, 4, 5, 10]

| And that's it! You've now expanded your array. But the thing is, if you're doing something like game development and want to have a growing array, it's extremely taxing to try and copy over so much data. This is only 5 values. What if it's 5 million? So for this reason, what a lot of games do instead is increase the size a lot at once, so there's way less copy operations involved. So for example if I know I might add more values later, I'll increase the size by 5 instead of 1, and if more values do in fact show up, I'll just fill those slots up instead of expanding the array more. Some games take this even further by just having a static array and having a counter, and if that counter exceeds a specific value then they just clear things in the array. For example, in Minecraft, within one block if you have more than 255 entities, it kills the extra ones. This function is exploited by players to make an unlimited food farm. In Google Chrome or Mozilla Firefox, if you have way too many tabs open then it won't run every single one at the same time. If you try to force it to do that, it'll crash instead since it runs out of RAM. That's why sometimes if you click on a tab it'll load the page from scratch.
|
| Alright, now we move onto the bread and butter. Next stop is Structures, the preview for Classes.