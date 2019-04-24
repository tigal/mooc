# -*- coding: utf-8 -*-

def get_models():
    from models.student import Student
    from models.student_answers import StudentAnswerQuestion, StudentFinishedTheme, StudentFinishedCourse, \
        StudentFinishedTest, StudentAnswerTestQuestion
    from models.user_defined import UserDefinedCourse, UserDefinedTheme
    from models.provider import Provider
    from models.specialization import Specialization
    from models.schedule import Schedule
    from models.course import Course, CourseTheme, Question, CertificateCourse, CertificateSpec
    from models.quick_tests import Test, TestQuestion
    from models.subscription import Subscription

    return [CertificateCourse, StudentAnswerQuestion, StudentFinishedTheme, StudentFinishedCourse,
          StudentFinishedTest, StudentAnswerTestQuestion, Subscription, Question, Course, CourseTheme, Test,
          TestQuestion,
          UserDefinedCourse, UserDefinedTheme, Schedule, Provider,
          CertificateSpec, Specialization, Student]
