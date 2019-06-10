import logging

logging.basicConfig(filename = 'test_student.log', level=logging.INFO, format = '%(asctime)s : %(created)f:%(levelname)s:%(message)s')

class Student:
    def __init__(self, firstname, lastname, num, dept, level, cgpa):
        self.firstname = firstname
        self.lastname = lastname
        self.num = num
        self.dept = dept
        self.level = level
        self.cgpa = cgpa
        logging.info('Student Profile: {} \n {} \n {} \n {} \n {}'.format (self.fullname, self.email_add, self.dept, self.level, self.cgpa))
        #logging.info('Student Profile: {}, {}, {}, {}, {}'.format (self.fullname, self.email_add, self.dept, self.level, self.cgpa))

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @property
    def email_add(self):
        return ('{}.{}@school.edu'.format(self.lastname, self.firstname))

student_1 = Student('Oghale', 'Ekaba', 'CSC/2007/055', 'Computer Science and Engineering', '500L', '2.6')
