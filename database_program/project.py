import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="hiren@8469",
    database="college"
)

mycur=db.cursor()

while True:

  print("1. Insert Data")
  print("2. Find Data")
  print("3. Update Data")
  print("4. Delete Data")
  print("5. Exit")


  hoice = input("choice option enter karo (1-5): ")

  if hoice == '1':
    id=int(input("Enter id: "))
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    sql="INSERT INTO first(id,name,age) values(%s,%s,%s)"
    val=(id,name,age)
    mycur.execute(sql,val)
    db.commit()
    print(mycur.rowcount,"record inserted \n")

  elif hoice == '2':
    mycur.execute("SELECT * FROM first")
    result=mycur.fetchall()
    for i in result:
        print(i)

  elif hoice == '3':
    print("What do you want to update?")
    print("1. Name")
    print("2. Age")

    user_choice = input("Enter option (1/2): ")
    if user_choice == '1':
        id=int(input("Enter id: "))
        name=input("Enter new name: ")
        sql="UPDATE first SET name=%s WHERE id=%s"
        val=(name,id)
        mycur.execute(sql,val)
        db.commit() 
        print(mycur.rowcount,"record updated \n")
    elif user_choice == '2':
        id=int(input("Enter id: "))
        age=input("Enter new age: ")
        sql="UPDATE first SET age=%s WHERE id=%s"
        val=(age,id)
        mycur.execute(sql,val)
        db.commit() 
        print(mycur.rowcount,"record updated \n")
    else:
        print("Invalid option")

  elif hoice == '4':
    id=int(input("Enter id to delete: "))
    sql="DELETE FROM first WHERE id=%s"
    val=(id,)
    mycur.execute(sql,val)
    db.commit()
    print(mycur.rowcount,"record deleted")

  elif hoice == '5':  
    print("Exit")
    break

 


        

    

    

