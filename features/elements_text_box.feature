Feature: Elements text box
  Test features available in landing_page->elements_page->text_box_page

  Scenario: Happy Path all data is filled correctly
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


  Scenario: Happy Path Full name is not filled
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I enter email "kakacper23@gmail.com"
    And I enter current address "swietojanska 18"
    And I enter permanent address "ten sam"
    And I click submit button
    Then I verify that form was processed


  Scenario: Happy Path Current address is not filled
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I enter full name "Kacper Komorowski"
    And I enter email "kakacper23@gmail.com"
    And I enter permanent address "ten sam"
    And I click submit button
    Then I verify that form was processed


  Scenario: Happy Path Permanent address not filled
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I enter full name "Kacper Komorowski"
    And I enter email "kakacper23@gmail.com"
    And I enter current address "swietojanska 18"
    And I click submit button
    Then I verify that form was processed

  Scenario: Negative path email has wrong format
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I enter full name "Kacper Komorowski"
    And I enter email "kakacper23@gmail."
    And I enter current address "swietojanska 18"
    And I enter permanent address "ten sam"
    And I click submit button
    Then I verify email has red border


  Scenario: Negative path empty form
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on text box in the menu
    And I click submit button
    Then I verify that result table did not appear