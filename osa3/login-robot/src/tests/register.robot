*** Settings ***
Resource          ../resource.robot
Test Setup        Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    testikalle    salasana123    
    Output Should Contain    New user registered