# OrangeHRM Automation Framework

## Project Description
This project is an automation framework built using Robot Framework and Selenium to test OrangeHRM web application.

##  Technologies Used
- Robot Framework
- SeleniumLibrary
- Python
- Git & GitHub

##  Framework Structure
- Data/ → Contains environment data (QA, DEV)
- Tests/ → Contains test cases
- BusinessLogic → Contains reusable keywords
- Support → Mapping layer (BDD)

##  Features
- Login automation
- Logout functionality
- Add Employee
- Search Employee
- UI validation
- Multi-environment support (QA & DEV)

## How to Run

### Run in QA:
```bash
python -m robot Tests/Web/scenarios
