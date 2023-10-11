Feature: Test of Buzz page features

    Background:
        Given Opem Orange HRM on Buzz page
        And Login to Orange HRM with "Admin" and "admin123"

    Scenario Outline: Add post
        When Put message "<message>"
        And Click Post button
        Then Check if massage "<message>" appeared

        Examples:
            | message      |
            | Hello there! |

    Scenario: Give like
        When Check the likes count on newest post
        And Give like on newest post
        Then Check if the likes count increased by one
    
    Scenario Outline: Add comment
        When Click the Comment button
        And Write message "<message>"
        And If Show More button is visible click it
        Then Check if comment with "<message>" appeared

        Examples:
            | message      |
            | That's grate |

    Scenario Outline: Share post
        When Click share button below post
        And Send message "<message>"
        And Click share button to publish
        Then Check if new post with "<message>" message appeared

        Examples:
            | message |
            | WOW!    |
