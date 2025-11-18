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
