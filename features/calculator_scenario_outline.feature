Feature: Calculator
  In order to perform basic math operations
  As a user
  I want to use a calculator

  Background:
      Given I am on the calculator page

  Scenario Outline: Calculator
      Given I have entered <first> into the calculator
      When I press <operation>
      And I have entered <second> into the calculator
      And I press equal
      Then the result should be <result> on the screen

      Examples: All the operations with two numbers
      | first | second | operation | result |
      |  2    |   2    |    add    |   4    |
      |  3    |   2    |  subtract |   1    |
      |  3    |   3    |  multiply |   9    |
      |  6    |   2    |   divide  |   3    |

    # @todo: Our tests are failing for subtract and divide, we need to fix them