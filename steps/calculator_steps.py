from behave import *
from calculator import Calculator

@given(u'I am on the calculator page')
def step_impl(context):
    context.calculator = Calculator()

@given('I have entered {number:d} into the calculator')
def given_enter_number(context, number):
    context.calculator = Calculator()
    context.calculator.result = number

@when('I have entered {number:d} into the calculator')
def enter_number(context, number):
    context.calculator.result = number

@when('I press add')
def press_add(context):
    context.calculator.arithmetic_operations("add")

@when('I press subtract')
def press_subtract(context):
    context.calculator.arithmetic_operations("subtract")

@when('I press multiply')
def press_multiply(context):
    context.calculator.arithmetic_operations("multiply")

@when('I press divide')
def press_divide(context):
    context.calculator.arithmetic_operations("divide")

@when('I press equal')
def press_equal(context):
    context.calculator.equal()

@then('the result should be {result:d} on the screen')
def check_result(context, result):
    assert context.calculator.result == result, f"Expected {result}, but got {context.calculator.result}"
