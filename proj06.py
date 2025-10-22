""" Source header """

import sys


# def input( prompt=None ):
#     """
#         DO NOT MODIFY: Uncomment this function when submitting to Codio
#         or when using the run_file.py to test your code.
#         This function is needed for testing in Codio to echo the input to the output
#         Function to get user input from the standard input (stdin) with an optional prompt.
#         Args:
#             prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
#         Returns:
#             str: The user input received from stdin.
#     """
#
#     if prompt:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str


choices = '''
  Menu : 
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together 
       Enter any other key(s) to exit

  '''

"Input a choice ~:"

"Error. File does not exist"
"\nEnter a names file ~:"
"\nEnter the X id file ~:"
"\nEnter the facebook id file ~:"

"The Max number intersection of friends between X and Facebook is: {}"
"{}% of people have no friends in common on X and Facebook"

"Enter a person's name ~:"
print("-"*14+"\nFriends in X\n"+"*"*14)
print("-"*20+"\nFriends in Facebook\n"+"*"*20)
"Invalid name or does not exist"

"{}% of people have more friends in X compared to Facebook"

"The number of triangle friendships in X is: {}"
"The number of triangle friendships in Facebook is: {}"
"The number of triangle friendships in X merged with Facebook is:  {}"
"Thank you"


##def open_file():
    #if(
    #pass

    
def readdict():
    namedict={}
    while(True):
        file1=input("\nEnter a names file ~:")
        try:
            name_file = open(file1,'r', encoding="utf-8")
            break
        except:
            print("Error. File does not exist")
            continue
    name_data=name_file.read()
    name_data_list=name_data.split("\n")
    namedata=name_data_list
    while(True):
        file2=input("\nEnter the twitter id file ~:")
        try:
            X_file=open(file2,'r')
            break
        except:
            print("Error. File does not exist")
            continue
    X_data=X_file.read()
    X_data_list=X_data.split("\n")
    for i in range(0,len(X_data_list)):
        X_data_list[i]=list(X_data_list[i].split(","))
        X_data_list[i].pop()
        for j in range(0,len(X_data_list[i])):
            X_data_list[i][j]=name_data_list[int(X_data_list[i][j])]
    while(True):
        file3=input("\nEnter the facebook id file ~:")
        try:
            facebook_file=open(file3,'r')
            break
        except:
            print("Error. File does not exist")
            continue
    facebook_data=facebook_file.read()
    facebook_data_list=facebook_data.split("\n")
    for i in range(0,len(facebook_data_list)):
        facebook_data_list[i]=list(facebook_data_list[i].split(","))
        facebook_data_list[i].pop()

    for i in range(0,len(name_data_list)):
        name=str(name_data_list[i])
        namedata[i]={
                        "Name":name,
                        "X_friends":X_data_list[i],
                        "Facebook_friends":facebook_data_list[i]
                     }
        namedict[name]=namedata[i]
    return namedict
    
##F1    
def f1(dictionary):
    namedict=dictionary
    intersection_max=0
    xfrnd={}
    for i in namedict:
        a=0
        frnd=namedict[i]
        c=0
        for j in frnd['X_friends']:
            xstring=(frnd['X_friends'])[c]
            c+=1
            d=0
            for h in frnd["Facebook_friends"]:
                fstring=frnd["Facebook_friends"][d]
                d+=1
                if(xstring==fstring):
                    a+=1
        if(a>intersection_max):
            intersection_max=a
    print("The Max number intersection of friends between X and Facebook is: ",intersection_max)
##F1

##F2
def f2(dictionary):
    namedict=dictionary
    x=len(dictionary) 
    xfrnd={}
    for i in namedict:
        a=0
        frnd=namedict[i]
        c=0
        for j in frnd['X_friends']:
            xstring=(frnd['X_friends'])[c]
            c+=1
            d=0
            for h in frnd["Facebook_friends"]:
                fstring=frnd["Facebook_friends"][d]
                d+=1
                if(xstring==fstring):
                    a+=1
        if(a>0):
            x-=1
            
    percentage=x*100
    r=round(percentage/len(namedict))
    print(f"{r}% of people have no friends in common on X and Facebook")
##F2

