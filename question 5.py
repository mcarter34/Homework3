#question 5
def function():
    x=list(range(1,100))
    print(sum(x))
    print(sum(x)/len(x))
    from statistics import stdev 
    print (stdev(x))
function()    