from hamcrest import assert_that, has_key

from lexicorm.conversion import python_dict_to_json_dict, json_dict_to_python_dict


def test_python_dict_to_json_dict() -> None:

    input = {'python_case': 'dont_change_me',
             'alreadyJsonCase': 'dont_change_me_either'}

    result = python_dict_to_json_dict(input)

    assert_that(result, has_key('pythonCase'))
    assert_that(result, has_key('alreadyJsonCase'))

def test_json_dict_to_python_dict() -> None:

    input = {'jsonCase': 'dont_change_me',
             'python_case': 'dont_change_me_either'}

    result = json_dict_to_python_dict(input)

    assert_that(result, has_key('json_case'))
    assert_that(result, has_key('python_case'))
