#!/bin/sh

# AIzaSyDQkfX1Y4NMM9qRK0IWSKV4ujRsZi2pUJ8
# AIzaSyDQkfX1Y4NMM9qRK0IWSKV4ujRsZi2pUJ8

TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbklkIjoiMTdhYTQ3NWMtNjdjNS00OTE4LWJkMGItNWVkNGQwZDM4ZjdlIiwiaWF0IjoxNjAyNjkxMzUxLCJhdWQiOiJ0cmlmYWN0YSIsImlzcyI6ImRhdGFwcmVwLWFwaS1hY2Nlc3MtdG9rZW5AdHJpZmFjdGEtZ2Nsb3VkLXByb2QuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJkYXRhcHJlcC1hcGktYWNjZXNzLXRva2VuQHRyaWZhY3RhLWdjbG91ZC1wcm9kLmlhbS5nc2VydmljZWFjY291bnQuY29tIn0.g6Sg1Fqeqnj8HSGleHAzFqpX1icbY5oOSfVjnXCQuyBiWfrYMXFcMTla88EWRzTQtsBZvb-uD06VzH7pJ8drk2NSqZlL1F1bsSBkyYcYbYEasucI7z7hVUrva5cGmiBajmyYd3COEJeuNk00nj5rq7xkvBEE-5mlybCbH3wMhKgm0FX9_1PT_yeDXt36lKgGs1dofuX5tT8VL2tBWDRdIdV-aj0uGidvmWcyN2CPOYmaOpqe2oCZP-xfuEfZxLTeY_48-Rc7G_tXRJnSGWwf6YPnI0jNAGHv6VdPO5VcYWsFdowenqGBSmzPu8tvMyLbnxx0kE_C74_XfYYidJSogA

#curl -X POST 'https://api.clouddataprep.com/v4/jobGroups' -H 'Content-Type: application/json' -H 'Authorization: Bearer AIzaSyDQkfX1Y4NMM9qRK0IWSKV4ujRsZi2pUJ8' -d '{ "wrangleDataset": { "id": "" } }'
curl -X GET 'https://api.clouddataprep.com/v4/jobGroups/6744503' -H 'Content-Type: application/json' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbklkIjoiMTdhYTQ3NWMtNjdjNS00OTE4LWJkMGItNWVkNGQwZDM4ZjdlIiwiaWF0IjoxNjAyNjkxMzUxLCJhdWQiOiJ0cmlmYWN0YSIsImlzcyI6ImRhdGFwcmVwLWFwaS1hY2Nlc3MtdG9rZW5AdHJpZmFjdGEtZ2Nsb3VkLXByb2QuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJkYXRhcHJlcC1hcGktYWNjZXNzLXRva2VuQHRyaWZhY3RhLWdjbG91ZC1wcm9kLmlhbS5nc2VydmljZWFjY291bnQuY29tIn0.g6Sg1Fqeqnj8HSGleHAzFqpX1icbY5oOSfVjnXCQuyBiWfrYMXFcMTla88EWRzTQtsBZvb-uD06VzH7pJ8drk2NSqZlL1F1bsSBkyYcYbYEasucI7z7hVUrva5cGmiBajmyYd3COEJeuNk00nj5rq7xkvBEE-5mlybCbH3wMhKgm0FX9_1PT_yeDXt36lKgGs1dofuX5tT8VL2tBWDRdIdV-aj0uGidvmWcyN2CPOYmaOpqe2oCZP-xfuEfZxLTeY_48-Rc7G_tXRJnSGWwf6YPnI0jNAGHv6VdPO5VcYWsFdowenqGBSmzPu8tvMyLbnxx0kE_C74_XfYYidJSogA'

curl -X GET 'https://api.clouddataprep.com/v4/jobGroups/6744503/jobs' -H 'Content-Type: application/json' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbklkIjoiMTdhYTQ3NWMtNjdjNS00OTE4LWJkMGItNWVkNGQwZDM4ZjdlIiwiaWF0IjoxNjAyNjkxMzUxLCJhdWQiOiJ0cmlmYWN0YSIsImlzcyI6ImRhdGFwcmVwLWFwaS1hY2Nlc3MtdG9rZW5AdHJpZmFjdGEtZ2Nsb3VkLXByb2QuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJkYXRhcHJlcC1hcGktYWNjZXNzLXRva2VuQHRyaWZhY3RhLWdjbG91ZC1wcm9kLmlhbS5nc2VydmljZWFjY291bnQuY29tIn0.g6Sg1Fqeqnj8HSGleHAzFqpX1icbY5oOSfVjnXCQuyBiWfrYMXFcMTla88EWRzTQtsBZvb-uD06VzH7pJ8drk2NSqZlL1F1bsSBkyYcYbYEasucI7z7hVUrva5cGmiBajmyYd3COEJeuNk00nj5rq7xkvBEE-5mlybCbH3wMhKgm0FX9_1PT_yeDXt36lKgGs1dofuX5tT8VL2tBWDRdIdV-aj0uGidvmWcyN2CPOYmaOpqe2oCZP-xfuEfZxLTeY_48-Rc7G_tXRJnSGWwf6YPnI0jNAGHv6VdPO5VcYWsFdowenqGBSmzPu8tvMyLbnxx0kE_C74_XfYYidJSogA'
