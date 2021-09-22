class LoginPageConstants:
    """Store constants related to Login Page"""

    # Sign in
    SIGN_IN_USERNAME_TEXT = "'user-name'"
    SIGN_IN_USERNAME_XPATH = f".//input[@name= {SIGN_IN_USERNAME_TEXT}]"
    SIGN_IN_PASSWORD_TEXT = "'password'"
    SIGN_IN_PASSWORD_XPATH = f".//input[@name= {SIGN_IN_PASSWORD_TEXT}]"
    SIGN_IN_BUTTON_TEXT = "'login-button'"
    SIGN_IN_BUTTON_XPATH = f".//input[@id= {SIGN_IN_BUTTON_TEXT}]"

    # Messages
    USERNAME_IS_REQUIRED_MESSAGE_TEXT = 'Epic sadface: Username is required'
    USERNAME_IS_REQUIRED_MESSAGE_XPATH = f".//div/form/div[3]/h3[contains(text(), '{USERNAME_IS_REQUIRED_MESSAGE_TEXT}')]"

    # Static credentials:
    STANDARD_USER_USERNAME = 'standard_user'
    LOCKED_OUT_USER_USERNAME = 'locked_out_user'
    PROBLEM_USER_USERNAME = 'problem_user'
    PERFROMANCE_GLITCH_USER_USERNAME = 'performance_glitch_user'
    CORRECT_PASSWORD = 'secret_sauce'
    SHORT_ALPHABETIC_VALUE_LOWER = 'a'
    SHORT_NUMERIC_VALUE = '123'
