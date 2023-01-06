#Name:Lakshmi K 
#UIC Email: lkris2@uic.edu
#Signature:I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s Academic Integrity standards. Signed:Lakshmi Krishnan
import pandas 
import pickle
import sqlite3
daytypes=['A','W','U']
def extract(filename,dbname):
  """insert table and add values to the columns"""
  data=pandas.read_csv(filename)
  conn=sqlite3.connect(dbname)
  curr=conn.cursor()
  #connecting to database and reading csv file using pandas 
  curr.execute("CREATE TABLE BusData(route,date,daytype,rides)")
   
  for i in range(len(data)):
      a = data['route'][i]
      b = data['date'][i]
      c = data['daytype'][i]
      d = data['rides'][i]
  curr.execute("INSERT INTO BusData VALUES (%f, %f, %s, %f)" % (a,b,c,d))
  #SQLite command to create a table and insert values from the csv files into a database
extract("bus_data.csv","bus_data.db")

def average():
  """compute average of rides"""
  conn=sqlite3.connect("bus_data.db")
  cur=conn.cursor()
  cur.execute("SELECT AVG('rides') FROM BusData")
  #computes the average of rides column from table
  
def dt_ave(**daytypes):
  """compute averages based on the user's input as keywords with day types"""
  conn=sqlite3.connect("bus_data.db")
  cur=conn.cursor()
  display_average=cur.execute("SELECT AVG(rides) FROM BusData WHERE daytype in 'daytypes'")
  #eturns the average daily ridership for all routes but only for those days which have a daytype matching the specified ones
  if daytypes==None:
    daytypes=['A','W','U']
    for i in daytypes:
      cur.execute(" SELECT AVG(rides) FROM BusData WHERE daytype in 'daytypes'")
  #By default, returns the list of average daily ridership filtered by every daytype
  db_entries=display_average.fetch_all()
  for entry in db_entries:
    print(entry)
  #fetch data from database
  conn.commit()
  conn.close()

  
def update():
  """creates a copy using pickle before update a value in the table"""
  conn=sqlite3.connect("bus_data.db")
  cur=conn.cursor()
  data=pandas.read_csv("bus_data.csv")
  with open("pickled_data.p",'wb') as f:
    pickle.dump([data],f)
  #creating a copy of the csv file using pickle module
  for n in range(12):
    for j in range(2000,2021):
      cur.execute("UPDATE BusData SET rides=rides+10 WHERE route=3 AND WHERE ({}/01/{})".format(n,j))
  #updating by adding 10 to route 3’s daily ridership for the first day of every month in the database



                  
def my_func():
  conn=sqlite3.connect("bus_data.db")
  cur=conn.cursor()
  pre_pandemic=[]
  post_pandemic=[]
  #create a list to add average of daily ridership based on date
  for i in range(2020,2022):
    for r in range(23):
      for l in range(12):
        if i==2020:
          for l in range(5,12):
              avg_ride_1=cur.execute("SELECT AVG(rides) FROM BusData WHERE ({}/{}/{})".format(i,l,r))
  post_pandemic.append(avg_ride_1)
#avg_ride_1 computes average of rides of days before the pandemic
  
  for y in range(2000,2020):
     for d in range(23):
      for m in range(12):
        if i==2020:
          for l in range(1,5):
            avg_ride_2=cur.execute("SELECT AVG(rides) FROM BusData WHERE ({}/{}/{})".format(m,d,y))
        pre_pandemic.append(avg_ride_2)
#avg_rides_2 computes averages of rides of days after the pandemic    
average()
dt_ave(daytypes=['U','A'])
update()
my_func()
    