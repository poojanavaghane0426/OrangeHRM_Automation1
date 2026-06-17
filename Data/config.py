import os
 
ENV = os.getenv("ENV", "QA").upper()
 
if ENV == "QA":
    DATA_PATH = "../../../Data/QA/data.py"
    URL_PATH = "../../../Data/QA/urls.py"
    XPATH_PATH = "../../../Data/QA/xpaths.py"
    print(f"Running tests in QA environment")
 
elif ENV == "DEV":
    DATA_PATH = "../../../Data/DEV/data.py"
    URL_PATH = "../../../Data/DEV/urls.py"
    XPATH_PATH = "../../../Data/DEV/xpaths.py"
    print(f"Running tests in DEV environment")
 
else:
    raise Exception(f"Unsupported Environment : {ENV}")