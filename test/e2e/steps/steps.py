from behave import given, when, then, step
from hamcrest import assert_that, equal_to, has_entries

from lexicorm.model_to_dict import model_to_dict
from test.fixtures import get_fixtures, get_fixtures_with_relationship


@given(u'I have no database model')
def no_model(context):
    context.model = None


@when(u'I call model_to_dict on the model "{model_name}"')
def model_dict_on_model(context, model_name):
    if model_name != 'None':
        model = getattr(context, model_name)
    else:
        model = context.model
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
def have_musician(context):
    fixtures = get_fixtures_with_relationship()
    context.musician = fixtures['musician']
    context.band = fixtures['band']


@then('I get a dictionary with a key "{key}" that is a list')
def get_dictionary(context, key):
    assert_that(type(context.result[key]), equal_to(list))


@step("""one of the objects in the '{object_name}'
         list contains the key '{key}' with the value '{value}'""")
def find_dict(context, object_name, key, value):
    things = context.result[object_name]

    for thing in things:
        if key in thing:
            if value is not None:
                assert_that(thing[key].lower(), equal_to(value.lower()))
            return
