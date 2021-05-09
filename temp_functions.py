def fahr_to_celsius(temp_fahrenheit):
  """
Function for converting temperature in Kelvins to Celsius
Paramaters
---------
fahr_to_celsius:<numerical>
converted temperature in celsius

Returns
---------
<numerical>
classified numbers
 """
  converted_temp=(temp_fahrenheit-32)/1.8;
  return converted_temp
def temp_classifier(temp_celsius):
  """
Function for classifinig Temperature.
Paramaters
---------
temp_celsius:<numerical>
temperature in celsius

Returns
---------
<numerical>
classified numbers
 """
  if (temp_celsius<-2):
   return 0
  elif (-2<=temp_celsius<2):
   return 1
  elif (2<=temp_celsius<15):
   return 2
  elif (temp_celsius>=15):
   return 3  
"""
This scrip is combined file into fahr_to_celsius and temp_classifier functions

"""
