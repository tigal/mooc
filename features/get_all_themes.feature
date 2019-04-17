Feature: Miscellaneous

  Scenario: Get all themes of the course 'Python'
    Given Python course
    Given the list of themes
      | course_id | name | points |
      | 4         | p1   | 5      |
      | 4         | p2   | 10     |
      | 4         | p3   | 15     |
      | 4         | p4   | 15     |
    When there is a need to get a list of the course themes wherever
    Then systems prints this list