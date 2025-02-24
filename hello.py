Commodity={}
def add_commodity(commodity,number):
  Commodity[commodity]=int(number)

def add():
  amal=input("if you want add a commodity write(add) or you want see commoditys write(see) if you want buy a commodity write commodity name's:")
  if amal=="add":
    name=input("Enter your commodity name:")
    number=input("Enter your number of commodity:")
    add_commodity(name,number)
    print("Commodity added!")
    add()
  
  else:
    if amal in Commodity:
      if Commodity[amal]>0:
        print("OK")
        Commodity[amal]-=1
      else:
        print("no OK!")
        
add()
