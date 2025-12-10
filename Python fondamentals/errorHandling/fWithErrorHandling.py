def divistion():
    try:
        a = float(input("Enter the valu of a : "))
        b = float(input("Enter the valu of b : "))
        c = a/b
        print(c)

    except:
        print(" the entered value is invalid :")


divistion()
""" if you enter anything that is not number(e.g: s or other letter) the our 
code does'nt get crushed so a used try
 except statement as errorhandling for prevent that and recoginizing what is happening  """
