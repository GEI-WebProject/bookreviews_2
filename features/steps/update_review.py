from behave import *

use_step_matcher("parse")


@then(u'I can\'t see the "Edit" button')
def step_impl(context):
    assert context.browser.find_by_name("update_review_button").is_empty()
