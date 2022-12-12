Feature: Elements radio button
  Test features available in landing_page->elements_page->radio_button_page

  Scenario: I select yes button and verify text at the bottom
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on radio button in the menu
    When I select 'Yes' radio button
    Then I verify bottom text "Yes" with radio button selected

  Scenario: I select yes button and verify text at the bottom
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on radio button in the menu
    When I select 'Impressive' radio button
    Then I verify bottom text "Impressive" with radio button selected