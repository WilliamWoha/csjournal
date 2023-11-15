.. _s3-dsa-req0:

Requirements
------------

| Same as the last two Semesters. You just need a Compiler and a Pen and Paper. Though this time we'll also be utilizing a Visualization program called ``Graphviz``. My university didn't teach this to me, I had to learn it on my own, but it's such a useful tool that I don't think anyone should learn Data Structures or any Data Visualizations without it. You can obtain it at https://graphviz.org/. This is a program that takes anything written in the ``DOT`` language and converts it into a ``.png`` or ``.svg`` for viewing. Here's an example to showcase its behaviour:

.. code-block:: DOT
   :linenos:
      
    graph {
        layout = "circo"
        a -- b;
        b -- c;
        a -- c;
        d -- c;
        e -- c;
        e -- a;
    }

| Produces this:
|
.. raw:: html
    :file: images/graphviz_example.svg
|
|
| https://graphs.grevian.org/example has more examples of it in action. So you can see how much power it has. The only challenge is that unlike ``pythontutor.com`` which shows how the data is actually arranged in memory, GraphViz and DOT require you to manually code the functionality, and that's going to depend on your specific Data Structure. You have to tell it how to visualize the data. It doesn't just do it for you. On top of this, the layout can sometimes be...less than ideal to work with. If you remove ``layout = "circo"`` then it turns into this:
|
.. raw:: html
    :file: images/graphviz_example2.svg
|
| Although the layout and links between nodes are the exact same, the actual layout it generates is not easy to look at. You'll have to put in extra effort to clean it up manually, which can involve a lot of trial and error.
|
| I'll provide functions for how to print out the full set of data using Graphviz, but if your Data Structure is implemented in a different way, your GraphViz function will also have to be done differently. All it does is visualize what you wrote in it, you still have to be careful about what you write into it.
