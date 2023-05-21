from behave import *

use_step_matcher("parse")


@when(u'I click on "Create a new review" button')
def step_impl(context):
    context.browser.find_by_name('create_review_button').first.click()


@then(u'I am redirected to the login page')
def step_impl(context):
    browser_url = context.browser.url
    login_url = context.get_url('login')
    assert browser_url.startswith(login_url)


@then(u'I can\'t create the review via url for the book "{book_title}"')
def step_impl(context, book_title):
    from bookapp.models import Book
    book_id = Book.objects.get(title=book_title).id
    context.browser.visit(context.get_url('review_create', book_id=book_id))

    browser_url = context.browser.url
    login_url = context.get_url('login')
    assert browser_url.startswith(login_url)