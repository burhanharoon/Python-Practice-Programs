numbers = [int(x) for x in input("Enter the list items seperated by a space: ").split()]
counters = {
    "evenCounter": 0,
    "oddCounter": 0
}
for x in numbers:
    if x % 2:
        counters["oddCounter"]+=1 
    else:
        counters["evenCounter"]+=1
        
print("""
      The total even nunmbers are: {} \n
      The total odd nunmbers are: {}
      """.format(counters["evenCounter"],counters["oddCounter"]))
