import pyodbc 

class Dtbase:
    conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=HAEL;'
                            'Database=AI_ASSISTANT;'
                            'Trusted_Connection=yes;')

    cursor = conn.cursor()

    ai_name = ''
    username = ''
    memory = []
    email = ''
    emailpass = ''

    def __init__(self):
        self.cursor = Dtbase.cursor
        return
        
    
    def queryDb(self):
        with Dtbase.conn:    
            query = ('select AI_NAME from ASSISTANT.AI')
            for row in Dtbase.cursor.execute(query):
                Dtbase.ai_name = row[0]

            query = ('select Name from AI_USER.INFO')
            for row in Dtbase.cursor.execute(query):
                Dtbase.username = row[0]
            
            query = ('select Memory from AI_USER.DATA')
            for row in Dtbase.cursor.execute(query):
                self.memory.append(row[0])

            query = ('select Email from AI_USER.INFO')
            for row in Dtbase.cursor.execute(query):
                Dtbase.email = row[0]

            query = ('select EmailPassword from AI_USER.INFO')
            for row in Dtbase.cursor.execute(query):
                Dtbase.emailpass = row[0]                
        return

    def dbreset(self):
        Dtbase.cursor.execute('exec dbreset')
        return

    def setupApp(self, aname, uname, password):
        Dtbase.cursor.execute('exec setup ?, ?, ?', (aname, uname, password)) 
        Dtbase.conn.commit()
        return

    def setupMail(self, email, password, uname):
        Dtbase.cursor.execute('exec mail ?, ?, ?', (email, password, uname))
        Dtbase.conn.commit()
        return

    def remember(self, memdata):
        Dtbase.cursor.execute('insert into AI_USER.DATA values ?', (memdata))
        Dtbase.conn.commit()
        return
    
    def pwdcompare(self, password):
        query = Dtbase.cursor.execute('exec pwcompare ?', (password))
        for row in query:
            is_password = row[0] 
        return is_password

    def memoryCall(self):
        
        pass

Dtbase().queryDb()
