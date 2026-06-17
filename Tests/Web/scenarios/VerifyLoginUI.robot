*** Settings ***
Resource    ../support/Support.robot

*** Test Cases ***

Verify Login Page UI Scenario
    [Documentation]    Verify login page structure using preceding locator

    Given the OrangeHRM login page is open
    Then the login page UI should be correct
