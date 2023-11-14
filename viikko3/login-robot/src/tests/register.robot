*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Crete User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  testisalasana1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testisalasana1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ll  testisalasana1
    Output Should Contain  Username is too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  testi1  testisalasana1
    Output Should Contain  Username is invalid

Register With Valid Username And Too Short Password
    Input Credentials  testi  testi12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testi  testisalasana
    Output Should Contain  Password is invalid

*** Keywords ***
Input New Command And Crete User
    Create User  kalle  kalle123
    Input New Command
    
    