'''
Created on 5 Sep 2017

@author: T

Script to try different options, trips and tricks
'''
# import dateparser
import string
# 
# print(dateparser.parse("1-jan/15"))
# print(dateparser.parse("1 week and 3 days ago"))
# print(dateparser.parse("3/4/17"))

def sanitize_string(userinput):
    whitelist = string.ascii_letters + string.digits + "!?$.,:;-'()&"
    return filter(lambda x: x in whitelist, userinput)

print("".join(sanitize_string('absdc<')))

print('aaa', "".join('aaa'))