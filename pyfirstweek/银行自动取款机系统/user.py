#！/usr/bin/python
# -*- coding: utf-8 -*-
class User(object):
    def __init__(self,name,idCard,phone,card):
        self.name = name
        self.card = card
        self.idCard = idCard
        self.phone = phone