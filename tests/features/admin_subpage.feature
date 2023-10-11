Feature: Test of Admin page features

    Background:
        Given Opem Orange HRM on Admin page
        And Login to Orange HRM with "Admin" and "admin123"

    Scenario Outline: Add system user
        When Check if "<username>" exist and delete it
        And Click +Add button
        And Click on User Role field and select admin
        And Type "<name>" in Employee Name and select first one
        And Select Enabled status
        And Enter Username "<username>"
        And Type Password "<password>" and confirm it
        And Click Save button
        Then Search for user "<username>"
        And Confirm that "<username>" appears

         Examples:
            | name | username       | password  |
            | a    | Roman Giertych | Password1 |

    Scenario Outline: Add job title
        When Click on Job and select Job Titles
        And If "<job title>" with "<job description>" exist then delete it
        And Click Add button
        And Set Job Title to "<job title>"
        And Set Job Description to "<job description>"
        And Click Save button
        Then Check if "<job title>" appeares on page

        Examples:
            | job title         | job description |
            | Backend Developer | Uses PHP        |

    Scenario Outline: Add pay grade
        When Click on job and select pay grade
        And If "<name>" and "<currency_check>" exist delete record
        And Click add button
        And Set "<name>" and click save button
        And Click add button and select "<currency>"
        And Set "<minimum>" and "<maximum>" salary and click save button
        Then Return to pay grade page
        And Check if "<name>" whit proper "<currency_check>" occurs

        Examples:
            | name         | currency           | minimum | maximum | currency_check |
            | Phil Clloins | PLN - Polish Zloty | 4000    | 6000    | Polish Zloty   |
    
    Scenario Outline: Add work shift
        When Click on job and select work shift
        And If "<shift_name>" from "<work_from>" to "<work_to>" exist delete it
        And Click add button
        And Set "<shift_name>"
        And Set "<work_from>" and "<work_to>"
        And In assigned employess type "<name>", choose first one and click save button
        Then Check if "<shift_name>" from "<work_from>" to "<work_to>" appeares
        
        Examples:
            | shift_name | work_from | work_to  | name |
            | Day shift  | 08:00 AM  | 04:00 PM | a    |