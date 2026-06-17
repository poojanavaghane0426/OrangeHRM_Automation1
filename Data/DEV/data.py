
import os

from dotenv import load_dotenv

load_dotenv()

VALID_USERNAME = "Admin"
INVALID_USERNAME = "wronguser"

VALID_PASSWORD = os.environ.get("VALID_PASSWORD")
INVALID_PASSWORD = os.environ.get("INVALID_PASSWORD")

EMPLOYEE_FIRST_NAME = "Pooja"
EMPLOYEE_LAST_NAME = "Navghane"
SEARCH_EMPLOYEE_NAME = "Pooja"  

