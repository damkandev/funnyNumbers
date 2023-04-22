def fn(number, message):
    fn_converted = ""
    if(number == 1):
        fn_converted = str(number+2) + "-" + str(number+1)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 4):
        fn_converted = str(number-2) + "+" + str(number-2)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 5):
        fn_converted = str(number-2) + "+" + str(number-3)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 7):
        fn_converted = str(number-5) + "+" + str(number-4) + "+" + str(number-5)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 8):
        fn_converted = str(number-5) + "+" + str(number-5) + "+" + str(number-6)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 9):
        fn_converted = str(number-5) + "+" + str(number-5) + "+" + str(number-8)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"  
    elif(number == 11):
        fn_converted = str(number-1) + "+" + str(number-10)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 13):
        fn_converted = str(number-1) + "+" + str(number-12)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 17):
        fn_converted = str(number-1) + "+" + str(number-16)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 18):
        fn_converted = str(number-2) + "+" + str(number-16)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    elif(number == 19):
        fn_converted = str(number-3) + "+" + str(number-16)
        if(message == True):
          fn_converted = fn_converted + " Cuidado con el FunnyNumber"
    else:
        fn_converted = number
    return fn_converted