def nameValidator(name):
  if name.count(" ") != 1:
    return "Validation Failed: Please check that the names are not more than or less than 2, or more than one space."
  
  if name.replace(" ", "").isalpha() != True:
    return "Validation Failed: Please check that your name does not contain special characters or numbers"
  nameList = name.split(" ")
  if 4 < len(nameList[0]) < 21 and 4 < len(nameList[1]) < 21:
    return "Validation Successful"
  return "Validation Failed: Please check that the names are up to 5 characters each."
        
print(nameValidator("Johnny Fooly "))