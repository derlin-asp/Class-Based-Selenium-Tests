# Class-Based-Selenium-Tests
Testing of Demo Website for Many Different Test using Python Unittest Request Library etc
Using Page Object Model

The tests can be run individually from the CLI or run as a group using pytest

<h2>Class Diagram</h2>


![Imgur](https://i.imgur.com/ChbZhn7.png)


<h2>Test Classes</h2>

These classes launch the POM class methods. Each Test Class is a single test.


They have names like <b>test_feature_being_tested.py</b>

So test_admin_employee_sort.py would be testing the sorting feature on the admin page.

They are located in the Tests folder


<h2>Page Object Models</h2>

These files contain the object representation of the pages being tested.


this includes the locators from the locators class and the methods for testing features.


They are named like AdminPage.py

Located in the Pages Folder


Locator.py and other configuration files are in the HelperClasses folder









