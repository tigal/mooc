Feature: Certificate Generation

  Scenario: Unverified user requested certificate
    Given student with id 1234 requests certificate for course_id 2
    And there is no verified userdata in DB
    When system verifies userdata for certificate
    Then there is an error that userdata should be verified
    And status of certificate is "refused"

   Scenario: Verified user requested certificate
    Given student with id 1234 requests certificate for course_id 2
    And there is verified userdata in DB
    When system verifies userdata for certificate
    Then status of certificate is "user_verified"

  Scenario: Requested certificate update
    Given student with id 1234 requests certificate with id 9876
    When system checks certificate in DB
    Then status of certificate is "updated"
     And system replaces old certificate

  Scenario: Requested certificate is expired
    Given student with id 1234 requests certificate with id 9876
    And certificate is expired
    When system checks certificate in DB
    Then status of certificate is "updated"
     And system replaces old certificate