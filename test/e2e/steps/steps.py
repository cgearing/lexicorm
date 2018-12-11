from behave import *
from hamcrest import assert_that, equal_to

from lexicorm.model_to_dict import model_to_dict


@given(u'I have no database model')
def step_impl(context):
    context.model = None


@when(u'I call model_to_dict on the model')
def step_impl(context):
    context.result = model_to_dict(context.model)


@then(u'I get an empty dictionary as the result')
def step_impl(context):
    assert_that(context.result, equal_to({}))
