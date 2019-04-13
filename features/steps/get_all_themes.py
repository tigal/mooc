from behave import given, when, then

from models.course import CourseTheme


@given('there are several themes in the course')
def reading_themes(context):
    for row in context.table:
        try:
            context.themes_list = CourseTheme.get(CourseTheme.name.where(CourseTheme.theme_id == row['theme_id']))
        except CourseTheme.DoesNotExist:
            CourseTheme.create(theme_id=row['theme_id'],
                               points=row['points'])
                                #name?

@when("there is a need to get a list of these themes wherever")
def need_to_print_themes_list(context):
    context.need_to_print_themes_list = True


@then("systems prints this list")
def printing_themes_list(context):
    if context.need_to_print_themes_list:
        print(context.themes_list)
