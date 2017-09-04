'''
Created on 18 Aug 2017

@author: T
'''
class MockDBHelper:
    
    def connect(self, database="crimemap"):
        pass
    
    def get_all_inputs(self):
        pass
    
    def add_input(self, data):
        pass
    
    def clear_all(self):
        pass
    
    def add_crime(self, category, date, latitude, longitude, description):
        print("INSERT INTO crimes (category, date, latitude, longitude, description) VALUES (%s, %s, %s, %s, %s)" %
              (category, date, latitude, longitude, description))