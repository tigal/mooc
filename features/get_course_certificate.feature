# feature written by Nastya
# steps written by Galina

Feature: Getting a course certificate
  # As a recent graduate who wants to apply for a vacancy in a week
  #I want to get a proof of my skills in programming on Python
  #So that I can attach it to my digital CV

  #comments: I apply for Junior JS Developer vacancy

  Scenario: Successful certificate generating
    Given Intermediate JavaScript course themes
          | course_id | name | points |
          | 1         | j1   | 5      |
          | 1         | j2   | 10     |
          | 1         | j3   | 15     |
          | 1         | j4   | 10     |
          | 1         | j5   | 15     |
    And I passed 3 themes in Intermediate JavaScript course
          | course_id | theme_id | points |
          | 1         | 1        | 5      |
          | 1         | 2        | 10     |
          | 1         | 3        | 15     |
    And To get the certificate more than 30% of this course should be done
    When I want to get a certificate
    Then The system generate a certificate with the list of passed topics and progress mark 60%

