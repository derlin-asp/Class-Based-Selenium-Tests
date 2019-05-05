# Class-Based-Selenium-Tests
Testing of Demo Website for Many Different Test using Python Unittest Request Library etc

<h2>Class Diagram</h2>

![Alt text](https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf}
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
)




<h1>login.py</h1>

This is the main testing file. Calls other methods from other classes to test login and logout functionality






