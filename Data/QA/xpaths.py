#  LOGIN PAGE LOCATORS
USERNAME_FIELD = "//input[@name='username']"
PASSWORD_FIELD = "//input[@name='password']"
LOGIN_BUTTON   = "//button[@type='submit']"
LOGIN_HEADER   = "//h5[normalize-space()='Login']"
ERROR_MESSAGE  = "//p[contains(@class,'alert-content-text')]"

#  DASHBOARD LOCATORS
DASHBOARD_TEXT = "//h6[normalize-space()='Dashboard']"

#  LOGOUT LOCATORS
PROFILE_DROPDOWN = "//span[contains(@class,'userdropdown-tab')]"
LOGOUT_BUTTON    = "//a[normalize-space()='Logout']"
LOGIN_PAGE_TEXT  = "//h5[normalize-space()='Login']"


#  MENU LOCATORS
MENU_XPATH = "//span[normalize-space()='REPLACE_MENU']"


#  ADD EMPLOYEE (PIM)
ADD_EMPLOYEE_BUTTON = "//a[normalize-space()='Add Employee']"
FIRST_NAME_FIELD    = "//input[@name='firstName']"
LAST_NAME_FIELD     = "//input[@name='lastName']"
SAVE_BUTTON         = "//button[normalize-space()='Save']"
PERSONAL_DETAILS_TEXT = "//h6[normalize-space()='Personal Details']"
LOADER = "//div[contains(@class,'oxd-form-loader')]"


#  SEARCH EMPLOYEE (PIM)
EMPLOYEE_NAME_SEARCH = "//input[@placeholder='Type for hints...']"
SEARCH_BUTTON        = "//button[normalize-space()='Search']"
EMPLOYEE_RECORD      = "//div[contains(normalize-space(),'REPLACE_EMPLOYEE')]"
