Feature: model_to_dict
  Scenario: calling model_to_dict on nothing
    Given I have no database model
    When I call model_to_dict on the model
    Then I get an empty dictionary as the result

  Scenario: calling model_to_dict on a basic model
    Given I have a musician
    When I call model_to_dict on the model
    Then I get a dictionary with a key "given_name" with the value "Jimi"