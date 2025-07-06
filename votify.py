import csv
import os
import pickle
#RECORD OF CLASS12 BOYS                
def displayB():
        f1=open('BOYS.csv','r')
        r=csv.reader(f1)
        for rec in r:
            print(rec)
        f1.close()
#RECORD OF CLASS12 GIRLS        
def displayG():
        f1=open('GIRLS.csv','r')
        r=csv.reader(f1)
        for rec in r:
            print(rec)
        f1.close()
#ASSIGNING INTERVIEW-MARKS TO CLASS12 BOYS        
def enmarksB():
    f1=open('BOYS.csv','r')
    f=open('newboys.csv','w+')
    r=csv.reader(f1)
    for rec in r:
            try:
                    print("For this row:",rec[0],rec[1])
                    im=input('enter interview marks:')
                    rec.pop()
                    rec.append(im)
                    w=csv.writer(f)
                    w.writerow(rec)
            except IndexError :
                    print('DONE')
    f.close()
    f1.close()
    os.remove('BOYS.csv')
    os.rename('newboys.csv','BOYS.csv')
#ASSISNGIN INTERVIEW-MARKS TO CLASS12 GIRLS    
def enmarksG():
    f1=open('GIRLS.csv','r')
    f=open('newgirls.csv','w+')
    r=csv.reader(f1)
    for rec in r:
            try:
                    print("For this row:",rec[0],rec[1])
                    im=input('enter interview marks:')
                    rec.pop()
                    rec.append(im)
                    w=csv.writer(f)
                    w.writerow(rec)
            except IndexError :
                    print('DONE')
    f.close()
    f1.close()
    os.remove('GIRLS.csv')
    os.rename('newgirls.csv','GIRLS.csv')

#SELECTION OF 5 BOYS FOR HEADBOY ON THE BASIS OF THEIR INTERVIEW MARKS   
def nomBOYS():
        fo=open('BOYS.csv','r')
        n=csv.reader(fo)
        a=[]
        for rec in n:
                try:
                        a.append(int(rec[2])+int(rec[3]))
                except IndexError:
                        pass
        a.sort(reverse=True)
        print(a)
        fo.close()
    
        fo=open('BOYS.csv','r')
        fc=open('boys_nom.csv','w+')
        n=csv.reader(fo)
        for rec in n:
                try:
                        if (int(rec[2])+int(rec[3])) in a[0:5]:
                                w1=csv.writer(fc)
                                w1.writerow(rec)
                except IndexError:
                        pass
        fo.close()
        fc.close()

#SELECTION OF 5 GIRLS FOR HEADGIRL ON THE BASIS OF THEIR INTERVIEW MARKS           
def nomGIRLS():
        fc=open('girls_nom.csv','w+')
        fo=open('GIRLS.csv','r')
        n=csv.reader(fo)
        a=[]
        for rec in n:
                try:
                        a.append(int(rec[2])+int(rec[3]))
                except IndexError:
                        pass
        a.sort(reverse=True)
        print(a)
        b=[]
        for i in a[0:5]:
                b.append(int(i))
                print(b)
                fo.close()
    
        fo=open('GIRLS.csv','r')
        fc=open('girls_nom.csv','w+')
        n=csv.reader(fo)
        for rec in n:
                try:
                        if int(rec[2])+int(rec[3]) in b:
                                w1=csv.writer(fc)
                                w1.writerow(rec)
                except IndexError:
                        pass
        fo.close()
        fc.close()
#SHOWING 5 SELECTED BOYS WITH THEIR DETAILS        
def show_nomBOYS():
        f1=open('boys_nom.csv','r')
        r=csv.reader(f1)
        for rec in r:
            print(rec)
        f1.close()
#SHOWING 5 SELECTED GIRLS WITH THEIR DETAILS        
def show_nomGIRLS():
        f1=open('girls_nom.csv','r')
        r=csv.reader(f1)
        for rec in r:
            print(rec)
        f1.close()
#SHOWS LIVE RESULT FOR HEADBOY        
def resultBOYS():
    f=open('resB.csv','r+')
    lc=[]
    r=csv.reader(f)
    try:
        for rec in r:
            lc.append(int(rec[1]))
            ma=max(lc)
    except IndexError:
        pass
    f.close()
    f=open('resB.csv','r+')
    r=csv.reader(f)
    try:
        for rec in r:
            if int(rec[1])==ma:
                print(rec[0])
    except IndexError:
        pass
    f.close()
        
