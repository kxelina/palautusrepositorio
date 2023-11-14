*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Register User And Go To Welcome Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  testi
    Set Password  testi
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi1
    Submit Credentials
    Register Should Fail With Message  Password isn't same

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed
    Log Out
    Set Username  testi
    Set Password  testi123
    Submit Credentials Login
    Login Should Succeed


Login After Failed Registration
    Set Username  testi
    Set Password  testi
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Password is invalid
    Click Login
    Set Username  testi
    Set Password  testi
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Log Out
     Click Link  Continue to main page
     Click Button  Logout

Submit Credentials Login
    Click Button  Login

Click Login
    Click Link  Login

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register User And Go To Welcome Page
    Create User  kalle  kalle123  
    Go To Register Page
    Register Page Should Be Open
