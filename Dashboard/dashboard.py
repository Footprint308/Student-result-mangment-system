from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
# import pymysql
import sqlite3
from tkinter import messagebox,ttk

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Managment System")
        self.root.geometry("14000x750+0+0")
        self.root.config(bg = "white")
        # Define Icons
        self.logo_dash = ImageTk.PhotoImage(file = "images/logo_p.png")

        # Define Title 
        title = Label(self.root,text="Student Result Managment System",padx = 10, compound = LEFT, image = self.logo_dash, font=("goudy old style",20,"bold"), bg="#033054", fg="white").place(x=0,y=0,relwidth=1,height=50)
        # Define Menu 
        M_Frame = LabelFrame(self.root, text = "Menu", font = ("times new roman", 15), bg = "white")
        M_Frame.place(x=10, y=70, width=1510, height=80)

        btn_course = Button(M_Frame, text = "Course", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command = self.add_course).place(x=60,y=5,width=200,height=40)
        btn_student = Button(M_Frame, text = "Student", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command = self.add_student).place(x=320,y=5,width=200,height=40)
        btn_result = Button(M_Frame, text = "Result", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command= self.add_result).place(x=540,y=5,width=200,height=40)
        btn_view = Button(M_Frame, text = "View Student Results", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command=self.add_report).place(x=760,y=5,width=200,height=40)
        btn_logout = Button(M_Frame, text = "Logout", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command=self.logout).place(x=980,y=5,width=200,height=40)
        btn_exit = Button(M_Frame, text = "Exit", font=("goudy old style",15,"bold"),bg="#0b5377",fg = "white", cursor = "hand2",command=self.exit_).place(x=1200,y=5,width=200,height=40)


        # Define Content_Window
        self.bg_img = Image.open("images/bg.png")
        # self.bg_img = self.bg_img.resize((920,350) ,Image.ANTIALIAS)
        # Other filters you can use
        filters = [Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]
        self.bg_img = self.bg_img.resize((920,350), filters[0])  # Change the index to use different filters
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=500,y=180,width=920,height=350)

        # Update Details
        self.lbl_course = Label(self.root,text="Total Courses\n[ 0 ]", font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=500,y=530,width=300,height=100)

        self.lbl_student = Label(self.root,text="Total Students\n[ 0 ]", font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=810,y=530,width=300,height=100)

        self.lbl_result = Label(self.root,text="Total Ressults\n[ 0 ]", font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1120,y=530,width=300,height=100)

        # Clock 
        self.lbl=Label(self.root,text="\nWebCode Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=30,y=180,height=450,width=400)
        # self.clock_image()
        self.working()


        # Define Footer 
        footer = Label(self.root,text="SRMS--Student Result Managment System\nContact Us For Any Technical Issue: 969xxxxx77", font=("goudy old style",12), bg="#262626", fg="white").pack(side = BOTTOM, fill = X)
        self.update_details()
# ==========================================

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
    
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
           
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
           
            self.lbl_course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        # print(h,m,s)
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        # self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.img = Image.open("images/clock_new.png")
        self.img = ImageTk.PhotoImage(self.img)

        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        # # For Clock Image 
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))

        # Formula to rotate the clock 

        # angle_in_radians = angle_in_degrees*math.pi/180
        # line_length=100
        # centre_x = 250
        # centre_y = 250
        # end_x = centre_x + line_length * math.cos(angle_in_radians)
        # end_y = centre_y - line_length * math.sin(angle_in_radians)

        # Hour Line Image 
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)

        # Minute Line Image 
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)

        # Second Line Image 
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)

        # Draw Ellipse
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        
        clock.save("images/clock_new.png")


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)    

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)    

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)    

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)    
 
    def logout(self):
        op=messagebox.askyesno("Confirm","Do You really want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do You really want to Exit",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()