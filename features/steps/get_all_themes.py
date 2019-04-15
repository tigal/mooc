from behave import given, when, then

from models.course import CourseTheme


@given('Python course with course_id=4')
def python_course(context):
     try:
         context.course = Course.get(Course.name.where(Course.course_id == 4))
     except Course.DoesNotExist:
         Course.create(course_id=4,
                       course_name='Python')
         context.course = Course.get(Course.name.where(Course.course_id == 4))


@given('the list of themes')
def reading_themes(context):
    for row in context.table:
        try:
            context.themes_list =  context.course.get_themes()
        except CourseTheme.DoesNotExist:
            CourseTheme.create(course_id = row['course_id'],
                               theme_id=row['theme_id'],
                               points=row['points'])
                                #name?
        if context.themes_list is empty:
            context.themes_list = context.course.get_themes()


@when("there is a need to get a list of the course themes wherever")
def need_to_print_themes_list(context):
    context.need_to_print_themes_list = True


@then("systems prints this list")
def printing_themes_list(context):
    if context.need_to_print_themes_list:
        print(context.themes_list)
