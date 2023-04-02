Feature: Gamestop has a functional and searchable site

Scenario: GameStop sells Halo games
    Given I have navigated to https://www.gamestop.com
    When I search for Halo
    Then I find items related to "Halo"


Scenario: GameStop sells Mario games
    Given I have navigated to https://www.gamestop.com
    When I search for Mario
    Then I find items related to "Mario"


Scenario Outline: GameStop sells a variety of games
    | game       | result     |
    | God of War | God of War |
    | Last of Us | Last of Us |
    | Warzone    | Warzone    | 