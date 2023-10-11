Feature: Test of Directory page features

    Background:
        Given Opem Orange HRM on Directory page
        And Login to Orange HRM with "Admin" and "admin123"

    Scenario: Find employee by name
        When Type "a" in Employee Name and select first one
        And Get name of selected employee
        And Click Search button
        Then Check if employee with proper name appeared

    Scenario: Find emplyee by job title
        When Select Job Title and choose the first one
        And Get name of selected job
        And Click Search button
        Then Check if first employee has proper job title

    Scenario Outline: Check number of employees by location
        When Select Location and choose "<number>" position
        And Click search button
        And Check how many results there are
        Then Check if right amount of employees displays

        Examples:
            | number |
            | 1      |
            | 2      |
            | 3      |
            | 4      |