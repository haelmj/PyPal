import pyodbc
import pandas as pd 

class Dtbase:
    conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=HAEL;'
                            'Database=AI_ASSISTANT;'
                            'Trusted_Connection=yes;')

    cursor = conn.cursor()

    ai_name = ''
    username = ''
    passcode = ''
    memory = []

    def __init__(self):
        self.cursor = Dtbase.cursor
        return
        
    
    def queryDb(self):
#       cursor.execute('select AI_NAME from ASSISTANT.AI')
#       for row in cursor: Dtbase.ai_name = row
        with Dtbase.conn:    
            query = ('select AI_NAME from ASSISTANT.AI')
            for row in Dtbase.cursor.execute(query):
                Dtbase.ai_name = row[0]

            query = ('select Name from AI_USER.INFO')
            for row in Dtbase.cursor.execute(query):
                Dtbase.username = row[0]
            
            query = ('select Passcode from AI_USER.INFO')
            for row in Dtbase.cursor.execute(query):
                Dtbase.passcode = row[0]
            
            query = ('select Memory from AI_USER.DATA')
            for row in Dtbase.cursor.execute(query):
                self.memory.append(row[0])    
        return

    def dbreset(self):
        Dtbase.cursor.execute('exec dbreset')
        return

    def setupApp(self, aname, uname, password):
        Dtbase.cursor.execute('exec setup ?, ?, ?', (aname, uname, password)) # add insert statement 
        Dtbase.conn.commit()
        return

    def remember(self, memdata):
        Dtbase.cursor.execute('insert into AI_USER.DATA values ?', (memdata))
        Dtbase.conn.commit()
        return

Dtbase().queryDb()
