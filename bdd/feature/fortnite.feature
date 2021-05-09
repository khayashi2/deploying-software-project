Feature: Fortnite Player ID Query
  As a user,
  I want to know my stats of my Fortnite account
  So that I can know if I played on that account


  Scenario Outline: Fortnite API will query an id to a json of player stats
    When the Fortnite API is queried with "<id>"
    Then the response status code is 404

    Examples: Fornite Query
      | id |
      | 5e70c11741254facbdbf36b88971f1b6 |