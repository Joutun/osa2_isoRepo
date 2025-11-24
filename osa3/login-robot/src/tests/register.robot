*** Settings ***
Resource          resource.robot
Test Setup        Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    testikalle    salasana123    
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kayttaja    salasana1234
    Output Should Contain    New user registered
    Input New Command
    Input Credentials    kayttaja    toinen1234    
    Output Should Contain    User with username kayttaja already exists

Register With Too Short Username And Valid Password
    Input Credentials    ab    salasana1234    
    Output Should Contain    Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    källe1    salasana1234
    Output Should Contain    Username must consist of only a-z characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  12345a
    Output Should Contain    Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  antti  longEnough
    Output Should Contain    Password must contain at least one number or special character