#！/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):

        if self.score>100 or self.score<0:
            raise ValueError("the score is wrong!")

        if self.score < 60:
            return 'C'

        if self.score < 80:
            return 'B'
        return 'A'

