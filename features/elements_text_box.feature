Feature: test

  Scenario: test
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I enter full name "Kacper Komorowski"
    And I enter email "kakacper23@gmail.com"
    And I enter current address "swietojanska 18"
    And I enter permanent address "ten sam"
    And I click submit button
    Then I verify that form was processed