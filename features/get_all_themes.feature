Feature: Miscellaneous

  Scenario: Get all themes of the course 'Python'
    Given Python course with course_id=4
    Given the list of themes
      | course_id | theme_id | points |
      | 3         | 1        | 5      |
      | 4         | 3        | 5      |
      | 4         | 4        | 10     |
      | 4         | 1        | 15     |
      | 4         | 2        | 15     |
    When there is a need to get a list of the course themes wherever
    Then systems prints this list