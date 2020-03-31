import allure
import pytest
from pytestDemo.test_mark_param_request1 import test_login
from pytestDemo.test_mark_param_request1 import login_r


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    print(arg1,arg2)


def test_with_imported_step():
    passing_step()
    test_login(login_r)


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
