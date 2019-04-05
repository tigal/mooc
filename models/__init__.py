# -*- coding: utf-8 -*-


def init_models(db):

    from models.student import Student
    from models.certificate import CertificateCourse,CertificateSpec
    from models.user_defined import UserDefinedCourse,UserDefinedTheme
    from models.student_answers import StudentAnswerQuestion,StudentFinishedTheme,StudentFinishedCourse,StudentFinishedTest,StudentAnswerTestQuestion
    from models.provider import Provider
    from models.specialization import Specialization
    from models.schedule import Schedule
    from models.course import Course,CourseTheme,Question
    from models.quick_tests import Test,TestQuestion

    ms = [CertificateCourse, StudentAnswerQuestion, StudentFinishedTheme, StudentFinishedCourse,
          StudentFinishedTest,StudentAnswerTestQuestion, Question, Course, Test, TestQuestion,
          UserDefinedTheme, UserDefinedCourse, CourseTheme, Schedule, Provider,
          CertificateSpec, Specialization, Student]

    db.database.drop_tables(ms)
    db.database.create_tables(ms)