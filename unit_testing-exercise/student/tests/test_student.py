from unittest import TestCase, main
from project.student import Student

class TestStudent(TestCase):


    def setUp(self) -> None:
        self.student = Student("OOP", {})
        self.student_whit_courses = Student("QA", {'unittest': ["unit1"]})

    def test_initialization(self):
        self.assertEqual(self.student.name, "OOP")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student_whit_courses.courses,{'unittest': ["unit1"]})

    def test_enroll_add_notes_student_whit_courses(self):
        result = self.student_whit_courses.enroll('unittest', ["unit2"])
        self.assertEqual("unit2", self.student_whit_courses.courses['unittest'][1])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_notes_name_Y_student_not_courses(self):
        result = self.student.enroll("unittest", ["unit3"])
        self.assertEqual("unit3", self.student.courses['unittest'][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_notes_name_none_student_not_courses(self):
        result = self.student.enroll("unittest", ["Y"], "Y")
        self.assertEqual("Y", self.student.courses['unittest'][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_course_name(self):
        result = self.student.enroll("unittest", ["unit3"], "N")
        self.assertEqual(0, len(self.student.courses["unittest"]))
        self.assertEqual("Course has been added.", result)

    def test_add_notes(self):
        result = self.student_whit_courses.add_notes("unittest", "unit4")
        self.assertEqual("unit4", self.student_whit_courses.courses["unittest"][-1])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_name_not_in_dict_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("unittest", "unit5")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student_whit_courses.leave_course("unittest")
        self.assertEqual({}, self.student_whit_courses.courses)
        self.assertEqual(result, "Course has been removed")

    def test_leave_course_not_course_in_dict(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("unittest")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
