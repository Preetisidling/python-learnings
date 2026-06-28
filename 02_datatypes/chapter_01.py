# mutable - that can change
# immutable - that can NOT change
# mutablity is always associated with object identity not value 
# below ex - numbes(2,12) is immutable & set it mutable

sugar_amount = 2
print (f"initial sugar_amount: {sugar_amount}")
sugar_amount = 12
print (f"second sugar_amount: {sugar_amount}")
print (f"id of sugar_amount {id(2)}")
print (f"id of sugar_amount {id(12)}")
spice_mix = set()
print (f"id of initial spice mix: {id(set)}")
spice_mix.add("ginger")
spice_mix.add("cardamom")
print (f"id of after spice mix: {id(set)}")
print(f"spice mix values: {spice_mix}")