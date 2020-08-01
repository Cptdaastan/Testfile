#!/usr/bin/env python
# coding: utf-8

# # OOPS

# In[54]:


class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name  =name
        self.sub1 =sub1
        self.sub2 =sub2
        self.sub3 =sub3
    def putval1(self,val1):
        self.sub1 =val1
        print("The value of sub1 is changed now value is",self.sub1)
        
    def putval2(self,val2):
        self.sub2 =val2
        print("The value of sub1 is changed now value is",self.sub1)
        
        
    def putval3(self,val3):
        self.sub3 =val3
        print("The value of sub1 is changed now value is",self.sub1)
        
    def show_info(self):
        list1 =[self.sub1,self.sub2,self.sub3]
        st ="st marrey school delhi"
        print("\t",st.title())
        print("Class of student is :\t 6A",end ='\n')
        print("Annnual year of student of passing is 2020-2021")
        print("The name of Student:\t",self.name)
        print("there is the marksof sunject s",list1)
    def cal(self):
        list1 =[self.sub1,self.sub2,self.sub3]
        for i in list1:
            if i >=35:
                if i>=75:
                    print("Passed with good gread!!",i)
                    break
                else:
                    print(self.name,"passed in exam in sub:\t",i)
            else:
                print("Sorry! Failed in Exam in sub:\t",i)
    
    def getval1(self):
        print("This is the marks of sub1:\t",self.sub1)
    
    def getval2(self):
        print("This is the marks of sub1:\t",self.sub2)
    def getval3(self):
        print("This is the marks of sub1:\t",self.sub3)


# In[55]:


suresh =Student("Suresh",35,34,35)
ramesh =Student("Ramesh",78,98,78)


# In[56]:


suresh.show_info()
suresh.putval1(78)
suresh.putval2(88)
suresh.putval3(98)


# In[57]:


ramesh.show_info()
suresh.show_info()
suresh.getval1()
suresh.getval2()
suresh.getval3()


# In[38]:


ramesh.cal()


# In[39]:


suresh.cal()


# # inheritance

# In[71]:


class Animal:
    def __init__(self):
        print("Animal is in world ")
    def WhoI(self):
        print("I am Animal")
    def eat(self):
        print("I am Animal and I eat")
    def breathe(self):
        print("Yes! \t I am Animal And I breathe tooo!!")


# In[72]:


class Student(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name =name
        print(f"Yes I am {self.name} and I am a Student and Animal too")


# In[74]:


Rema =Student("Reema")
Rema.WhoI()
Rema.eat()
Rema.breathe()


# In[67]:


Rema.WhoI()


# In[68]:


Rema.eat()


# In[70]:


Rema.breathe()


# In[ ]:


class (A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
MRO 

