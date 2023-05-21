Feature: Delete Review
  In order to delete my opinion about a book
  As a user
  I want to delete my review


  Background: There is one book, two users and one review
    Given Exists a book with title "Test Book" isbn "1111111111111" synopsis "This is a testing book!" genres "Fiction" language "English" cover "https://marketplace.canva.com/EAFMf17QgBs/1/0/1003w/canva-green-and-yellow-modern-book-cover-business-Ah-do4Y91lk.jpg" author "Test Author" publisher "Test Publisher"
    And Exists a user "user" with password "pass12345"
    And Exists a user "another_user" with password "pass12345"
    And Exists a review for the book "Test Book" posted by "user" with title "My first review!" body "Very good!" and rating "3"