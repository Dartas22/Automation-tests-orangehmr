Feature: Add employee claims

    Scenario Outline: Add claim
        Given Opem Orange HRM on Claim page
        When Login to Orange HRM with "Admin" and "admin123"
        And Click Assign Claim button
        And Input empleyee name "<name>"
        And Select Event "<event>"
        And Select Currency "<currency>"
        And Add remark "<remark>"
        And Click Create button
        Then Check if Assign Claim displays

        Examples:
            | name | event            | currency      | remark |
            | a    | Travel Allowance | Belize Dollar | abc    |