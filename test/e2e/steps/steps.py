from behave import given, when, then
from hamcrest import assert_that, equal_to, has_entries

from lexicorm.model_to_dict import model_to_dict
from test.fixtures import get_fixtures, get_fixtures_with_relationship


@given(u'I have no database model')
def no_model(context):
    context.model = None


@when(u'I call model_to_dict on the model "{model_name}"')
def model_dict_on_model(context, model_name):
    model = getattr(context, model_name)
    context.result = model_to_dict(model)


@then(u'I get an empty dictionary as the result')
def empty_dict(context):
    assert_that(context.result, equal_to({}))


@given("I have a musician")
def musician(context):
    fixtures = get_fixtures()
    context.musician = fixtures['musician']


@then('I get a dictionary with a key "{key}" with the value "{value}"')
def get_dictionary_with_key(context, key, value):
    assert_that(context.result, has_entries({key: equal_to(value)}))


@given("I have a musician with a related band")
def step_impl(context):
    fixtures = get_fixtures_with_relationship()
    context.musician = fixtures['musician']
    context.band = fixtures['band']
