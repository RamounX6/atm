
import time
class operations:

        print("50")


        print("100")


        print("200")


        print("300")

        print("500")

        print("800")

        print("another option") ##leads to new window

        ##new window

        print("with draw") ##leads to new window


        print("depposite") ##leads to new window

        ##new window

        print("please enter your cash")

        g=int(input())  ##leads to new window
        l=list(str(g))

        ##new window

        if(len(l)<4):



            p =int(l[-1])
            if p in range(1,4) or p in range(6,9):

                l[-1]=0

                for x in l:
                    print(x,end="")
                print (" for your account")
                print(time.asctime())

            else:
                print(g,"for your account")
                print(time.asctime())


