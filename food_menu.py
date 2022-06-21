print("WELCOME to the home_feel ")
while True:
    print("""please selet one 
    1 for sunday 
    2 for mon day
    3 for tuesday 
    4 for wednesday 
    5 for thursday
    6 for frieday 
    7 for sunday 
    press anythings for exist  """)
    day=int(input(">>>>>>>"))
    if day==1:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==3:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL ROTI 
            PRESS 2 FOR MATON ROTI  
            PRESS 3 FOR VEG ROTI
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL ROTI  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL ROTI   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON ROTI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON ROTI   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG ROTI  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG ROTI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==0:
                break
            else :
                print("you enter something wrong!!!!")
        
    elif day==2:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==3:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL ROTI 
            PRESS 2 FOR MATON ROTI  
            PRESS 3 FOR VEG ROTI
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL ROTI  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL ROTI   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON ROTI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON ROTI   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG ROTI  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG ROTI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==0:
                break
            else :
                print("you enter something wrong!!!!") 
    elif day==3:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==3:
               while True :
                print("""1 for breakfast
    2 for lunch 
    3 for dinner""")
                meal=int(input(">>>>>"))
                if meal==1:
                    while True:
                        print("""AVAILAIBLE FOOD FOR BREKFAST :-
                PRESS 1 FOR POHA
                PRESS 2 FOR  MEGGI
                PRESS 3 FOR MILK PRODUCT
                press 0 for exist """)
                        s=int(input(">>>>>>>>"))
                        if s==1:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected poha and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected poha  and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==2:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected MEGGI and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected MEGGI  and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==3:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected MILK PRODUT  and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected MILK PRODUCT   and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==0:
                            print("okkkk !!!")
                            break
                        else:
                            print("you enter something wrong!!! ")
                elif meal==2:
                    while True:
                        print("""AVAILAIBLE FOOD FOR BREKFAST :-
                PRESS 1 FOR DALL CHAVAL 
                PRESS 2 FOR MATON CHAVAL 
                PRESS 3 FOR VEG CHAVAL 
                press 0 for exist """)
                        s=int(input(">>>>>>>>"))
                        if s==1:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected DALL CHAVAL  and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected DALL CHAVAL   and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==2:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected MATON CHAVAL and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected MATON CHAVAL   and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==3:
                            print("""
                            press 1 for half plate 30 $$
                            press 2 for full plate 60 $$""")
                            s1=int(input(">>>>>"))
                            if s1==1:
                                print("you slected VEG CHAVAL  and half plate 30 $$ ")
                            elif s1==2:
                                print("you slected VEG CHAVAL  and half plate 60 $$ ")
                            elif s1==0:
                                break
                            else:
                                print("you enterted smethings wrong !!")
                        elif s==0:
                            print("okkkk !!!")
                            break
                        else:
                            print("you enter something wrong!!! ")
    elif day==4:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
    elif day==5:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
    elif day==6:
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
    elif day ==7 :
        while True :
            print("""1 for breakfast
2 for lunch 
3 for dinner""")
            meal=int(input(">>>>>"))
            if meal==1:
                while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR POHA
            PRESS 2 FOR  MEGGI
            PRESS 3 FOR MILK PRODUCT
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected poha and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected poha  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MEGGI and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MEGGI  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MILK PRODUT  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MILK PRODUCT   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
            elif meal==2:
                 while True:
                    print("""AVAILAIBLE FOOD FOR BREKFAST :-
            PRESS 1 FOR DALL CHAVAL 
            PRESS 2 FOR MATON CHAVAL 
            PRESS 3 FOR VEG CHAVAL 
            press 0 for exist """)
                    s=int(input(">>>>>>>>"))
                    if s==1:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected DALL CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected DALL CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==2:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected MATON CHAVAL and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected MATON CHAVAL   and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==3:
                        print("""
                        press 1 for half plate 30 $$
                        press 2 for full plate 60 $$""")
                        s1=int(input(">>>>>"))
                        if s1==1:
                            print("you slected VEG CHAVAL  and half plate 30 $$ ")
                        elif s1==2:
                            print("you slected VEG CHAVAL  and half plate 60 $$ ")
                        elif s1==0:
                            break
                        else:
                            print("you enterted smethings wrong !!")
                    elif s==0:
                        print("okkkk !!!")
                        break
                    else:
                        print("you enter something wrong!!! ")
    elif day==0:
        break
    else:
        print("you enter sommething wrong !!!!")