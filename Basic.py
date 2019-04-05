from tkinter import *
import math

class calculator:
    
    def __init__(self, application):
        application.title("Basic Calculator")
        application.geometry("330x256")
        self.exp = Entry(application)
        self.exp.grid(row=0,column=0,columnspan=6,pady=3) 
        self.exp.focus_set() #Sets focus on the input text area 
        
        equalsButton = Button(application,text="=", anchor = "center", width=23,height=3,fg="white", bg="blue",command=lambda:self.equals())
        equalsButton.grid(row=4, column=1, columnspan = 3)
        
        acButton = Button(application,text='AC',width=5,height=3,fg="white", bg="blue",command=lambda:self.clearall())
        acButton.grid(row=1, column=4)
        
        cButton = Button(application,text='C',width=5,height=3, fg="white", bg="blue", command=lambda:self.clear1())
        cButton.grid(row=2, column=4) 

        ################# Numbers ####################
        sevenButton = Button(application,text="7",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(7)).grid(row=1, column=0) 
        
        eightButton = Button(application,text="8",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(8)).grid(row=1, column=1) 
  
        nineButton = Button(application,text="9",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(9)).grid(row=1, column=2) 

        fourButton = Button(application,text="4",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(4)).grid(row=2, column=0) 

        fiveButton = Button(application,text="5",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(5)).grid(row=2, column=1) 

        sixButton = Button(application,text="6",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(6)).grid(row=2, column=2) 

        oneButton = Button(application,text="1",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(1)).grid(row=3, column=0) 

        twoButton = Button(application,text="2",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(2)).grid(row=3, column=1) 

        threeButton = Button(application,text="3",width=5,height=3,fg="red",bg="light green", command=lambda:self.action(3)).grid(row=3, column=2) 
        
        zeroButton = Button(application,text="0",width=5,height=3, fg="red",bg="light green", command=lambda:self.action(0)).grid(row=4, column=0) 


        ############### Mathematical Operations ################
        
        plusButton = Button(application,text="+",width=5,height=3, fg="blue",bg="orange",command=lambda:self.action('+')).grid(row=1, column=3) 
        multiplyButton = Button(application,text="x",width=5,height=3, fg="blue",bg="orange",command=lambda:self.action('x')).grid(row=2, column=3) 
        subtractButton = Button(application,text="-",width=5,height=3, fg="blue",bg="orange",command=lambda:self.action('-')).grid(row=3, column=3) 
        divideButton = Button(application,text="÷",width=5,height=3, fg="blue",bg="orange", command=lambda:self.action('/')).grid(row=4, column=3) 
    
    def evaluateExpression(self):
        self.expression = self.exp.get()
        self.expressionText = self.expression.replace("x", "*")
        self.expressionText = self.expression.replace("/", "/")
        
    def equals(self):
        self.evaluateExpression()
        try:
            self.answer = eval(self.expressionText)
        except SyntaxError or NameError or AttributeError:
            self.exp.delete(0, END)
            self.exp.insert(0, 'Enter Valid Input')
        else:
            self.exp.delete(0, END)
            self.exp.insert(0, self.answer)
            
    def clearall(self):
        self.exp.delete(0, END)
    
    def clear1(self):
        self.txt=self.exp.get()[:-1]
        self.exp.delete(0,END) 
        self.exp.insert(0,self.txt) 
    
    def action(self,argi): 
        """pressed button's value is inserted into the end of the text area"""
        self.exp.insert(END,argi)

application = Tk()
applicationInstance = calculator(application)
application.mainloop()
