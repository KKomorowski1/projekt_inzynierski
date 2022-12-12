Feature: Elements Web Tables
  Test features available in landing_page->elements_page->web_tables_page

  Scenario: Add person to table
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on web tables in the menu
    And I click add button
    And I enter "Kacper" as first name
    And I enter "Komorowski" as last name
    And I enter "kakacper23@gmail.com" as email
    And I enter "26" as age
    And I enter "12000" as salary
    And I enter "Testing" as department
    And I click submit button in form
    Then I verify data is in table: "Kacper", "Komorowski", "kakacper23@gmail.com", "26", "12000", "Testing"

  Scenario: Delete person
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on web tables in the menu
    And I click add button
    And I enter "Kacper" as first name
    And I enter "Komorowski" as last name
    And I enter "kakacper23@gmail.com" as email
    And I enter "26" as age
    And I enter "1200" as salary
    And I enter "Testing" as department
    And I click submit button in form
    Then I verify data is in table: "Kacper", "Komorowski", "kakacper23@gmail.com", "26", "1200", "Testing"
    When I click trash can on user number "4"
    Then I verify data is not in table: "Kacper", "Komorowski", "kakacper23@gmail.com", "26", "1200", "Testing"


  Scenario: Edit person
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on web tables in the menu
    And I click add button
    And I enter "Kacper" as first name
    And I enter "Komorowski" as last name
    And I enter "kakacper23@gmail.com" as email
    And I enter "26" as age
    And I enter "1200" as salary
    And I enter "Testing" as department
    And I click submit button in form
    Then I verify data is in table: "Kacper", "Komorowski", "kakacper23@gmail.com", "26", "1200", "Testing"
    When I click edit on user number "4"
    And I enter "Kacper123" as first name
    And I enter "Komorowski123" as last name
    And I enter "123@gmail.com" as email
    And I enter "41" as age
    And I enter "12011" as salary
    And I enter "dev" as department
    And I click submit button in form
    Then I verify data is in table: "Kacper123", "Komorowski123", "123@gmail.com", "41", "12011", "dev"

