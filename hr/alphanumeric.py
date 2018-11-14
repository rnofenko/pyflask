if __name__ == '__main__':
    s = "qA2"
    s = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

    anyAlphanumeric = False
    anyAlphabetical = False
    anyDigits = False
    anyLowercase = False
    anyUppercase = False
    for c in s:
      if c.isdigit():
        anyAlphanumeric = True
        anyDigits = True
      elif c.isalpha():
        anyAlphanumeric = True
        anyAlphabetical = True
        if c.islower():
          anyLowercase = True
        elif c.isupper():
          anyUppercase = True
    
    print(anyAlphanumeric)
    print(anyAlphabetical)
    print(anyDigits)
    print(anyLowercase)
    print(anyUppercase)
