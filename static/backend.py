import psycopg2

conn = psycopg2.connect(
        dbname="userdatabase",
        user="avguser",
        password="blegh3",
        host="localhost",
        port="5432"
    )
cur = conn.cursor()



class createGame():
    complete = False
    def __init__(self, name, area, achieve):
        self.name = name
        self.area = area
        self.achieve = achieve
    
BreakOut = createGame("Break Out", "Home", "Broken Heart...")
Platform = createGame("Platformer", "Portfolio", "Stepping Up!")
AimTrain = createGame("Aim Trainer", "Requests", "Frustrated?")

gameList = [BreakOut, Platform, AimTrain]

def checkGames(gameList):
    for game in gameList:
        print(f"{game.name}'s completion status: {game.complete}")

checkGames(gameList)

IDLIST = []

class userDatabase():
    AchList = []
    def __init__(self, username, email, password, provID, joinDate):
        self.name = username
        self.email = email
        self.password = password # Yes I know, passwords should not be stored this way. I will be integrating a different system soon.
        self.id = provID
        self.joinDate = joinDate
    def addAchieve(self, achieve):
        self.AchList.append(achieve)
        print(f"Achievement Get: {achieve}")

def Login(cur):
    inDatabase = False
    loginApproved = False
    loginUser = input("Please enter a valid username: ")
    cur.execute('SELECT userName from userdata.LoginInfo')
    for row in cur:
        if row[0] == loginUser:
            print("correct, continue")
            inDatabase = True
            break
        else:
            continue
    if inDatabase == True:
        cur.execute(f"SELECT password FROM userdata.LoginInfo WHERE username = '{loginUser}'")
        while loginApproved == False:
            userPass = input("Please enter your password: ")
            if userPass == 'exit':
                print("sorry about your password.")
                quit()
            for row in cur:
                if userPass == row[0]:
                    loginApproved = True
                    break
                else: 
                    print("Please try again or enter 'exit' to stop.")
                    continue
        if loginApproved == True:
            print("Thank you, here are your current stats.")
            cur.execute(f"SELECT * FROM userdata.LoginInfo WHERE userName = '{loginUser}'")
            for row in cur:
                loggedUser = userDatabase(row[1], row[3], row[2], row[0], row[4])
        elif loginApproved == False:
            print("Please try again.")
            quit()
    elif inDatabase == False:
        print("Please enter a diffrent username.")
        quit()
    return loggedUser
        
loggedUser = Login(cur)

loggedUser.addAchieve(BreakOut.achieve)

def printUserData(user):
    print(f"ID: {user.id}, USERNAME: {user.name}, EMAIL: {user.email}")
    print(f"Achievements: {user.AchList}")


printUserData(loggedUser)