#SHOWS LIVE RESULT FOR HEADGIRL
def resultGIRLS():
        f=open('resG.csv','r+')
        lc=[]
        r=csv.reader(f)
        try:
                for rec in r:
                        lc.append(int(rec[1]))
                        ma=max(lc)
        except IndexError:
                pass
        f.close()
        f=open('resG.csv','r+')
        r=csv.reader(f)
        try:
                for rec in r:
                        if int(rec[1])==ma:
                                print(rec[0])
        except IndexError:
                pass
        f.close()
#TAKING VOTES FOR HEADBOY
def vote_to_boys():
    f=open('resB.csv','w+')
    fo=open('boys_nom.csv','r')
    fc=open('temp.csv','w+')
    bo=csv.reader(fo)
    for rec in bo:
        try:
            print(rec[1])
            r=csv.writer(fc)
            r.writerow([rec[1],0])
        except IndexError:
            pass
    fo.close()
    f.close()
    Hgirl=input("Enter the HG name")
    f=open('resB.csv','r+')
    b=csv.reader(f)
    for rec in b:
        try:
            if Hgirl==rec[0]:
                r=csv.writer(fc)
                r.writerow([rec[0],int(rec[1])+1])
            else:
                r=csv.writer(fc)
                r.writerow([rec[0],rec[1]])
        except IndexError:
            pass
    f.close()
    fc.close()
    os.remove('resB.csv')
    os.rename('temp.csv','resB.csv')
    print('SUCCESSFULLY!!!voted for headgirl')
     
       
        
       
                        
#TAKING VOTES FOR HEADGIRL                       
def vote_to_girls():
     
        
        f=open('resG.csv','w+')
        fo=open('girls_nom.csv','r')
        fc=open('temp.csv','w+')
        bo=csv.reader(fo)
        for rec in bo:
            try:
                print(rec[1])
                r=csv.writer(fc)
                r.writerow([rec[1],0])
            except IndexError:
                pass
        fo.close()
        f.close()
        Hgirl=input("Enter the HG name")
        f=open('resG.csv','r+')
        b=csv.reader(f)
        for rec in b:
                try:
                    if Hgirl==rec[0]:
                        r=csv.writer(fc)
                        r.writerow([rec[0],int(rec[1])+1])
                    else:
                        r=csv.writer(fc)
                        r.writerow([rec[0],rec[1]])
                except IndexError:
                        pass
        f.close()
        fc.close()
        os.remove('resG.csv')
        os.rename('temp.csv','resG.csv')
        print('SUCCESSFULLY!!!voted for headgirl')
     
       
        
#HOMEPAGE FOR STUDENTS TO GIVE VOTES       
def student():
        while True:
                print('press 1 to vote for headboy')
                print('press 2 to vote for headgirl')
                print('press 3 to see result of headboy')
                print('press 4 to see result of headgirl')
                print('press 5 to exit')
                ch2=int(input('enter your choice'))
                if ch2==1:
                        vote_to_boys()
                        
                        #print('SUCCESSFULLY!!!voted for headboy')
                        continue
                if ch2==2:
                        vote_to_girls()
                        continue
                if ch2==3:
                        resultBOYS()
                        continue
                if ch2==4:
                        resultGIRLS()
                        continue
                if ch2==5:
                        print('THANKS!!for voting')
                        break
                else:
                        print('OOPS!!!something went wrong')
                        print('please try again')
                        continue
#HOMEPAGE FOR TEACHERS TO ORGANISE THE VOTING SYSTEM                       
def teacher():
    while True:
        print('press 1 to display (boys)')
        print('press 2 to display (girls)')
        print('press 3 to enter marks (boys) ')
        print('press 4 to enter marks (girls)')
        print('press 5 to see nominated candidates(boys)')
        print('press 6 to see nominated candidates(girls)')
        print('press 7 to go home page')
        c1=int(input('enter your choice'))
        if c1==1:
                displayB()
                continue
        if c1==2:
                displayG()
                continue
        if c1==3:
                enmarksB()
                continue
        if c1==4:
                enmarksG()
                continue 
        if c1==5:
                show_nomBOYS()
                continue
        if c1==6:
                show_nomGIRLS()
                continue
        if c1==7:
                break
        else:
                print("enter a valid choice")
                continue
# MAIN HOMEPAGE        
while True:
    print("press 1 if you are teacher")
    print("press 2 if you are student")
    print("press 3 to exit")
    choice=int(input('tell your profession (teacher/student):'))
    if choice==1:
        teacher()
        continue
    elif choice==2:
        student()
        continue
    elif choice==3:
        print('thanks for participating!!!')
        break
    else:
        print('Enter a valid choice')
        continue
