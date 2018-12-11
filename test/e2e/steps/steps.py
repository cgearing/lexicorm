from behave import given, when, then
from hamcrest import assert_that, equal_to, has_entries

from lexicorm.model_to_dict import model_to_dict
from test.fixtures import get_fixtures

fixtures = get_fixtures()


@given(u'I have no database model')
def no_model(context):
    context.model = None


@when(u'I call model_to_dict on the model')
def model_dict_on_model(context):
    context.result = model_to_dict(context.model)


@then(u'I get an empty dictionary as the result')
def empty_dict(context):
    assert_that(context.result, equal_to({}))


@given("I have a musician")
def musician(context):
    context.model = fixtures['musician']


@then('I get a dictionary with a key "{key}" with the value "{value}"')
def get_dictionary_with_key(context, key, value):
    assert_that(context.result, has_entries({key: equal_to(value)}))
