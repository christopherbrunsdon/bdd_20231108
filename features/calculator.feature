@basic
Feature: Calculator
  In order to perform basic math operations
  As a user
  I want to use a calculator

  Background:
    Given I am on the calculator page

  Scenario: Add two numbers
    Given I have entered 5 into the calculator
    When I press add
    And I have entered 3 into the calculator
    And I press equal
    Then the result should be 8 on the screen

  # @todo: Add you Scenario to add three numbers
