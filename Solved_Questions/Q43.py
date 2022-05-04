"""Q13:Write a python program to Access the value of key ‘history’ from the following dictionarysampleDict
= {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}"""

dict_1 ={"class" : {"student" : {"name" : "Mike", "marks" : {"physics" : 70, "history" : 80}}}}
history_key = dict_1['class']['student']['marks']['history']
print("for 'history' key value is ", history_key)