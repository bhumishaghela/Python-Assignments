def getdata():
    import datetime
    return datetime.datetime.now()
def locktasksdone(client_name):
    if 'rohan' in client_name.lower():
        choice=int(raw_input("Press 1 for exercise or 2 for diet"))
        if choice==1:
            exercise=raw_input("What should I lock")
            fp=open("rohanExercise.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(exercise))
        elif choice==2:
            diet=raw_input("What should I lock")
            fp=open("rohanDiet.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(diet))
    elif 'hammad' in client_name.lower():
        choice=int(raw_input("Press 1 for exercise or 2 for diet"))
        if choice==1:
            exercise=raw_input("What should I lock")
            fp=open("HammadExercise.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(exercise))
        elif choice==2:
            diet=raw_input("What should I lock")
            fp=open("HammadDiet.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(diet))
    elif 'harry' in client_name.lower():
        choice=int(raw_input("Press 1 for exercise or 2 for diet"))
        if choice==1:
            exercise=raw_input("What should I lock")
            fp=open("HarryExercise.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(exercise))
        elif choice==2:
            diet=raw_input("What should I lock")
            fp=open("HarryDiet.txt","a")
            time=getdata()
            fp.write("["+str(time)+"] ")
            fp.write(str(diet))
    else:
        print("Try client name Rohan, Hammad or Harry")
        
def retrievetaskperformed(client_name):
    if 'rohan' in client_name:
        print("Rohan's Exercise Plan is:")
        fp=open("rohanExercise.txt","r")
        if line in fp:
            print(line)
        fp.close()
        print("Rohan's Diet Plan is:")
        f2=open("rohanDiet.txt","r")
        if line in f2:
            print(line)
        f2.close()
    
        
    elif 'hammad' in client_name:
        print("Hammad's Exercise Plan is:")
        fp=open("HammadExercise.txt","r")
        if line in fp:
            print(line)
        fp.close()
        print("Hammad's Diet Plan is:")
        f2=open("HammadDiet.txt","r")
        if line in f2:
            print(line)
        f2.close()
    elif 'harry' in client_name:
        print("Harry's Exercise Plan is:")
        fp=open("HarryExercise.txt","r")
        if line in fp:
            print(line)
        fp.close()
        print("Harry's Diet Plan is:")
        f2=open("HarryDiet.txt","r")
        if line in f2:
            print(line)
        f2.close()
while(1):
    choice=int(raw_input("Enter 1 to lock or 2 to retrieve task"))
    if choice==1:
        client_name=raw_input("Enter client name for which you want  to lock task")
        locktasksdone(client_name)
    elif choice==2:
        client_name=raw_input("Enter client name for which you want  to lock task")
        retrievetaskperformed(client_name)
        
        
        

            
            
        
    
    