##F3
def f3(dictionary):
    name=input("Enter a person name:")
    namedict=dictionary
    c=0
    while (c!=1):
        for i in namedict:
            if(i==name):
                c=1
                break
        if(c!=1):
            print("Invalid name or does not exist")
            name=input("Enter the name:")
        
    frnd=namedict[name]
    ascendingorder(name,'X_friends',dictionary)
    print("-"*14+"\nFriends in X\n"+"*"*14)
    d=0
    for g in frnd['X_friends']:
        printable=(frnd['X_friends'])[d]
        print(str(printable))
        d+=1
    ascendingorder(name,'Facebook_friends',dictionary)
    print("-"*20+"\nFriends in Facebook\n"+"*"*20)
    e=0
    for l in frnd['Facebook_friends']:
        printable=(frnd['Facebook_friends'])[e]
        print(str(printable))
        e+=1
    
def ascendingorder(name,string,dictionary):
    namedict=dictionary
    frnd=namedict[name]
    c=0
    for j in frnd[string]:
        xxstring=(frnd[string])[c]
        for k in range(c+1,len(frnd[string])):
            temp=""
            tempr=""
            xystring=(frnd[string])[k]
            if(xystring<xxstring):
                temp=xystring
                tempr=(frnd[string])[c]
                xystring=xxstring
                (frnd[string])[c]=(frnd[string])[k]
                xxstring=temp
                (frnd[string])[k]=tempr
            k+=1      
        c+=1
    return frnd[string]
##F3

##F4
def f4(dictionary):
    namedict=dictionary
    morexcount=0
    for i in namedict:
        frnd=namedict[i]
        xfriend=0
        for j in frnd['X_friends']:
            xfriend+=1
        fbfriend=0
        for h in frnd["Facebook_friends"]:
            fbfriend+=1
        if(xfriend>fbfriend):
            morexcount+=1
    percentage=morexcount*100
    r=round(percentage/len(namedict))
    print(f"{r}% of people have more friends in X compared to Facebook")
##F4

##F5
def f5(dictionary):
    namedict=dictionary
    triangle_Friend=[]
    for na1, k in namedict.items():
        for na2 in k['X_friends']:
            for na3 in k['X_friends']:
                if(na3 not in namedict[na2]['X_friends']):
                    continue
                if({na1,na2,na3} in triangle_Friend):
                    continue
                triangle_Friend.append({na1,na2,na3})
    print(len(triangle_Friend))
 

def f6(dictionary):
    namedict=dictionary
    triangle_Friend=[]
    for na1, k in namedict.items():
        for na2 in k["Facebook_friends"]:
            for na3 in k["Facebook_friends"]:
                if(na3 not in namedict[na2]["Facebook_friends"]):
                    continue
                if({na1,na2,na3} in triangle_Friend):
                    continue
                triangle_Friend.append({na1,na2,na3})
    print(len(triangle_Friend))



   
def f7(dictionary):
    namedict=dictionary
    thisdict={}
    fbxmerge=[]
    data=[]
    x=1
    for na1, k in namedict.items():
        fbxmerge=[]
        name=namedict[na1]
        for h in k['X_friends']:
            fbxmerge.append(h) 
        for j in k["Facebook_friends"]:
            if(j not in fbxmerge):
                fbxmerge.append(j)
        thisdict[name["Name"]] = fbxmerge
        x+=1 
    triangle_Friend=[]
    for na1, k in thisdict.items():
        for na2 in k:
            for na3 in k:
                if(na3 not in thisdict[na2]):
                    continue
                if({na1,na2,na3} in triangle_Friend):
                    continue
                triangle_Friend.append({na1,na2,na3})
    print(len(triangle_Friend))



    

def main():
    namedict=readdict()
    while(True):
        print(choices)
        n=input("Input a choice ~:")
        if(n=="1"):
            f1(namedict)
        elif(n=="2"):
            f2(namedict)
        elif(n=="3"):
            f3(namedict)
        elif(n=="4"):
            f4(namedict)
        elif(n=="5"):
            f5(namedict)
        elif(n=="6"):
            f6(namedict)
        elif(n=="7"):
            f7(namedict)
        else:
            print("Thank you")
            break
    
            
    
    pass


if __name__ == '__main__':
    main()
