Feature: Points validation

  Scenario: Unvalidated user's points
    Given student with id 1234 requests certificate for course_id 2
    And student has points less than needed in this course
    When system verifies userdata for certificate
    Then there is an error that there are not enough points
    And status of certificate is "refused"

   Scenario: Validated user's points
    Given student with id 1234 requests certificate for course_id 2
    And student has points more or equal than needed in this course
    When system verifies userdata for certificate
    Then status of certificate is "user_verified"
    And status of certificate is "generated"
