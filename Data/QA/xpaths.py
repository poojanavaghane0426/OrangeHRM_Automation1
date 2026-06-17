# XPaths
USERNAME_FIELD ="//label[contains(text(),'Username')]/following::input[1]"
PASSWORD_FIELD = "//label[contains(text(),'Password')]/following::input[1]"
LOGIN_BUTTON = "//button[@type='submit']"

DASHBOARD_TEXT = "//h6[contains(text(),'Dashboard')]"
ERROR_MESSAGE = "//p[contains(@class,'oxd-alert-content-text')]"

PROFILE_DROPDOWN = "//span[contains(@class,'userdropdown-tab')]"
LOGOUT_BUTTON = "//a[text()='Logout']"

LOGIN_HEADER = "//input[@name='username']/preceding::h5[1]"
LOGIN_PAGE_TEXT = "//h5[contains(text(),'Login')]"

MENU_XPATH = "//span[normalize-space()='REPLACE_MENU']"

ADD_EMPLOYEE_BUTTON = "//a[text()='Add Employee']"
FIRST_NAME_FIELD = "//input[@name='firstName']"
LAST_NAME_FIELD = "//input[@name='lastName']"
SAVE_BUTTON = "//button[@type='submit' and normalize-space()='Save']"

PERSONAL_DETAILS_TEXT = "//h6[normalize-space()='Personal Details']"
LOADER = "//div[contains(@class,'oxd-form-loader')]"

EMPLOYEE_NAME_SEARCH = "//input[@placeholder='Type for hints...']"
SEARCH_BUTTON = "//button[@type='submit']"

EMPLOYEE_RECORD = "//div[contains(normalize-space(),'REPLACE_EMPLOYEE')]"

