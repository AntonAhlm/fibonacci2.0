a=0
tal1=1
tal2=0
space1=str("")
space2=str("")
while a<40: 
       a+=1
       if a<10:
           space1=str(" ")
       else:
           space1=str("")
       if a<18:
           space2=str("\t")
       else:
           space2=str("")
 

       if a % 2 == 0:
           if tal2>2 or tal1>2: 
               print("Tal",a,space1,":",tal1,space2, "\t\t Kvot:",tal1/tal2 )
               tal2+=tal1 
           else: 
               print("Tal",a,space1,":",tal1 )
               tal2+=tal1 

       else :
           if tal2>2 or tal1>2: 
               print("Tal",a,space1,":",tal2,space2, "\t\t Kvot:",tal2/tal1)  
               tal1+=tal2
           else:
               print("Tal",a,space1,":",tal2,) 
               tal1+=tal2
      
