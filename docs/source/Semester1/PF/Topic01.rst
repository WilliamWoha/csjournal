.. _s1-pf-t01:

1) Intro to Binary and Languages
--------------------------------

| There are three types of languages:
*    Machine Language: The only language machine actually understands. This is the 0's and 1's you see. Very cumbersome for humans but ALL languages are deconstructed to this level via something that translates them for the computer.
*    Assembly Language: 1's and 0's with letters. It's very very close to Machine Language but is readable by humans. You can program in it but it will test your patience like no other. But hey, Chris Sawyer got 30 Million Dollars for it since he made a game called RollerCoaster Tycoon. So if you have the guts, then go for it. The translator for Assembly Language is called the Instructor.
*    High Level Language: Way closer to Human Language. Uses Common Math operations, and converted either in real time with Interpretors, or after compiling all at once with Compilers. C++ is a Compiled language. Compiler languages are much faster than Interpreted languages but troubleshooting can be a massive hassle as, if one part of the code doesn't work, the entire thing drops.

| Ok so if you didn't understand the above stuff much, here's how it works.
| The things we see on the computer. The Images and Movies we watch or the Sounds we hear or the Games we play. They're all handled by the Computer. The stronger the computer, the better it handles it. But the thing is, the Computer is dumb. It can't understand any of that. And you might be thinking, yeah that's why we would use a Programming Language. But the thing is, even a Programming Language is made up of elements that the computer can't actually understand. It has to be broken down into the absolute basics: The 1's and 0's you see in memes or movies. Those 1's and 0's are Machine Language. But the thing is, they're basically impossible to understand, even if you *do* know how they work. So to make it easier. Assembly Language was invented. But even that is kind of difficult to handle. So Programming Languages were made, which are FAR more readable and understandable for us humans.
| The drawback of adding more layers to make it easier for *us* to understand, is that it makes it harder for *the computer* to understand. This is why Python is considered the simplest language for beginner programmers but it's also 70 times less efficient than something like C++. Both Python and C++ are High Level Languages. 
| C++ is a compiled language, meaning you make a code, and then it's built. But if the code has a problem, then the computer won't even *start* to build it. 
| Python on the other hand is an Interpreted language, meaning after the code is made, you can immediately build it, and you'll only experience a problem when you actually get to it.

Intro to the Binary Number System
"""""""""""""""""""""""""""""""""

| As for what the 1's and 0's in Machine Language actually are, they're the Binary System. You can see the video here to understand it. If you know it already then you can skip to :ref:`s1-pf-t03`.

.. raw:: html

    <div style="position: relative; padding-bottom: 2%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="640" height="360" src="https://www.youtube.com/embed/LpuPe81bc2w" title="Binary Numbers and Base Systems as Fast as Possible" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

| If the video doesn't make sense to you then I'll try to explain it in text. Knowing how it works is important because the language we'll be doing (C++) uses these concepts a lot in how its made.
| If the video DOES make sense then you can skip the rest of this page, or read it anyways for a better understanding.
|
| This might get a bit difficult to explain so I'm just *hoping* it makes sense.
|
| Let's say you have the number 5,279. I'd ask you how you actually *know* it's that number. And you'd be confused as to what kind of question is that. It's an unusual question but, just bear with me. We're roleplaying. I'm the computer. I'm dumb, I don't understand anything. So how do you know what 5,279 means?
|
| There are 10 digits. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. And that's all you can count towards. If you were counting, and counted till, for example, 5, and then suddenly started counting again, you could go to 6. Then 7, then 8, then 9. But how do you count what comes after 9? You've run out of digits haven't you?
| That's where extra positions come in. Tens, Hundreds, Thousands.
| That's how the number system works.
|
| The digit 9 is in the Units place.
| The digit 7 is in the Tens place.
| The digit 2 is in the Hundreds place.
| The digit 5 is in the Thousands place.
|
| The thing is, the digits are the same. They're all from 0 to 9. 5 falls in that range, so does 2, so does 7, and so does 9. What gives the numbers their *values* are their positions. The Tens Position means if you put a digit there, it would be worth 10 times more. So 7 would actually be 70. Hundreds means the digit would be worth 100 times more. So 2 would actually be 200.
|
| 5,279 is in fact 5000 + 200 + 70 + 9.
|
| Now here's where it gets a bit trickier because I have to explain the Binary system now. But I'm just *praying* it makes sense.
|
| The reason the Tens position is worth 10 times the digits, is because there's 10 digits. The reason the Hundreds position is worth 100 times the digits, is because there's 10 digits. The number of *base digits* is 10.
|
| Let's say, instead of 0 to 9, you want to use a new set of digits. And this new set of digits only has two positions: 0, and 1. But what if you want to count till the number 3?
| We'll do the same thing 0 to 9 did. We add more digits to the left side, with their values increasing. So to represent the number 3, you'd say it is 11. 
| You might see that number and think it's eleven, but it is in fact three. It's just difficult to see that because of the two 1's. You're just not used to it. But I'm hoping what I say next will let everything just click.
|
| Tens meant 10 times the value. 10 can also be written as 10\ :sup:`1` \.
| Hundreds meant 100 times the value. 100 can also be written as 10\ :sup:`2` \.
| Units meant the original digits are the value. 0 to 9. It can also be understood as multiplying with 1, or multiplying with 10\ :sup:`0` \.
|
| 5,279 is (5 x 10\ :sup:`3` \) + (2 x 10\ :sup:`2` \) + (7 x 10\ :sup:`1` \) + (9 x 10\ :sup:`0` \).
|
| Since there are 10 digits from 0 to 9, the values in the Tens and Hundreds positions are in fact exponents of 10. I said *base digits* earlier. If you've studied exponents then the word should be familiar. The *base* of the powers are 10. But if you reduce the Base to 2 instead, then what happens to the values of the Tens and Hundreds?
|
| They become 2\ :sup:`1` \ and 2\ :sup:`2` \ respectively. So any number in the Tens position with Base 2 would in fact be worth 2\ :sup:`1` \ times more, and any number in the Hundreds position with Base 2 would in fact be worth 2\ :sup:`2` \ times more.
|
| So going back to the number 11 that we wrote. I told you it's not actually eleven, but it's three. It should make sense to you now. The reason it's three is because it's (1 x 2\ :sup:`1` \) + (1 x 2\ :sup:`0` \). Which is 2+1.
| What about the number 6?
| Just like how one position with 0 to 9 can go till 9, and two positions can go till 99, if you want to store more with base 2 then you just keep adding more positions. So the max value of two positions with Base 2 is 3. But with three positions, it's 7. Three positions are enough to store the number 6.
| So we adjust accordingly and we get 110. Which is (1 x 2\ :sup:`2` \) + (1 x 2\ :sup:`1` \) + (0 x 2\ :sup:`0` \).
|
| To basically summarize: The number system works on the foundation that every next position is worth the *base* times more than the previous one. Thousands is worth 10 times more than 100, which is 10 times more than 10, which is 10 times more than 1. And the base is determined by the number of digits. If the base was switched to 2, then the next values would be worth 2, 4, 8, and 16 times respectively.
|
| This is the Binary system. A number system with Base 2. Every single computer on the planet that works with electricity uses this.
|
| As for how to actually *convert* to and from Binary values, that's gonna be explained on the next page. This much is already enough.
