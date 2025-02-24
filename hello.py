Commodity=[]
def add_commodity(commodity):
  Commodity.append(commodity)

def add():
  amal=input("if you want add a commodity write(add) or you want see commoditys write(see)")
  if amal=="add":
    name=input("Enter your commodity name:")
    add_commodity(name)
    print("Commodity added!")
    add()
  elif amal=="see":
    print(Commodity)
    add()
  else:
    print("Can't detect command please try again...")
    add()
add()
