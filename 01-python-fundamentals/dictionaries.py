#x = [ [5,2,3], [10,8,9] ] 
#x[1][0]=15
#print(x)
#students = [
 #{'first_name':  'Michael', 'last_name' : 'Jordan'},
 #{'first_name' : 'John', 'last_name' : 'Rosales'}
#]
#students[0]['last_name'] ='Bryant'
#print(students)

#sports_directory = {
 #'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
 #'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
#sports_directory['soccer'][0]= 'Andres'
#print(sports_directory)
#z = [ {'x': 10, 'y': 20} ]
#z[0]['y']=30
#print(z)
students = [
 {'first_name':  'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#def iterateDictionary(list):
  # for i in range(len(list)):
       # print(list[i])
      
 
#iterateDictionary(students)
def iterateDictionary(students):
   for i in students:
    for key,value in i.items():
      
      print{f"{key}-{value}"}


      iterateDictionary(students)

 