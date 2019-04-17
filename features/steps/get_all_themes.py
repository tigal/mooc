from behave import given, when, then

from models.course import Course,CourseTheme


@given('Python course')
def python_course(context):
    try:
        context.course = Course.get(Course.name.where(Course.name == "Python"))
    except Course.DoesNotExist:
        Course.create(course_name='Python')
        context.course = Course.select().where(Course.name == "Python")


@given('the list of themes')
def reading_themes(context):
    try:
        context.themes_list = context.course.get_themes()
    except CourseTheme.DoesNotExist:
        for row in context.table:
            CourseTheme.create(course_id=row['course_id'],
                               name=row['name'],
                               points=row['points'])
        if not context.themes_list:
            context.themes_list = context.course.get_themes()


@when("there is a need to get a list of the course themes wherever")
def need_to_print_themes_list(context):
    context.need_to_print_themes_list = True


@then("systems prints this list")
def printing_themes_list(context):
    if context.need_to_print_themes_list:
        print(context.themes_list)
