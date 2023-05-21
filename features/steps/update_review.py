from behave import *

use_step_matcher("parse")


@then(u'I can\'t see the "Edit" button')
def step_impl(context):
    assert context.browser.find_by_name("update_review_button").is_empty()


@given(u'I access the url to edit a review of "{book_title}"')
def step_impl(context, book_title):
    from bookapp.models import Book
    from reviews.models import Review
    book_id = Book.objects.get(title=book_title).id
    review_id = Review.objects.get(book_id=book_id).id
    context.browser.visit(context.get_url(
        'review_update', book_id=book_id, pk=review_id))


@when(u'I click on the "Edit" button')
def step_impl(context):
    context.browser.find_by_name("update_review_button").first.click()