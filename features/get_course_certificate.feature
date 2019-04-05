# Written by Nastya, corrected by Galya [comments]

Feature: Getting a course certificate
  # As a recent graduate who wants to apply for a vacancy in a week
  #I want to get a proof of my skills in programming on Python
  #So that I can attach it to my digital CV

  #comments: I apply for Junior JS Developer vacancy

  Scenario: Successful certificate generating
    Given I passed 3 of 5 themes in 'Intermediate JavaScript' course
    And To get the certificate more than 30% of this course should be done
    When I want to get a certificate
    Then The system generate a certificate with the list of passed topics and progress mark 60%

