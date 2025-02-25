import re

class Valid:
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def zip(input):
    try:
      int(input)
      if re.match(r"^\d{5}$", input):
        return True
    except ValueError as e:
      print("not a valid zip. enter 5 digits e.g.'12345'")
    #length?

    #digits?

    #real ZIP?
    
    return False
  
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def phone(input):
    try:
      if re.match(r"^\+?\d{1,3} \(\d{3}\) \d{3}-\d{4}$", input):
        return True
    except ValueError:
      print(
        "Not a valid phone number. Enter in the format '(656) 777-7777' or with a country code like '+1 (656) 777-7777'.")
      return False

    #length?

    #digits?

    #format?

    #real number?
    
    return False