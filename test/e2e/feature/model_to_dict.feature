Feature: model_to_dict
  Scenario: calling model_to_dict on nothing
    Given I have no database model
    When I call model_to_dict on the model "None"
    Then I get an empty dictionary as the result

  Scenario: calling model_to_dict on a basic model
    Given I have a musician
    When I call model_to_dict on the model "musician"
    Then I get a dictionary with a key "given_name" with the value "Jimi"

  Scenario: calling model_to_dict on a model with a relationship
    Given I have a musician with a related band
    When I call model_to_dict on the model "musician"
    Then I get a dictionary with a key "bands" with the value "The Band of Gypsys"