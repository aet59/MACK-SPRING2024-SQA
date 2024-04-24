

from mining import *


def fuzzDays_between():
   try:
    #result is negative days
    res = days_between(0, 25)
    return res
   except Exception as e:
        print ("Cannot have negative days", e)
   

def fuzz_getDevEmailForCommit():
    try:
    #result is negative days
        res = getDevEmailForCommit('this_path_is_invalid', "this_has_is_too")
        return res
    except Exception as e:
        print ("Path is invalid", e)
    

def fuzz_makeChunks():
    try:
    #invalid list size
        res = makeChunks("list_name", 'chunksize')
        return res
    except Exception as e:  
        print ("Invalid list size", e)
    

def fuzz_getPythonFileCount():
   try:
    #invalid path
    res = getPythonFileCount(1)
    return res
   except Exception as e:
     print ("Invalid path", e)
   

def fuzz_dumpContentIntoFile():
   try:
   #invalid path 
    res = dumpContentIntoFile("something", )
    return res
   except Exception as e:
    print ("invalid path", e)
   

if __name__=='__main__':
    fuzz_makeChunks()
    fuzz_dumpContentIntoFile()
    fuzz_getDevEmailForCommit()
    fuzz_getPythonFileCount()
    fuzzDays_between()

