Feature: Login to OrangeHRM

    Scenario: Succesfully login to OrangeHRM
        Given I open HRM Homepage
        When Enter username "admin" and password "admin123"
        And Click on login button
        Then User must successfully login to the Dashboard page