*** Settings ***
Resource    ../support/Support.robot

*** Test Cases ***

Positive Login Scenario
    [Documentation]    Verify that user can login with valid credentials

    Given the OrangeHRM login page is open
    When the user logs in with valid credentials
    Then the user should be on dashboard


Negative Login Scenario
    [Documentation]    Verify that user cannot login with invalid credentials

    Given the OrangeHRM login page is open
    When the user logs in with invalid credentials
    Then error message should be displayed
