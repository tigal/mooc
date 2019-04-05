# Written by Nastya

Feature: Getting a certificate via testing
  #As a nonprofessional, who is experienced in programming but whose knowledge is not confirmed
  #I want to pass a quick test to confirm my mastering of Python and get a certificate
  #So that I can attach it to my digital CV

  Scenario: Successful generation of certificate for skills confirmation
    Given I passed Python skill confirmation test with "<percent>" of correct answers
    And certificate can be generated if "<max_points>" of a test questions are answered correctly
    When I want to get the certificate
    Then the system generates a certificate about confirmed skills with the test name and mark "<percent>"
