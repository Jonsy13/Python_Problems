while True:
    try:
        age = int(input("Enter Ur Age : "))
        10/age
        
    except ValueError:
        print("U motherFucker Enter the fucking Age")
    except ZeroDivisionError:
        print("So u r a chutiya")
    else:
        print("Thank You")
        break;
    finally:
        print('ok now im done')
    
    
# def sum(n1 , n2):
#     try:
#         return n1+n2
#     except TypeError as err:
#         print(f"Enter numbers please : error : {err}")

# print(sum('1',2))


