from decimal import *
 
val1 = Decimal('7.3')
val2 = Decimal('1.56231455')
 
result = val1
roundresult = result.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)
 
l = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
print(l)