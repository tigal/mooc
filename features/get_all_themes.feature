Feature: Miscellaneous

  Scenario: Get all themes of the course
    Given there are several themes in the course
      | course_id |theme_id | points |
      | 4         |3        | 5      |
      | 4         |4        | 10     |
      | 4         |1        | 15     |
      | 4         |2        | 15     |
    When there is a need to get a list of these themes wherever
    Then systems prints this list