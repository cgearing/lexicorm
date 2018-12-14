Feature: model_to_dict
  Scenario: calling model_to_dict on nothing
    Given I have no database model
    When I call model_to_dict on the model "None"
    Then I get an empty dictionary as the result

  Scenario: calling model_to_dict on a basic model
    Given I have a musician
    When I call model_to_dict on the model "musician"
    Then I get a dictionary with a key "given_name" with the value "Jimi"

  Scenario: calling model_to_dict on a model with an eager relationship
    Given I have a musician with a related band
    When I call model_to_dict on the model "musician"
    Then I get a dictionary with a key "bands" that is a "list"
     And one of the objects in the "bands" list contains the key "name" with the value "Band of Gypsys"

  Scenario: calling model_to_dict on a model with a lazy relationship
    Given I have a musician with a related band
    When I call model_to_dict on the model "band"
    Then I get a dictionary with a key "musician" that is a "integer"

  Scenario: calling model_to_dict on a model with a lazy relationship and get_lazy is true
    Given I have a musician with a related band
    When I call model_to_dict on the model "band" and get_lazy is true
    Then I get a dictionary with a key "musician" that is a "dict"
     And the object has a key "given_name" with the value "Jimi"