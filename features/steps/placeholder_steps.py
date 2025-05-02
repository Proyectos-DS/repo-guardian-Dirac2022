from behave import given, when, then

@given('nothing')
def step_impl(context):
    pass


@when('nothing happens')
def step_impl(context):
    pass


@then('everything is oke')
def step_impl(context):
    assert True