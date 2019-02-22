*** Settings ***
Library           Library1.py

*** Test Cases ***
Test 1
    ${skus}=    Get Skus    first:1    Second:2
    ${data}=    Json Template1    Name    VERY_SECRET_TOKEN    FirstClient    ASDJOLASDJASLDFJLSAIFJL    223233
    ...    sku_list=${skus}
    Log To Console    ${data}
