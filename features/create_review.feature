Feature: Create Review
  In order to share my opinion about a book
  As a user
  I want to create a review

  Background: There is a book and a user
    Given Exists a book with title "Test Book" isbn "1111111111111" synopsis "This is a testing book!" genres "Fiction" language "English" cover "https://marketplace.canva.com/EAFMf17QgBs/1/0/1003w/canva-green-and-yellow-modern-book-cover-business-Ah-do4Y91lk.jpg" author "Test Author" publisher "Test Publisher"
    And Exists a user "user" with password "pass12345"

    Scenario: A user who is not logged in can't write a review
        Given I am on the "Test Book" detail page
        When I click on "Create a new review" button
        Then I am redirected to the login page
        And I can't create the review via url for the book "Test Book"