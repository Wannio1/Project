import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
import MySQLdb 


def click_Login(): 
    try:
        db = MySQLdb.connect('localhost', 'root', '', 'project_akhir')
        cursor = db.cursor() 

        # Use parameterized query to prevent SQL injection
        sql = "SELECT * FROM pemrograman WHERE username = %s AND password = %s"
        cursor.execute(sql, (input_username_login.get(),input_password.get()))
        result = cursor.fetchone()

        if result:
            showinfo("Success", "Login successful!")
            main_menu()
        else:
            showerror("Error", "Invalid username or password.")
    
    except MySQLdb.Error as e:
        showerror("Database Error", str(e))
    
    finally:
        if db:
            db.close()

def click_Registrasi_open_window():
    window_login.withdraw()  # Hide login window
    register_window.deiconify()  # Show register window

def click_Registrasi():
    try:
        db = MySQLdb.connect('localhost', 'root', '', 'project_akhir')
        cursor = db.cursor()

        # Use parameterized query to prevent SQL injection
        sql = "INSERT INTO pemrograman (Username, Password) VALUES (%s, %s)"
        cursor.execute(sql, (input_register_username.get(),input_register_password.get()))
        db.commit()
        
        showinfo("Success", "Registration successful!")
        register_window.withdraw()
        window_login.deiconify()

    except MySQLdb.Error as e:
        showerror("Database Error", str(e))
    
    finally:
        if db:
            db.close()

def main_menu():
    window_login.withdraw()  # Hide login window
    main_window = tk.Tk()
    main_window.title('Login')
    main_window.geometry('400x540')
    main_window.configure(bg='white')
    main_window.resizable(False,False)

    label = tk.Label(main_window, text="Welcome to the Project Akhir Ridwan ", font=("Arial", 16))
    label.pack(pady=10, fill='both', expand=True)

    button = ttk.Button(main_window, text="Logout", command=main_window.destroy)
    button.pack(padx=20, pady=10)

    main_window.mainloop()

window_login = tk.Tk()
window_login.title("Login")
window_login.geometry('400x540')
window_login.configure(bg='white')
window_login.resizable(False,False)

frame_login = tk.Frame(window_login)
frame_login.pack(padx=20,pady=10,fill='x', expand=True)

#                   Header              
login_label = tk.Label(frame_login, text="Login", font=("Arial", 16))
login_label.pack(pady=10, fill='x', expand=True)

#               Input Username dan Password
label_username_login = ttk.Label(frame_login,text='Username',font=('Arial',10))
label_username_login.pack(padx=20,pady=5, fill='x', expand=True)
input_username_login = ttk.Entry(frame_login)
input_username_login.pack(padx=20,pady=5,fill='x',expand=True)


label_password_login = ttk.Label(frame_login,text="Password",font=('Arial',10))
label_password_login.pack(padx=20,pady=5,fill='x',expand=True)
input_password = ttk.Entry(frame_login,show='*')
input_password.pack(padx=20,pady=5,fill='x',expand=True)

click_Login = ttk.Button(frame_login,text="Login",command=click_Login)
click_Login.pack(padx=90,pady=15)

click_Registrasi_open_window = ttk.Button(frame_login,text="Registrasi",command=click_Registrasi_open_window)
click_Registrasi_open_window.pack(padx=90,pady=5)

###############################
register_window = tk.Toplevel()
register_window.title('Register')
register_window.geometry('400x450')
register_window.resizable(False,False)
register_window.withdraw() 

frame_register = tk.Frame(register_window)
frame_register.pack(padx=20,pady=10,fill='x', expand=True)

#                   Header              
register_label = tk.Label(frame_register, text="Register", font=("Arial", 16))
register_label.pack(pady=10, fill='x', expand=True)

ttk.Label(frame_register, text="Email").pack(padx=10, pady=5, fill='x',expand=True)
input_register_email = ttk.Entry(frame_register)
input_register_email.pack(padx=10, pady=5, fill='x', expand=True)

ttk.Label(frame_register, text="Username").pack(padx=10, pady=5, fill='x',expand=True)
input_register_username = ttk.Entry(frame_register)
input_register_username.pack(padx=10, pady=5, fill='x', expand=True)

ttk.Label(frame_register, text="Password").pack(padx=10, pady=5, fill='x',expand=True)
input_register_password = ttk.Entry(frame_register, show="*") 
input_register_password.pack(padx=10, pady=5, fill='x', expand=True)


# Register button
ttk.Button(frame_register, text="Register", command=click_Registrasi).pack(padx=20, pady=10)

# Button to go back to login
ttk.Button(frame_register, text="Back to Login", command=lambda: [register_window.withdraw(), window_login.deiconify()]).pack(padx=20, pady=5)


frame_login.mainloop()