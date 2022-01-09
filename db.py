
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "zamir",
    password = "galica124",
    database = "nea",
    auth_plugin='mysql_native_password'
    )

mycursor = db.cursor()

#make a function to access the db
def user_login(tup):
    try:
        getUn = "SELECT username FROM student WHERE username='" + str(tup[0]) + "';"
        mycursor.execute(getUn)
        usernameCheck = mycursor.fetchall()
        if usernameCheck == []: #username not in db
            return "Username incorrect"
        else:
            getPw = "SELECT studentpassword FROM student WHERE studentpassword='" + str(tup[1]) + "';"
            mycursor.execute(getPw)
            passwordCheck = mycursor.fetchall()
            if passwordCheck == []: #password not in db
                return "Password incorrect"
            else:
                return True
    except:
        return False

def teacher_login(tup):
    try:
        getUn = "SELECT username FROM teacher WHERE username='" + str(tup[0]) + "';"
        mycursor.execute(getUn)
        usernameCheck = mycursor.fetchall()
        if usernameCheck == []: #username not in db
            return "Username incorrect"
        else:
            getPw = "SELECT teacherpassword FROM teacher WHERE teacherpassword='" + str(tup[1]) + "';"
            mycursor.execute(getPw)
            passwordCheck = mycursor.fetchall()
            if passwordCheck == []: #password not in db
                return "Password incorrect"
            else:
                return True
    except:
        return False

def subject_check(username):
    try:
        getSub = "SELECT subjects FROM student WHERE username ='" + username + "';"
        mycursor.execute(getSub)
        subject = mycursor.fetchall()
        subject = str(subject[0])
        subject = subject.strip("()',")
        return subject
    except:
        return False

def class_check(username, classID):
    try:
        getTeacherID = "SELECT teacherID FROM teacher WHERE username = '" + username + "';"
        mycursor.execute(getTeacherID)
        teacherID = mycursor.fetchall()[0][0]

        getClass = "SELECT classID, teacherID FROM classes WHERE classes.teacherID ='" + str(
            teacherID) + "' AND classes.classID = '" + str(classID) + "';"
        mycursor.execute(getClass)
        test = mycursor.fetchall()

        checkTeacherInClass = False

        if test[0][0] == 'False':
            checkTeacherInClass = False
        elif test[0][0] == classID and test[0][1] == teacherID:
            checkTeacherInClass = True

        return checkTeacherInClass
    except:
        return False


def get_topics(tableName, topicID):
    try:
        getTopic = "SELECT " + str(topicID) + " FROM " + str(tableName) + ";"
        mycursor.execute(getTopic)
        sub_topics = mycursor.fetchall()
        topicList = []
        for topics in sub_topics:
            topics = str(topics)
            topics = topics.strip("()',")
            topicList.append(topics)
        return topicList
    except:
        return False



def get_Quiz(table):
    try:
        quizName = table + "Quiz"
        query = "SELECT questions, correct_answer, wrong_answer1, wrong_answer2 FROM " \
                + str(table) + " JOIN (" + str(quizName) + ") ON (" \
                + str(table) + ".quizID = " + str(quizName) + ".quizID);"
        mycursor.execute(query)
        quiz = mycursor.fetchall()
        return quiz
    except:
        return False

def addScoreToDB(username, score, topic):
    try:
        # 0 - get id of student using select student id from student where username=self.username
        getStudentID = "SELECT studentID FROM student WHERE username = '" + str(username) + "';"
        mycursor.execute(getStudentID)
        studentID = mycursor.fetchall()[0][0]

        # 1: select quiz grades id from quiz table
        topicQuiz = topic + "Quiz"
        getQuizGradeID = "SELECT gradeID FROM " + str(topicQuiz) + ";"
        mycursor.execute(getQuizGradeID)
        quizGradeID = mycursor.fetchall()[0][0]

        # 2: insert into quiz grade id score, userid
        insertScore = "INSERT INTO " + str(quizGradeID) + " (gradeID, studentID, grade) VALUES (\"" + str(
            quizGradeID) + "\", \"" + str(studentID) + "\", \"" + str(score) + "\");"
        mycursor.execute(insertScore)
        db.commit()

        return 1
    except:
        return False

def getQuestionAmount(topic):
    quiz = topic + "Quiz"
    questionCount = "SELECT COUNT(*) FROM " + quiz + ";"
    mycursor.execute(questionCount)
    questionAmount = mycursor.fetchall()
    return questionAmount[0][0]


def addQuestion(q, a, wa1, wa2, topic):
    try:
        #first get the quizID
        quizID = "SELECT quizID FROM " + str(topic) + ";"
        mycursor.execute(quizID)
        qid = mycursor.fetchall()[0][0]

        gradeID = qid + "QGrades"

        quizName = topic + "Quiz"
        insertQuestion = "INSERT INTO " + str(quizName) + " (quizID, questions, correct_answer, wrong_answer1, wrong_answer2, gradeID) VALUES (\"" + str(qid) + "\", \"" + str(q) + "\", \"" + str(a) + "\", \"" + str(wa1) + "\", \"" + str(wa2) + "\", \"" + str(gradeID) + "\");"

        mycursor.execute(insertQuestion)

        db.commit()
        return True
    except:
        return False

def add_student(n, a, c, s, sp, u, g):
    try:
        teacherID = "SELECT quizID FROM teacher;"
        mycursor.execute(teacherID)
        insertStudent = "INSERT INTO student (name,age,class,subjects,studentpassword,username,gender) VALUES (\"" + str(n) + "\", \"" + str(a) + "\", \"" + str(c) + "\", \"" + str(s) + "\", \"" + str(sp) + "\", \"" + str(u) + "\",\"" + str(g) + "\");"
        mycursor.execute(insertStudent)
        db.commit()
        return True
    except:
        return False






