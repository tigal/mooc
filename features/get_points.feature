# Written by Galya

Feature: Completing tests

  Scenario: Passing test during course
    Given a set of themes in course
       | course_id | name                  | max_points |
       | 4         | Basic of programming  | 30         |
       | 4         | Python functions      | 40         |
       | 4         | Pandas                | 40         |
     And a set of student answers
        | student_id | course_id |theme_id | points |
        | 4545       | 4         | 3        | 5      |
        | 4545       | 4         | 3        | 10     |
        | 4545       | 4         | 3        | 15     |
        | 4545       | 4         |3        | 15      |
    When we want to know 4545 students points in Pandas
    Then we get 35


         #And  a set of questions
     #   | theme_id | question_name  | points |
     #   |   3      | Python_1       | 5      |
     #   |   3      | Python_2       | 15     |
     #   |   3      | Python_3       | 10     |