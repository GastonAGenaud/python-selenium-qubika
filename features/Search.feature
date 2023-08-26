Feature: Google Search Functionality

  @smoke
  Scenario: Validate Google Search and Filters
    Given I am on the Google homepage
    Then I should see the correct title, menu and search bar
    When I search for "testxng"
    Then I should see the suggestion "testing"
    When I click on the suggestion "testing"
    Then I should see the search results for "testing"
    When I click on the "Imágenes" filter
    Then I should see the images results for "testing" with the filter "Images"
