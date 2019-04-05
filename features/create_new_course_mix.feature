# Written by Nastya, corrected by Galina [comments added]
Feature: Course Construction

  Scenario: Adding themes from one course to another course
    Given there is a Python course
    And there is an R course that includes data scienсe lessons I want to learn
    When I choose topics from R course to add to Python course
    Then the system creates a new course
    And the system adds selected topics from Python course to the new course
    And the system adds selected topics from R course to new course
