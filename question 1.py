# question 1
marks={'Joanna':77,'Mahalia':70,'Gerald':66,'Maria':80}
name='Maria'
def function(name):
    try:
        print( marks[name])
    except:
        print(name+'not found')
function(name) 

# question 1 part 2
marks={'Joanna':77,'Mahalia':70,'Gerald':66,'Maria':80}
def average ():
    average_value=sum(marks.values())/len(marks)
    print (average_value)
average()