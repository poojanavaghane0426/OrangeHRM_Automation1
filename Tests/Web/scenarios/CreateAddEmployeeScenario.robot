*** Settings ***
Resource    ../support/Support.robot

*** Test Cases ***
Add Employee Scenario
    [Documentation]    Verify user can add employee successfully

    Given the OrangeHRM login page is open
    When the user logs in with valid credentials
    When the user adds a new employee
    Then employee should be added successfully

Search Employee Scenario
    [Documentation]    Verify employee can be searched successfully

    Given the OrangeHRM login page is open
    When the user logs in with valid credentials
    When the user searches for an employee
    Then employee records should be displayed

