#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)   # call User's __init__
        self.knowledge = []   # <-- this is required
    
    def learn(self, string):
        self.knowledge.append(string)
