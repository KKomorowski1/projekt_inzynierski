Feature: Elements check box
  Test features available in landing_page->elements_page->check_box_page

#  Scenario Outline: Clicking on <value> and verifying message at the bottom
#    Given I open demoqa website
#    When I click Elements Card
#    Then I verify that elements page was opened successfully
#    When I click on check box in the menu
#    When I expand full tree
#    When I select <value> checkbox
#    Then Verify text of what was selected is showing
#
#    Examples: Test
#    | value     |
#    | Desktop   |
#    | Documents |
#    | Office    |
#    | Downloads |


  Scenario: I click on check box next to Desktop
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on check box in the menu
    When I expand full tree
    When I select "Desktop" checkbox
    Then Verify text of what was selected is showing

  Scenario: I click on check box next to Documents
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on check box in the menu
    When I expand full tree
    When I select "Documents" checkbox
    Then Verify text of what was selected is showing


  Scenario: I click on check box next to Office
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on check box in the menu
    When I expand full tree
    When I select "Office" checkbox
    Then Verify text of what was selected is showing


  Scenario: I click on check box next to Downloads
    Given I open demoqa website
    When I click Elements Card
    Then I verify that elements page was opened successfully
    When I click on check box in the menu
    When I expand full tree
    When I select "Downloads" checkbox
    Then Verify text of what was selected is showing