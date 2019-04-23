Feature: Certificate Generation

  Scenario: Unverified user requested certificate
    Given certificate is requested
    And there are no verified userdata in DB
    When system verifies userdata for certificate
    Then there is an error that userdata should be verified
    And status of certificate is 'refused'

   Scenario: Verified user requested certificate
    Given certificate is requested
    And there are verified userdata in DB
    When system verifies userdata for certificate
    Then status of certificate is 'userdata verified'
     And system starts to validate certificate

  Scenario: Requested certificate update
    Given student with id 1234 requests certificate with id 9876
    And there is existing certificate for student 1234 with id 9876 in DB
    When system checks certificate in DB
    Then status of certificate is "updated"
     And system replaces old certificate