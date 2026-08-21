# brand generator
import random
# prefix
quantity=(int(input("\n How many brands names you required?..")))
generated_name=set()
for i in range(quantity):
   collection_1=["cloud","data","vision","spark","nova","pixel","quantum"]
# suffix
   collection_2=["labs","ai","tech","io","ly","hub"]
   choose1=random.choice(collection_1)
   choose2=random.choice(collection_2)
   brand_name=choose1+choose2
#    duplicate avoid
   if brand_name not in generated_name:
    #  You can't use += with a dictionary or set like that.
     generated_name.add(brand_name)
     print(brand_name)