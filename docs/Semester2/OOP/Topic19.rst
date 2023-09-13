.. _s2-oop-t19:

19) Operator Overloading
------------------------

| Out of the frying pan and into the fire. It's crazy just how much functionality and freedom C++ gives you. Being able to make your own data type, having specific ways to Construct it, Destruct it, Copy it, Make Friends, and now perform specific operations on it.
|
| Operator Overloading lets you perform specific tasks on Objects through the use of already existing operators within C++. It saves you from the headache of trying to use function names. It's the kind of thing where you spend a lot of time and effort on making the class as polished as possible, so the implementation of it for the user, whether it's you or someone else, is as easy and as efficient as possible. If you're the only one that's working on your code then readability can be thrown out the window as long as it works. But later on you're going to be working in teams, and asking for improvement or advice or trying to understand and cooperate with people about implementations. This is what makes readability so important. It's much much easier and much more readable to write ``c3 = c1 + (c2 * c3);`` than it is to write ``c3(c1.add(c2.mul(c3)));``. So, let's get started.