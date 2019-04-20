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
