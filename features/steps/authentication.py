from behave import *


use_step_matcher("parse")


@when(u'I click on "Log in" link')
def step_impl(context):
    context.browser.find_by_name("login_link").first.click()


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_name('login_form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_name('login_button').first.click()


@then(u'I am logged in as "{username}"')
def step_impl(context, username):
    user_section = context.browser.find_by_name('user_session').first.value
    assert user_section.find(username) != -1
