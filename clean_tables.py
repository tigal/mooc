# Written by Galya
# -*- coding: utf-8 -*-

from models.student import Student
from models.course import Course, CourseTheme, Question
from models.user_defined import UserDefinedCourse, UserDefinedTheme
from models.student_answers import StudentAnswerQuestion,StudentFinishedTheme
from models.provider import Provider
from models.specialization import Specialization
from models.schedule import Schedule
from models.certificate import CertificateCourse, CertificateSpec


def clean_tables():
    Student.delete()
    Course.delete()
    CourseTheme.delete()
    Question.delete()
    UserDefinedCourse.delete()
    UserDefinedTheme.delete()
    StudentAnswerQuestion.delete()
    StudentFinishedTheme.delete()
    Provider.delete()
    Specialization.delete()
    Schedule.delete()
    CertificateCourse.delete()
    CertificateSpec.delete()


clean_tables()
print("Tables cleaned")

