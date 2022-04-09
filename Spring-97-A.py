from time import time
import os
import binascii
import math
import os.path
#Author’s Jurijus Pacalovas
lenf=0
name=""
add_bits=""
Make_togher=""

memory = str(input("How many computer RAM memory do have e.g. 4294967296: "))
x = memory.isnumeric()
if x==False:    
        print("Sorry this not whole number")
        raise SystemExit
                        
if x==True:
        memory=int(memory)

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:

        def cryptograpy_compression4(self):

                def Forest_Extract(Number_Row2,Number_Row_Count):

                        Number_Row_Count1=int(Number_Row2)
                        
                        if Number_Row_Count1==10:
                                Number_Row_Count1=0
        
                        Number_Row_Count_str1=str(Number_Row_Count1)
                        if Number_Row_Count1>-1 and Number_Row_Count1<10:
                                Number_Row_Count_str1="0"+Number_Row_Count_str1     
                        Number_Row6=Number_Row_Count_str1
                        
                        return Number_Row6
                
                
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
                    
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""
                    Number_Row_Count=10

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""
                    #Number_Row14=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(name) as my_file:
                            my_file.seek(0, os.SEEK_END) # go to end of file
                            if my_file.tell(): # if current position is truish (i.e != 0)
                                    my_file.seek(0) # rewind the file for later use 
                            else:
                                    x2 = time()
                                    x3=x2-x
                                    xs=float(x3)
                                    return print(x3)
                            
                      

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        Deep3=8
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+Equal_info_between_of_the_cirlce_of_the_file_2

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                  

                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda
                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>(memory):
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)

                                    
                                        

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                 
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                  
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                   
                                    g=0

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)                      
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                
                                    add_bits=""

                                    Times_6=""

                                    #Compression

                                    sda10=""
                                    Translate_info_Decimal=""
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                   
                 
                                    

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    Equal_info_between_of_the_cirlce_of_the_file2=""

                                    if Circle_times2>=(2**48)-3:
                                            compress_or_not_compress=2
                                            
                                    Equal_info_between_of_the_cirlce_of_the_file2=Equal_info_between_of_the_cirlce_of_the_file
                                  
                                    
                                    
 
                
                                    
                                
                                    nameas=name+".bin"
                                    Equal_info_between_of_the_cirlce_of_the_file_11=""
 
                                    
                                    

                                    Spin=0

                                    ei=0

                                    while ei<=lenf6:
                                            number_predict=Equal_info_between_of_the_cirlce_of_the_file2[ei:ei+8]
                                            er=ei%8
                                            
                                            if er==0:
                                                Spin=0
                                            
                                            

                                            if number_predict[0:2]=="11" and Spin==0 or number_predict[0:2]=="01" and Spin==0 or number_predict[0:2]=="10" and Spin==0:
                                                    number_predict1="1"+number_predict[2:8]
                                                 
                                                 
                                                    
                                                    Equal_info_between_of_the_cirlce_of_the_file_11=Equal_info_between_of_the_cirlce_of_the_file_11+number_predict1
                                                    Spin=1


                                            else:
                                                    
   
                                                            
                                                                                                        
                                                            
                                                    if   Spin==1:
                                                        
                                                            Equal_info_between_of_the_cirlce_of_the_file_11=Equal_info_between_of_the_cirlce_of_the_file_11+number_predict
                                                        

  
                                                    else:
                                                            number_predict1="0"+number_predict[2:8]
                                                                    
                                                            Equal_info_between_of_the_cirlce_of_the_file_11=Equal_info_between_of_the_cirlce_of_the_file_11+number_predict1
                                                    
                                            ei=ei+8
                                            
                                    
                                    

                                    

                                    
                                    
                                            #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                              
                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_11
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_17
                                    
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)
                                    Circle_times2=Circle_times2+1
                                    if   Circle_times2==1:

                                                Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17

                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                if count_bits==8:
                                                	count_bits=0
                                                count_bits2=count_bits
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                                while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1

                                        

                                    #if   lenfS<=Deep3 or compress_or_not_compress==2:
                                    	   


                                        
                                            #lenf=len(Number_Row14)

                                           # add_bits10=""
                                            #count_bits=8-lenf%8
                                            #z=0
                                            #if count_bits!=0:
                                                #if count_bits!=8:
                                                        #while z<count_bits:
                                                         	#add_bits10="0"+add_bits10
                                                         	#z=z+1   
                                    if Circle_times2==1:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                    #if   lenfS<=Deep3 or compress_or_not_compress==2:
                                                
                                    		
                                    		#Number_Row14=add_bits10+Number_Row14
                                    		#L=len(Number_Row14)
                                    		#n = int(Number_Row14, 2)
                                    		#width_bits=len(Number_Row14)
                                    		#width_bits=(width_bits//8)*2
                                    		#width_bits=str(width_bits)
                                    		#width_bits="%0"+width_bits+"x"
                                    		#width_bits3=binascii.unhexlify(width_bits % n)
                                    		#width_bits2=len(width_bits3)
                                    		#add_bitszzza=""
                                    		#add_bitszs=""
                                    		#Equal_info_between_of_the_cirlce_of_the_file_2=Times_6

                                    		
                                    		
                                    		#with open("Extra.bin", "wb") as f2:
                                    			#f2.write(width_bits3)
                                    		
                                    	
                                    		

                                    if   Circle_times2==1:
                                                
                                    		L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                    		width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		width_bits=(width_bits//8)*2
                                    		width_bits=str(width_bits)
                                    		width_bits="%0"+width_bits+"x"
                                    		width_bits3=binascii.unhexlify(width_bits % n)
                                    		width_bits2=len(width_bits3)
                                    		add_bitszzza=""
                                    		add_bitszs=""
                                    		Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(width_bits3)
                                    		
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    Prime_Not=0
                                 
                                    if C==1:
                                        if   Circle_times2==0:

                                                Translate_info_Decimal=Equal_info_between_of_the_cirlce_of_the_file[0:8]
                                                Translate_info_Decimal_2 = int(Translate_info_Decimal, 2)
                                                if Translate_info_Decimal_2>7:
                                                        Corrupted=1
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                sda10=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                Deep5 = int(sda10, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                
                                                
                                                Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                T = int(Times_6, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                
                                                
                                   
                                        if   Circle_times2>0:
                                                        Translate_info_Decimal_2=0
                                                
                                                        
            
                                        if C==1 and T!=0:
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Translate_info_Decimal_2:]
                                                        #Extract ###################################################################################################################
                                                        Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)
                                                            
                                                        
                                                        
                                                            
                                                        Number_Row1=""
                                                        Number_Row6=""
                                                        Number_Row_Count=12
                                                        Number_Row_Count_str3=""
                                                        Number_Row=str(Number_of_the_file)
                                                        Number_Row_Count=Number_Row_Count+1
                                                        Number_Row_Count_str=str(Number_Row_Count)
                                                    
                                                            
                                                            
                                                        Row=len(Number_Row)
                                                        ei=0
                                                        Spin_bits=0
                                                        while ei<Row:
                                                                    
                                                                    Number_Row2=Number_Row[ei:ei+1]
                                                                    Number_Row4=Number_Row[ei:ei+2]
                                                                    Number_Row8=Number_Row2[ei+2:ei+3]
                                                                    Number_Row3=Number_Row2
                                                                    Number_Row_Count_str3=str(Number_Row_Count)
                                                                    Number_Row_Count_str=str(Number_Row_Count)
                                                                    Number_Row_Count_str2=Number_Row_Count_str[1:2]+Number_Row_Count_str[0:1]


                                                                    if ei==0:
                                                                            Number_Row6=Number_Row[ei:ei+2]
                                                                            Number_Row1=Number_Row1+Number_Row6
                                                                    
                                                                            pin_bits=0
                                                                            ei=ei+2
                                                                    
                                                                    
                                                                    
                                                            
                                                                    elif Number_Row2[0:1]!=Number_Row_Count_str[0:1]  and ei!=0:
                                                                
                                                                            Number_Row10=Number_Row[ei:ei+2]
                                                                            Spin_bits=1
                                                                            

                                                                   

                                                                    elif Number_Row2[0:1]==Number_Row_Count_str[0:1] and ei!=0:
                                                                
                                                                            Number_Row6=Number_Row_Count_str
                                                                            Number_Row1=Number_Row1+Number_Row6
                                                                            Spin_bits=0
                                                                            ei=ei+1

                                                                    
                                                                    if Spin_bits==1:
                                                                           
                                                                            Number_Row6=Forest_Extract(Number_Row10,Number_Row_Count)
                                                                            
                                                                            Number_Row1=Number_Row1+Number_Row6
                                                                            pin_bits=0
                                                                            ei=ei+2
                                                                    
                                                                            
                                                                    Number_Row_Count=Number_Row_Count+1
                                                                    if Number_Row_Count==88:
                                                                                    Number_Row_Count=12
                                                                    Number_Row_Count_str=str(Number_Row_Count)
                                                                        
                                                        Number_Row3=Number_Row1
                                                        #print(Number_Row3)
                                                        
                                                        Number_Row_int=int(Number_Row3)
                                                           
                                                     
                                                        Equal_info_between_of_the_cirlce_of_the_file_11=bin(Number_Row_int)[2:]

                                                        Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_11
                                                                        
                                               
                                                        Times_6=Number_add_plus_one
                                                        Number_add_plus_one=""
                                              
                                            #####################################################################################################################################################
                                           
                                                        Prime_Not=""
                                            
                                            

                                            #Extract
                                            
                                             
                                                        Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                           

                                        if i==2:
                                                Make_togher=""
                                                Make_togher=Times_6
                                                Number_add_plus_one=""
                                                add_bits=""
                                                if C==1 and T!=0:
                                                        Circle_times2=Circle_times2+1

                                                lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(Circle_times2)
                                                
                                                
                                                
                                                
                                                if  Circle_times2==T:
                                                           
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                   
                                                    
                                                
                                                    if C==1:

                                                        if T!=0:    
         
                                                                Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17[1:(Deep5*8)+1]
                                                        
                                                        lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        #print(lenf14)
                                                        lenf16=lenf14%8
                                                        
                                                        
                                                        lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        add_bits=""
                                                        count_bits=8-lenf%8
                                                        z=0
                                                        if count_bits!=0:
                                                                if count_bits!=8:
                                                                    while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                                    L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                 
                                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                    width_bits=(width_bits//8)*2
                                                    width_bits=str(width_bits)
                                                    width_bits="%0"+width_bits+"x"
                                                    width_bits3=binascii.unhexlify(width_bits % n)
                                                    width_bits2=len(width_bits3)

                                                    add_bitszzza=""
                                                    add_bitszs=""
                                                    Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                                     
                                                    with open(nameas, "wb") as f2:
                                                    
                                                      
                                                        f2.write(width_bits3)
                                                    x2 = time()
                                                    x3=x2-x
                                                    xs=float(x3)
                                                    return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
