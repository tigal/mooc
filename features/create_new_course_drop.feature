## Written by Nastya, corrected by Galina

Feature: Removing themes from course
  #I want to learn Vue.js
  #I don't want to repeat JS-basics that I'm already know
  #I master JS

  Scenario: Removing unnecessary themes from an already made course
    Given there is course that includes both JS-basics and Vue.js themes
      And I want to learn Vue.js only
      And total sum of points must be more than 50 to form a course
      And on Vue.js themes 50 points can be got
     When I remove JS-basics themes from this course
     Then the system creates a new course with Vue.js themes only