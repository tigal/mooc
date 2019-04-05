# Written by Galya

Feature: Searching for course

  Scenario: Find courses for some specialization
     Given a set of specializations
        | name             |
        | Programming      |
        | Natural Sciences |
     And a set of providers
        | name  |
        | ITMO  |
        | SPSU  |
     And  a set of courses
        | name           | provider_id | spec_id |
        | Java           | 1           | 1       |
        | JavaScript     | 1           | 1       |
        | Biology        | 1           | 2       |
        | Python         | 2           | 1       |
    When we search for courses in "Programming"
    Then we will find 3 Programming items
