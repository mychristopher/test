#！/usr/bin/python
# -*- coding: utf-8 -*-
from Father import Father
from Mother import Mother

class Child(Father,Mother):
    def __init__(self,money,faceValue):
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)
        self.height = 178