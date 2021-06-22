import mysql.connector 
from django.shortcuts import render 

def home(request):
    try:
        myconnection = mysql.connector.connect(username='root',password='Smarty@123', host='localhost', database='testdb')
        mycursor = myconnection.cursor()
        mycursor.execute('select * from vw_caseproducts')
        results  = mycursor.fetchall()
        print(results )
        return render(request, 'home.html', {'results':results})
    except mysql.connector.Error as error:
        print("error {} ".format(error))
    finally:
        mycursor.close()
        myconnection.close()
