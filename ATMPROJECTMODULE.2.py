import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9625789430",
    database="bank"
)

def display_menu():
    while True:
        print("\n===== ATM Machine =====")
        print("1. Open a New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. account details")
        print("5. EXIT")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            open_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
               acc_details()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

mycursor=mydb.cursor()


def open_account():
  r= input("enter acc_no")
  n= input ("enter name")
  i= input("enter address")
  m= input ("enter phone_number")
  n= input ("enter balance")
  j= input ("enter status")
  sql ="insert into acc_details(acc_no,name,address,phone_number,balance,status) values('"+r+"','"+n+"','"+i+"','"+m+"','"+n+"','"+j+"')"
  mycursor.execute(sql)
  mydb.commit()
  print("data inserted")
 
def display():
 r=input("enter the acc_no")
 sql="select * from acc_details where acc_no='"+r+"'"
 n=input("enter the balance")
 sql="select * from acc_details where acc_no='"+n+"'"
 mycursor.execute(sql)
 r=mycursor.fetchall()
 n=mycursor.fetchall()
 



def deposit_money():
   
    an=input("Enter the account no")
    amt=input("Enter the amount to b e deposit")
    d=input("Enter date")
    ty="deposit"
    sql="select * from acc_details where acc_no='"+ an+"'"
    at=amt
    mycursor.execute(sql)
    r=mycursor.fetchall()
    p=0
    x=0
    if r!=[]:
       for i in r:
          p=i[4]
       x=int(p)+int(amt)
       print(amt)
       sql1="update acc_details set balance='"+ str(x)+"' where acc_no='"+an+"'"
       mycursor.execute(sql1)
       mydb.commit()
       sql2="insert into trans value('"+an+"','"+ty+"','"+at+"','"+d+"')"
       mycursor.execute(sql2)
       mydb.commit()
       print("Deposit successful. New balance:")

    else:
        print("Account not found.")




def withdraw_money():
   
    an=input("Enter the account no")
    amt=input("Enter the amount to b e withdraw")
    d=input("Enter date")
    ty="withdraw"
    sql="select * from acc_details where acc_no='"+ an+"'"
    at=amt
    mycursor.execute(sql)
    r=mycursor.fetchall()
    p=0
    x=0
    if r!=[]:
       for i in r:
          p=i[4]
       print(p)
       if int(p)>=int(amt):
        x=int(p)-int(amt)
        print(amt)
        sql1="update acc_details set balance='"+ str(x)+"' where acc_no='"+an+"'"
        mycursor.execute(sql1)
        mydb.commit()
        sql2="insert into trans value('"+an+"','"+ty+"','"+at+"','"+d+"')"
        mycursor.execute(sql2)
        mydb.commit()
        print("withdraw successful. New balance:")
       else:
         print("insuficent amount")
    else:
        print("Account not found.")
def acc_details():
    acc_no = input("Enter the account number: ")
    sql = "SELECT * FROM acc_details WHERE acc_no = %s"
    mycursor.execute(sql, (acc_no,))
    result = mycursor.fetchone()

    if result:
        print("\n===== Account Details =====")
        print(f"Account No: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Address: {result[2]}")
        print(f"Phone Number: {result[3]}")
        print(f"Balance: {result[4]}")
        print(f"Status: {result[5]}")
    else:
        print("Account not found.")#




display_menu()

      

