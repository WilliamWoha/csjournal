.. _s1-pft-l11:

Theory Lecture 11
-----------------

| Week 6, but this is the second class of the week and not the first. That one was lost due to Sessionals. I have no idea what they'll do to recover that.

.. _s1-pft-t013:

Selection Structures (elseif)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| So remember the statement I made earlier? "If this happens, then do this. Otherwise do this". Let's modify that a bit. "If this happens, do this, but if this happens, do this, and if neither of those happen, then do this". That's IF, ElseIF, and ELSE in a nutshell.
| Elseif is used when more than two conditions have to be checked. Let's assume we have two numbers, a and b.

    | ``if (a>b)``
    | ``{``
    
        | ``cout << a << " is greater." << endl;``
    | ``}``
    | ``elseif (b>a)``
    | ``{``
    
        | ``cout << b << " is greater." << endl;``
    | ``}``
    | ``else``
    | ``{``
    
        | ``cout << "Both are equal." << endl;``
    | ``}``
| There's three conditions there. One being, ``a > b``, the second being ``a < b``, and the third being ``a == b``. Now you could do this any way you want, and even put the ``a == b`` statement at the start and leave the other two in an ``elseif`` and ``else``. The choice is yours.
| You can have wayyyy more elseif statements too, for checking more conditions.
| Here's a little tip about IF statements though. Those ``{ }`` brackets you see? They're only used if there's more than one line of code to execute. Otherwise, you can be completely fine with something like this:

    | ``if (marks >= 90 && marks <= 100)``
    
        | ``cout << "A grade." << endl;``
    | ``elseif (marks >= 80 && marks < 90)``
    
        | ``cout << "B grade." << endl;``
    | ``elseif (marks >= 70 && marks < 80)``
    
        | ``cout << "C grade." << endl;``
    | ``elseif (marks >= 60 && marks < 70)``
    
        | ``cout << "D grade." << endl;``
    | ``else``
    
        | ``cout << "Failed." << endl;``
| And yes this is exactly how you do correction statements. You just write ``if (marks > 100 || marks < 0)`` at the start and get the code to output a statement saying that this isn't an acceptable answer.
| Anyways. That about covers that. The only thing left is Nested IF statements, and then my 9 hours of typing can come to a rest and PF will have been caught up. Then I'll do weekly updates on this or something.

.. _s1-pft-t014:

Nested Selections
^^^^^^^^^^^^^^^^^

| Ok so if you already know this then great but if you don't already know this then it's a rather simple concept but once you get it, it's super easy.
| "If Pizza Hut is open, go there. If they have the Medium Combo, then get the Medium Combo, otherwise get the Small Combo. If Pizza hut isn't open, go to Dominoes. If they have the Weekend Deal, get the Weekend deal. Otherwise, get a Buy 1 Get 1 Free Deal. If neither is open, come back home."
| Here's how that would be written in code.

    | ``if (Pizza hut is open)``
    
        | ``if (Medium Combo is there)``
        
            | ``Get Medium Combo``
        | ``else``
        
            | ``Get Small Combo``
            
    | ``elseif (Pizza hut is closed && Dominoes is open)``
    
        | ``if (Weekend Deal is there)``
        
            | ``Get Weekend Deal``
        | ``else``
        
            | ``Get Buy 1 Get 1 Free Deal``
    | ``elseif (Pizza Hut is closed && Dominoes is closed)``
    
        | ``Go home``
| That's about it. You should be able to understand that. If not then watch a YT video on it, I'm tired.
| You may have noticed that the last statement is an ``elseif`` and not an ``else``. That's because the two conditions before it were: ``Pizza hut is open``, ``Pizza hut is closed AND Dominoes is open``. If we did an ELSE statement here, that would also include the situation of both Pizza Hut and Dominoes being open. You're not supposed to go home if they both happen to be open.
| ELSE is the equivalent of checking the opposites of the previous IF statements.

