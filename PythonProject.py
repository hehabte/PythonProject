#Declaring global variables
global testcount
global totalprice
global producePrice
testcount = 0
totalprice = 0
producePrice = 0

#We call these three methods (PriceFunction, ShippingFunction, TotalPriceFunction) up top
#because our main functions (ShowMenu & ProcessInput) will require them
##Method used to apply discount
def PriceFunction(producePrice):
    if producePrice > 100 :
        producePrice = prodicePrice - (producePrice * 0.05)
        return producePrice
    else :
        return producePrice
#END

##Method for finding shipping cost
def ShippingFunction(producePounds):
    if producePounds < 5 :
        shippingCost = 3.50
        return shippingCost
    elif producePounds < 20 :
        shippingCost = 10
        return shippingCost
    else :
        shippingCost = 9.5 + (0.10*producePounds)
        return shippingCost
#END

##Method used to determine total price 
def TotalPriceFunction(producePrice):
    global totalprice
    #totalprice = totalprice + producePrice
    return totalprice        
#END 

##Show menu##
def ShowMenu():
    global artichokes, carrots, beets, choice

    artichokes = input("Pounds of artichokes: ")
    carrots = input("Pounds of carrots: ")
    beets = input("Pounds of beets: ")
    print "Main Menu"
    print "Choose one of the following commands"
    print "1. Submit"
    print "2. Summary"
    print "3. Reset"
    print "4. Exit"    
    choice = input ("Enter your command [1-4]: ")
  
    ProcessInput()
    
#END

## Create a new class called InputProcessing. Within that class, create a global variable
## ProcessInput that will act as our ProcessInput function. Making it global first
## allows the function to be global as well. notice, they are the same name.
## With our global function created, we can call it from anywhere within the code
class InputProcessing:
  global ProcessInput
  #Method for executing the appropriate actions for the right commands
  def ProcessInput():
      global testcount, totalprice, producePrice
      #Output
      if choice == 1:    
          artPrice = artichokes * 2.67
          carPrice = carrots * 1.49
          beePrice = beets * 0.67
          producePounds = artichokes + carrots + beets
          producePrice = artPrice + carPrice + beePrice
          testcount += 1
          totalprice += producePrice
          print "Produce price: ", PriceFunction(producePrice)
          print "Shipping cost: ", ShippingFunction(producePounds)
          print "Total: " , PriceFunction(producePrice) + ShippingFunction(producePounds)
          ShowMenu()
      elif choice == 2:
          averageprice = TotalPriceFunction(producePrice)/testcount
          print "Total produce price: ", totalprice
          print "Count: ", testcount
          print "Average produce price: ", averageprice
          ShowMenu()
      elif choice == 3:
          ShowMenu()
      else:
          print "Command 4"
#END


##none of the above code runs as its all enclosed in functions and they never get called. 
##Lets actually run our ShowMenu Function.
ShowMenu()


    
