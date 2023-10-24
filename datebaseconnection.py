import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "zamir",
    password = "password",
    database = "nea",
    auth_plugin='mysql_native_password'
    )

mycursor = db.cursor()

#HARDCODED VALUES AND DATABASE CONNECTION TESTS###
###STUDENT TABLE CREATION###

"""
mycursor.execute("DROP TABLE student;")
mycursor.execute("CREATE TABLE student ("
                 "name VARCHAR(50), "
                 "age smallint UNSIGNED, "
                 "class VARCHAR(20), "
                 "subjects VARCHAR(30), "
                 "studentID int PRIMARY KEY AUTO_INCREMENT, "
                 "studentpassword CHAR(60),"
                 "username VARCHAR(20),"
                 "gender VARCHAR(20));")

mycursor.execute("DELETE FROM student;")
mycursor.execute("TRUNCATE student;")

mycursor.execute("INSERT INTO student (name, age, gender , subjects, username, studentpassword, class) VALUES"
                 "(\"Zamir\", 17, \"Male\", \"Computer science\",\"Zamir1\", \"Zamir123\", \"CS1\"), "
                 "(\"Eris\", 17, \"Male\", \"Media\",\"Eris1\", \"Eris123\", \"ME1\"), "
                 "(\"Erina\", 17, \"Female\", \"Economics\",\"Erina1\", \"Erina123\", \"EC1\"),"
                 "(\"Ervin\", 17, \"Male\", \"Computer science\",\"Ervin1\", \"Ervin123\", \"CS2\"), "
                 "(\"Nahum\", 17, \"Male\", \"Media\",\"Nahum1\", \"Nahum123\", \"ME2\"), "
                 "(\"Blini\", 17, \"Male\", \"Economics\",\"Blini1\", \"Blini123\", \"EC2\"); "
                 )

db.commit()

###TEACHER TABLE CREATION###

mycursor.execute("DROP TABLE teacher;")
mycursor.execute("CREATE TABLE teacher ("
                 "name VARCHAR(50), "
                 "age smallint UNSIGNED, "
                 "class VARCHAR(20), "
                 "subjects VARCHAR(30), "
                 "teacherID int PRIMARY KEY,"
                 "teacherpassword CHAR(60), "
                 "username VARCHAR(20),"
                 "gender VARCHAR(20));")

mycursor.execute("DELETE FROM teacher;")
mycursor.execute("TRUNCATE teacher;")
mycursor.execute("INSERT INTO teacher (name, age, gender , subjects, username, teacherpassword, class, teacherID) VALUES"
                 "(\"Alexander\", 23, \"Male\", \"Computer science\",\"Alexander1\", \"Alexander123\", \"CS1\",0), "
                 "(\"Bob\", 55, \"Male\", \"Media\",\"Bob1\", \"Bob123\", \"ME1\",1), "
                 "(\"Enisa\", 27, \"Female\", \"Economics\",\"Enisa1\", \"Enisa123\", \"EC1\",2), "
                 "(\"James\", 33, \"Male\", \"Computer science\" , \"James1\" , \"James123\", \"CS2\",3), "
                 "(\"Tommy\", 41, \"Male\", \"Media\" , \"Tommy1\" , \"Tommy123\", \"ME2\",4), "
                 "(\"Amy\", 24, \"Female\", \"Economics\" , \"Amy1\" , \"Amy123\", \"EC2\",5); "
                 )

###SUBJECT TABLE CREATION###

mycursor.execute("DROP TABLE subjects;")
mycursor.execute("CREATE TABLE subjects ("
                 "subjectID VARCHAR(10) PRIMARY KEY);"
                 )

mycursor.execute("INSERT INTO subjects (subjectID) VALUES"
                 "(\"CS\"),"
                 "(\"ME\"),"
                 "(\"EC\");"
                 )
db.commit()


###CLASSES TABLE CREATION###



#mycursor.execute("DROP TABLE classes;")
mycursor.execute("CREATE TABLE classes ("
                 "classID VARCHAR(10) PRIMARY KEY,"
                 "teacherID int,"
                 "FOREIGN KEY(teacherID) REFERENCES teacher(teacherID));"
                 )
mycursor.execute("INSERT INTO classes (classID, teacherID) VALUES"
                 "(\"CS1\", 0),"
                 "(\"ME1\", 1),"
                 "(\"EC1\", 2),"
                 "(\"CS2\", 3),"
                 "(\"ME2\", 4),"
                 "(\"EC2\", 5);"
                 )
db.commit()


###CLASSES TABLE CREATION###
###CLASS CS1 AND CS2 TABLE CREATION###

mycursor.execute("DROP TABLE CS1;")
mycursor.execute("CREATE TABLE CS1 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )
mycursor.execute("INSERT INTO CS1 (classID, studentID) VALUES"
                 "(\"CS1\",0);"

                 )
db.commit()

mycursor.execute("DROP TABLE CS2;")
mycursor.execute("CREATE TABLE CS2 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )
mycursor.execute("INSERT INTO CS2 (classID, studentID) VALUES"
                 "(\"CS2\" , 3);"
                  )
db.commit()

###CLASS ME1 AND ME2 TABLE CREATION###

mycursor.execute("DROP TABLE ME1;")
mycursor.execute("CREATE TABLE ME1 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )

mycursor.execute("INSERT INTO ME1 (classID, studentID) VALUES"
                 "(\"ME1\" , 1);"
                  )
db.commit()

mycursor.execute("DROP TABLE ME2;")
mycursor.execute("CREATE TABLE ME2 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )
mycursor.execute("INSERT INTO ME2 (classID, studentID) VALUES"
                 "(\"ME2\" , 4);"
                   )
db.commit()

###CLASS EC1 AND EC2 TABLE CREATION###

mycursor.execute("DROP TABLE EC1;")
mycursor.execute("CREATE TABLE EC1 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )
mycursor.execute("INSERT INTO EC1 (classID, studentID) VALUES"
                 "(\"EC1\" , 3);"
                 )
db.commit()

mycursor.execute("DROP TABLE EC2;")
mycursor.execute("CREATE TABLE EC2 ("
                 "classID VARCHAR(10),"
                 "studentID int,"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID));"
                 )
mycursor.execute("INSERT INTO EC2 (classID, studentID) VALUES"
                 "(\"EC2\" , 5);"
                   )
db.commit()

###CS TOPICS TABLE CREATION###

mycursor.execute("DROP TABLE cs_topics;")

mycursor.execute("CREATE TABLE cs_topics ("
                 "cs_topicID VARCHAR(50) PRIMARY KEY),"
                 "subjectID VARCHAR(10),"
                 "FOREIGN KEY(subjectID) REFERENCES subjects(subjectID));"
                 )

mycursor.execute("DELETE FROM cs_topics;")

mycursor.execute("INSERT INTO cs_topics (cs_topicID , subjectID) VALUES"
                 "(\"ComputerNetworks\", \"CS\"),"
                 "(\"ComputerSystems\", \"CS\"),"
                 "(\"DataAndInformation\", \"CS\"),"
                 "(\"DataStructuresAndAlgorithms\", \"CS\"),"
                 "(\"ProgrammingFundamentals\", \"CS\");"
                 )
db.commit()

###CS TOPIC CLASS TABLE CREATION###

mycursor.execute("DROP TABLE ComputerScience;")
mycursor.execute("CREATE TABLE ComputerScience ("
                 "subjectID VARCHAR(10),"
                 "teacherID int,"
                 "classID VARCHAR(10),"
                 "FOREIGN KEY(subjectID) REFERENCES subjects(subjectID),"
                 "FOREIGN KEY(teacherID) REFERENCES teacher(teacherID),"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "cs_topics VARCHAR(50));"
                 )

mycursor.execute("INSERT INTO ComputerScience(subjectID , teacherID, classID, cs_topics) VALUES"
                 "(\"CS\", 0, \"CS1\", \"ComputerNetworks\"),"
                 "(\"CS\", 0, \"CS1\", \"ComputerSystems\"),"
                 "(\"CS\", 0, \"CS1\", \"DataAndInformation\"),"
                 "(\"CS\", 0, \"CS1\", \"DataStructuresAndAlgorithms\"),"
                 "(\"CS\", 0, \"CS1\", \"ProgrammingFundamentals\");"
                 )
db.commit()

mycursor.execute("INSERT INTO ComputerScience(subjectID , teacherID, classID, cs_topics) VALUES"
                 "(\"CS\", 3, \"CS2\", \"ComputerNetworks\"),"
                 "(\"CS\", 3, \"CS2\", \"ComputerSystems\"),"
                 "(\"CS\", 3, \"CS2\", \"DataAndInformation\"),"
                 "(\"CS\", 3, \"CS2\", \"DataStructuresAndAlgorithms\"),"
                 "(\"CS\", 3, \"CS2\", \"ProgrammingFundamentals\");"
                 )
db.commit()

mycursor.execute("DROP TABLE ComputerNetworks;")
mycursor.execute("CREATE TABLE ComputerNetworks ("
                 "cs_topicID VARCHAR(50),"
                 "FOREIGN KEY(cs_topicID) REFERENCES cs_topics(cs_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )

mycursor.execute("INSERT INTO ComputerNetworks (cs_topicID , quizID) VALUES"
                 "(\"ComputerNetworks\" , \"CN\");"
                 )
db.commit()

mycursor.execute("DROP TABLE ComputerNetworksQuiz;")
mycursor.execute("CREATE TABLE ComputerNetworksQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES ComputerNetworks(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES CNQGrades(gradeID));"
                )

###CS QUIZ GRADE TABLE CREATION - CONTINUED FURTHER DOWN###

mycursor.execute("DROP TABLE CNQGrades;")
mycursor.execute("CREATE TABLE CNQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("DELETE FROM ComputerNetworksQuiz;")
mycursor.execute("INSERT INTO ComputerNetworksQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"CN\",\"What is a network?\",\"Two or more computers connected together\",\"A standalone computer\",\"Two or more computers working in tandem\",\"CNQGrades\"),"
                 "(\"CN\",\"What is a LAN?\",\"Local area network\",\"Large area network\",\"Large arrayed network\",\"CNQGrades\"),"
                 "(\"CN\",\"Which device may contain a modem?\",\"A router\",\"A switch\",\"A hub\",\"CNQGrades\"),"
                 "(\"CN\",\"What is a server?\",\"A computer that manages and stores files\",\"A computer that is connected to the internet\",\"A collection of high speed computers\",\"CNQGrades\"),"
                 "(\"CN\",\"Why are fibre optic cables better than copper?\", \"Higher data transfer rate\",\"They are cheaper\",\"More flexible\",\"CNQGrades\"),"
                 "(\"CN\",\"What is the purpose of a router?\",\"To connect networks together\",\"To broadcast messages across a network\",\"Translate a domain name into an internet address\",\"CNQGrades\"),"
                 "(\"CN\",\" Which is a disadvantage of wireless connection?\",\"Limited connection range\", \"Freedom of movement\",\"Users cannot share files\",\"CNQGrades\"),"
                 "(\"CN\",\"What is a PAN?\",\"Personal area network\",\"Protected area network\", \"Person array network\",\"CNQGrades\"),"
                 "(\"CN\",\"Which of these is a WAN?\",\"The internet\",\"A business network within one building\",\"A network within two buildings on the same site\",\"CNQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE ComputerSystems;")
mycursor.execute("CREATE TABLE ComputerSystems ("
                 "cs_topicID VARCHAR(50),"
                 "FOREIGN KEY(cs_topicID) REFERENCES cs_topics(cs_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                  )
mycursor.execute("INSERT INTO ComputerSystems (cs_topicID , quizID) VALUES"
                 "(\"ComputerSystems\" , \"CSY\");"
                 )
db.commit()

mycursor.execute("DROP TABLE ComputerSystemsQuiz;")
mycursor.execute("CREATE TABLE ComputerSystemsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES ComputerSystems(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES CSQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE CSQGrades;")
mycursor.execute("CREATE TABLE CSQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY (studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO ComputerSystemsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"CSY\",\"What are computers used for?\",\"To perform multiple tasks\",\"To create iPhones\",\"To form a system\",\"CSQGrades\"),"
                 "(\"CSY\",\"What is clock speed measured in?\",\"Hertz\",\"Bytes\",\"Seconds\",\"CSQGrades\"),"
                 "(\"CSY\",\"Which are parts of the CPU?\",\"Registers,cache,ALU\",\"Registers,ROM,cache\",\"Resisters,ROM,ALU\",\"CSQGrades\"),"
                 "(\"CSY\",\"Which CPU component makes logical decisions?\",\"ALU\",\"Cache\",\"CU\",\"CSQGrades\"),"
                 "(\"CSY\",\"What is a register?\",\"High speed RAM\",\"High speed ROM\",\"A small computer\",\"CSQGrades\"),"
                 "(\"CSY\",\"What is a core?\",\"A processing unit in the CPU\",\"Reads data\",\"Executes data\",\"CSQGrades\"),"
                 "(\"CSY\",\"Name the three types of bus?\",\"Address,control,data\",\"Address,control,instruction\",\"Address,data,instruction\",\"CSQGrades\"),"
                 "(\"CSY\",\"Which statement of Von Neumann architecture is true?\",\"Data & instructions are both stored in main memory\",\"Data is stored in main memory\",\"Instructions are stored in main memory\",\"CSQGrades\"),"
                 "(\"CSY\",\"What is hardware?\",\"Physical components\",\"Attached to RAM\",\"Logical components\",\"CSQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE DataAndInformation;")
mycursor.execute("CREATE TABLE DataAndInformation ("
                 "cs_topicID int,"
                 "FOREIGN KEY(cs_topicID) REFERENCES cs_topics(cs_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO DataAndInformation (cs_topicID , quizID) VALUES"
                 "(\"DataAndInformation\" , \"DI\");"
                 )
db.commit()

mycursor.execute("DROP TABLE DataAndInformationQuiz;")
mycursor.execute("CREATE TABLE DataAndInformationQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES DataAndInformation(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES DIQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE DIQGrades;")
mycursor.execute("CREATE TABLE DIQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY)," 
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO DataAndInformationQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"DI\",\"Whats the left most digit called in binary?\",\"Most siginficant bit\",\"Least significant bit\",\"The first bit\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats the right most digit called in binary?\",\"Least significant bit\",\"Most significant bit\",\"The last bit\",\"DIQGrades\"),"
                 "(\"DI\",\"What base number does a hexadecimal value have?\",\"16\",\"32\",\"8\",\"DIQGrades\"),"
                 "(\"DI\",\"Why is hexadecimal used as a shorthand for binary?\",\"Easier for humans to read\",\"It is more efficient\",\"So that computers can't understand\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats ASCII?\",\"A common character set\",\"A programming language\",\"A calculator\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats unicode\",\"A advanced character set \",\"A old character set\",\"A programming language\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats metadata?\",\"Data about other data\",\"A large amount of data\",\"Data inputed by a user\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats a pixel?\",\"Smallest element of a graphic\",\"Size of a screen\",\"A large picture\",\"DIQGrades\"),"
                 "(\"DI\",\"Whats image resolution?\",\"How clear a image is\",\"How unclear a image is\",\"How large a image is\",\"DIQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE DataStructuresAndAlgorithms;")
mycursor.execute("CREATE TABLE DataStructuresAndAlgorithms ("
                 "cs_topic VARCHAR(50),"
                 "FOREIGN KEY(cs_topicID) REFERENCES cs_topics(cs_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO DataStructuresAndAlgorithms (cs_topicID , quizID) VALUES"
                 "(\"DataStructuresAndAlgorithms\" , \"DSA\");"
                 )
db.commit()

mycursor.execute("DROP TABLE DataStructuresAndAlgorithmsQuiz;")
mycursor.execute("CREATE TABLE DataStructuresAndAlgorithmsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES DataStructuresAndAlgorithms(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES DSAQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE DSAQGrades;")
mycursor.execute("CREATE TABLE DSAQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO DataStructuresAndAlgorithmsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"DSA\",\"What data structure can be used to check if a syntax has balanced parenthesis ?\",\"Stack\",\"List\",\"Tree\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Travelling salesman problem is an example of\",\"Greedy algorithm\",\"Dynamic algorithm\",\"Recursive approach\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Program with highest run-time complexity is?\",\"A way of defining,storing and retrieving of data in a structural way\",\"32\",\"8\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Why is hexadecimal used as a shorthand for binary?\",\"Tower of Hanoi\",\"Fibonacci Series\",\"Prime Number Series\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Whats a data-structure?\",\"A organization format\",\"How data is created\",\"Neither\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Whats a array\",\"Holds a number of data items\",\"A programming language\",\"Neither\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Whats a tree?\",\"A connected graph with no cycles\",\"A data type\",\"A unconnected graph\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Whats a stack?\",\"An abstract data type\",\"A graph\",\"Neither\",\"DSAQGrades\"),"
                 "(\"DSA\",\"Whats a tuple?\",\"An ordered sequence of elements\",\"Unordered sequence\",\"A data type\",\"DSAQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE ProgrammingFundamentals;")
mycursor.execute("CREATE TABLE ProgrammingFundamentals ("
                 "cs_topicID VARCHAR(50),"
                 "FOREIGN KEY(cs_topicID) REFERENCES cs_topics(cs_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO ProgrammingFundamentals (cs_topicID , quizID) VALUES"
                 "(\"ProgrammingFundamentals\" , \"PF\");"
                 )
db.commit()

mycursor.execute("DROP TABLE ProgrammingFundamentalsQuiz;")
mycursor.execute("CREATE TABLE ProgrammingFundamentalsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES ProgrammingFundamentals(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES PFQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE PFQGrades;")
mycursor.execute("CREATE TABLE PFQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO ProgrammingFundamentalsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"PF\",\"Whats an integer?\",\"A whole number\",\"A true or false value\",\"A single character\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a real or float\",\"A number with a decimal point\",\"A whole number\",\"Neither\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a boolean value?\",\"Data that is either a True or False value\",\"A decimal number\",\"Neither\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a string?\",\"A piece of text formed by characters\",\"A single character\",\"A whole number\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a sequence?\",\"A series of instructions that a program executes in order\",\"A unordered sequence\",\"Neither\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a local variable\",\"Only accessible within a specific part of a program\",\"Accessed within the whole program\",\"A user input\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats a global variable?\",\"Accessible anywhere in a program\",\"Within a specific part\",\"Neither\",\"PFQGrades\"),"
                 "(\"PF\",\"Which is an advantage of a subroutine?\",\"Make programs shorter\",\"Runs the code automatically\",\"Neither\",\"PFQGrades\"),"
                 "(\"PF\",\"Whats string concatenation?\",\"Joining two strings together\",\"Splitting up two strings\",\"Decreasing the characters in a string\",\"PFQGrades\");"
                )
db.commit()


mycursor.execute("DROP TABLE me_topics;")
mycursor.execute("CREATE TABLE me_topics ("
                 "me_topicID VARCHAR(50) PRIMARY KEY,"
                 "subjectID VARCHAR(10),"
                 "FOREIGN KEY(subjectID) REFERENCES subjects(subjectID));"
                 )

mycursor.execute("DELETE FROM me_topics;")
mycursor.execute("INSERT INTO me_topics (me_topicID , subjectID) VALUES"
                 "(\"OwnershipModelsOfMediaInstitutions\", \"ME\"),"
                 "(\"HowMediaProductsAreAdvertised\", \"ME\"),"
                 "(\"HowMeaningIsCreatedInMediaProducts\", \"ME\"),"
                 "(\"TargetAudienceOfMediaProducts\", \"ME\"),"
                 "(\"LegalAndEthicalIssues\", \"ME\");"

            )
db.commit()


###MEDIA TOPICS TABLE CREATION###


#mycursor.execute("DROP TABLE Media;")
mycursor.execute("CREATE TABLE Media ("
                 "me_topics VARCHAR(50),"
                 "teacherID int,"
                 "subjectID VARCHAR(10),"
                 "classID VARCHAR(10),"
                 "FOREIGN KEY(teacherID) REFERENCES teacher(teacherID),"
                 "FOREIGN KEY (subjectID) REFERENCES subjects (subjectID),"
                 "FOREIGN KEY(classID) REFERENCES classes(classID));"
                 )
mycursor.execute("INSERT INTO Media(subjectID , teacherID, classID, me_topics) VALUES"
                 "(\"ME\", 1, \"ME1\", \"OwnershipModelsOfMediaInstitutions\"),"
                 "(\"ME\", 1, \"ME1\", \"HowMediaProductsAreAdvertised\"),"
                 "(\"ME\", 1, \"ME1\", \"HowMeaningIsCreatedInMediaProducts\"),"
                 "(\"ME\", 1, \"ME1\", \"TargetAudienceOfMediaProducts\"),"
                 "(\"ME\", 1, \"ME1\", \"LegalAndEthicalIssues\");"
                 )
db.commit()

mycursor.execute("INSERT INTO Media(subjectID , teacherID, classID, me_topics) VALUES"
                 "(\"ME\", 4, \"ME2\", \"OwnershipModelsOfMediaInstitutions\"),"
                 "(\"ME\", 4, \"ME2\", \"HowMediaProductsAreAdvertised\"),"
                 "(\"ME\", 4, \"ME2\", \"HowMeaningIsCreatedInMediaProducts\"),"
                 "(\"ME\", 4, \"ME2\", \"TargetAudienceOfMediaProducts\"),"
                 "(\"ME\", 4, \"ME2\", \"LegalAndEthicalIssues\");"
                 )
db.commit()


mycursor.execute("DROP TABLE OwnershipModelsOfMediaInstitutions;")
mycursor.execute("CREATE TABLE OwnershipModelsOfMediaInstitutions ("
                 "me_topicID VARCHAR(50),"
                 "FOREIGN KEY(me_topicID) REFERENCES me_topics(me_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO OwnershipModelsOfMediaInstitutions (me_topicID , quizID) VALUES"
                 "(\"OwnershipModelsOfMediaInstitutions\" , \"OMMI\");"
                 )
db.commit()

mycursor.execute("DROP TABLE OwnershipModelsOfMediaInstitutionsQuiz;")
mycursor.execute("CREATE TABLE OwnershipModelsOfMediaInstitutionsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES OwnershipModelsOfMediaInstitutions(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES OWMIQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE OWMIQGrades;")
mycursor.execute("CREATE TABLE OWMIQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO OwnershipModelsOfMediaInstitutionsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"OMMI\",\"Whats a conglomerate structure?\",\"A parent compmany that owns smaller subsidaries\",\"A independent company\",\"A small company\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats an independent company?\",\"A company free from the control of a conglomerate\",\"A small company\",\"Neither\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats a joint venture?\",\"When a company works with another on a project that is mutually beneficial\",\"Competiton between two companies\",\"A company being sold to another\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats distribution?\",\"How a product reaches an audience\",\"A company losing market share\",\"Neither\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats cross media?\",\"A conglomerate that produces more than one type of media\",\"Two companies working together\",\"Neither\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats a specialist provider?\",\"Companies that produce and distribute products within a specific medium \",\"Produce more than one type of media\",\"A popular company\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats synergy?\",\"The increased efficiency and profit\",\"Decrease of efficiency and profits\",\"Neither\",\"OWMIQGrades\"),"
                 "(\"OMMI\",\"Whats a public service broadcaster?\",\"A company that delivers services beneficial to the public interest\",\"Provides only news\",\"Neither\",\"OWMIQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE HowMediaProductsAreAdvertised;")
mycursor.execute("CREATE TABLE HowMediaProductsAreAdvertised ("
                 "me_topicID VARCHAR(50),"
                 "FOREIGN KEY(me_topicID) REFERENCES me_topics(me_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO HowMediaProductsAreAdvertised (me_topicID , quizID) VALUES"
                 "(\"HowMediaProductsAreAdvertised\" , \"HMPA\");"
                 )
db.commit()

mycursor.execute("DROP TABLE HowMediaProductsAreAdvertisedQuiz;")
mycursor.execute("CREATE TABLE HowMediaProductsAreAdvertisedQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES HowMediaProductsAreAdvertised(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES HMPAQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE HMPAQGrades;")
mycursor.execute("CREATE TABLE HMPAQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO HowMediaProductsAreAdvertisedQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"HMPA\",\"Whats traditional advertising?\",\"Old fashioned methods of advertising eg Bus banners\",\"Digital advertising\",\"Neither\",\"HMPAQGrades\"),"
                 "(\"HMPA\",\"Whats above the line advertising?\",\"Where mass media is used to promote brands\",\"Whre one type of media is used to promote brands\",\"Neither\",\"HMPAQGrades\"),"
                 "(\"HMPA\",\"Whats below the line advertising?\",\"When a company works with another on a project that is mutually beneficial\",\"Competiton between two companies\",\"A company being sold to another\",\"HMPAQGrades\"),"
                 "(\"HMPA\",\"Whats a traditionanl advertising example? ?\",\"Bus banner\",\"Personalised ads on social media\",\"Website banners\",\"HMPAQGrades\");"
                 )
db.commit()

mycursor.execute("DROP TABLE HowMeaningIsCreatedInMediaProducts;")
mycursor.execute("CREATE TABLE HowMeaningIsCreatedInMediaProducts ("
                 "me_topicID VARCHAR(50),"
                 "FOREIGN KEY(me_topicID) REFERENCES me_topics(me_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO HowMeaningIsCreatedInMediaProducts (me_topicID , quizID) VALUES"
                 "(\"HowMeaningIsCreatedInMediaProducts\" , \"HMCMP\");"
                 )
db.commit()

mycursor.execute("DROP TABLE HowMeaningIsCreatedInMediaProductsQuiz;")
mycursor.execute("CREATE TABLE HowMeaningIsCreatedInMediaProductsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES HowMeaningIsCreatedInMediaProducts(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES HMCMPGrades(gradeID));"
                )

mycursor.execute("DROP TABLE HMCMPQGrades;")
mycursor.execute("CREATE TABLE HMCMPGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO HowMeaningIsCreatedInMediaProductsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"HMCMP\",\"Whats mise-en-scene?\",\"The setting of a scene\",\"A editing technique\",\"Neither\",\"HMCMPGrades\"),"
                 "(\"HMCMP\",\"Which of these is an example of a camera shot?\",\"Long shot\",\"Far away shot\",\"Distance shot\",\"HMCMPGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE TargetAudienceOfMediaProducts;")
mycursor.execute("CREATE TABLE TargetAudienceOfMediaProducts ("
                 "me_topicID VARCHAR(50),"
                 "FOREIGN KEY(me_topicID) REFERENCES me_topics(me_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO TargetAudienceOfMediaProducts (me_topicID , quizID) VALUES"
                 "(\"TargetAudienceOfMediaProducts\",\"TAMP\");"
                 )
db.commit()

mycursor.execute("DROP TABLE TargetAudienceOfMediaProductsQuiz;")
mycursor.execute("CREATE TABLE TargetAudienceOfMediaProductsQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES TargetAudienceOfMediaProducts(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES TAMPGrades(gradeID));"
                )

mycursor.execute("DROP TABLE TAMPQGrades;")
mycursor.execute("CREATE TABLE TAMPGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY)," 
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));"
                 )

mycursor.execute("INSERT INTO TargetAudienceOfMediaProductsQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"TAMP\",\"Whats another word for niche?\",\"Specific\",\"Creative\",\"Great\",\"TAMPGrades\"),"
                 "(\"TAMP\",\"What does demographic mean?\",\"The structure of a population\",\"How many people own a media product\",\"Neither\",\"TAMPGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE LegalAndEthicalIssues;")
mycursor.execute("CREATE TABLE LegalAndEthicalIssues ("
                 "me_topicID VARCHAR(50),"
                 "FOREIGN KEY(me_topicID) REFERENCES me_topics(me_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO LegalAndEthicalIssues (me_topicID , quizID) VALUES"
                 "(\"LegalAndEthicalIssues\" , \"LEI\");"
                 )
db.commit()

mycursor.execute("DROP TABLE LegalAndEthicalIssuesQuiz;")
mycursor.execute("CREATE TABLE LegalAndEthicalIssuesQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES LegalAndEthicalIssues(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES LEIQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE LEIQGrades;")
mycursor.execute("CREATE TABLE LEIQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO LegalAndEthicalIssuesQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"LEI\",\"Whats does PEGI do?\",\"Regulate video games\",\"Regulate films\",\"Regulate radio\",\"LEIQGrades\"),"
                 "(\"LEI\",\"What does BBFC?\",\"Regulate films\",\"Regulate video games\",\"Regulate radio\",\"LEIQGrades\");"
                )
db.commit()

###ECONOMICS TOPICS TABLE CREATION###

mycursor.execute("DROP TABLE ec_topics;")
mycursor.execute("CREATE TABLE ec_topics ("
                 "ec_topicID VARCHAR(50) PRIMARY KEY,"
                 "subjectID VARCHAR(10),"
                 "FOREIGN KEY(subjectID) REFERENCES subjects(subjectID));"
                 )

mycursor.execute("DELETE FROM ec_topics;")
mycursor.execute("INSERT INTO ec_topics (ec_topicID , subjectID) VALUES"
                 "(\"EconomicsMethodologyAndTheEconomicProblem\", \"EC\"),"
                 "(\"MarketStructures\", \"EC\"),"
                 "(\"EconomicDecisionMaking\", \"EC\"),"
                 "(\"DistributionOfIncomeAndWealth\", \"EC\"),"
                 "(\"GovernmentPolicies\", \"EC\");"
                 )
db.commit()

mycursor.execute("DROP TABLE Economics;")
mycursor.execute("CREATE TABLE Economics ("
                 "subjectID VARCHAR(10),"
                 "teacherID int,"
                 "classID VARCHAR(10),"
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(subjectID) REFERENCES subjects(subjectID),"
                 "FOREIGN KEY(teacherID) REFERENCES teacher(teacherID),"
                 "FOREIGN KEY(classID) REFERENCES classes(classID),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID));"
                 )

mycursor.execute("INSERT INTO Economics(subjectID , teacherID, classID, ec_topics) VALUES"
                 "(\"EC\", 2, \"EC1\", \"EconomicsMethodologyAndTheEconomicProblem\"),"
                 "(\"EC\", 2, \"EC1\", \"MarketStructures\"),"
                 "(\"EC\", 2, \"EC1\", \"EconomicDecisionMaking\"),"
                 "(\"EC\", 2, \"EC1\", \"DistributionOfIncomeAndWealth\"),"
                 "(\"EC\", 2, \"EC1\", \"GovernmentPolicies\");"
                 )
db.commit()

mycursor.execute("INSERT INTO Economics(subjectID , teacherID, classID, ec_topics) VALUES"
                 "(\"EC\", 5, \"EC2\", \"EconomicsMethodologyAndTheEconomicProblem\"),"
                 "(\"EC\", 5, \"EC2\", \"MarketStructures\"),"
                 "(\"EC\", 5, \"EC2\", \"EconomicDecisionMaking\"),"
                 "(\"EC\", 5, \"EC2\", \"DistributionOfIncomeAndWealth\"),"
                 "(\"EC\", 5, \"EC2\", \"GovernmentPolicies\");"
                 )
db.commit()

mycursor.execute("DROP TABLE EconomicsMethodologyAndTheEconomicProblem;")
mycursor.execute("CREATE TABLE EconomicsMethodologyAndTheEconomicProblem ("
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO EconomicsMethodologyAndTheEconomicProblem (ec_topicID , quizID) VALUES"
                 "(\"EconomicsMethodologyAndTheEconomicProblem\" , \"EMEP\");"
                 )
db.commit()

mycursor.execute("DROP TABLE EconomicsMethodologyAndTheEconomicProblemQuiz;")
mycursor.execute("CREATE TABLE EconomicsMethodologyAndTheEconomicProblemQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES EconomicsMethodologyAndTheEconomicProblem(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES EMEPGrades(gradeID));"
                )

mycursor.execute("DROP TABLE EMEPQGrades;")
mycursor.execute("CREATE TABLE EMEPGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO EconomicsMethodologyAndTheEconomicProblemQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"EMEP\",\"Whats does consumer mean?\",\"An individual who buys and uses a product\",\"An individual who sells products\",\"An individual who wants to own a product\",\"EMEPGrades\"),"
                 "(\"EMEP\",\"Whats a need?\",\"Something essential for survival\",\"Something which is desired\",\"Neither\",\"EMEPGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE MarketStructures;")
mycursor.execute("CREATE TABLE MarketStructures ("
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO MarketStructures (ec_topicID , quizID) VALUES"
                 "(\"MarketStructures\" , \"MS\");"
                 )
db.commit()

mycursor.execute("DROP TABLE MarketStructuresQuiz;")
mycursor.execute("CREATE TABLE MarketStructuresQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES MarketStructures(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES MSQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE MSQGrades;")
mycursor.execute("CREATE TABLE MSQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO MarketStructuresQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"MS\",\"When does allocative efficieny occur?\",\"When P=MC\",\"When MC=AC\",\"MR=MC\",\"MSQGrades\"),"
                 "(\"MS\",\"When does productive efficiency occur\",\"When MC=AC\",\"When P=MC\",\"MR=MC\",\"MSQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE EconomicDecisionMaking;")
mycursor.execute("CREATE TABLE EconomicDecisionMaking ("
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO EconomicDecisionMaking (ec_topicID , quizID) VALUES"
                 "(\"EconomicDecisionMaking\" , \"EDM\");"
                 )
db.commit()

mycursor.execute("DROP TABLE EconomicDecisionMakingQuiz;")
mycursor.execute("CREATE TABLE EconomicDecisionMakingQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES EconomicDecisionMaking(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES EDMQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE EDMQGrades;")
mycursor.execute("CREATE TABLE EDMQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO EconomicDecisionMakingQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"EDM\",\"What does opportunity cost mean?\",\"The value of the next best alternative when a decision is made\",\"When a firm loses profits\",\"When there is a chance to reinvest\",\"EDMQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE DistributionOfIncomeAndWealth;")
mycursor.execute("CREATE TABLE DistributionOfIncomeAndWealth ("
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO DistributionOfIncomeAndWealth (ec_topicID , quizID) VALUES"
                 "(\"DistributionOfIncomeAndWealth\" , \"DOIW\");"
                 )
db.commit()

mycursor.execute("DROP TABLE DistributionOfIncomeAndWealthQuiz;")
mycursor.execute("CREATE TABLE DistributionOfIncomeAndWealthQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES DistributionOfIncomeAndWealth(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES DOIWQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE DOIWQGrades;")
mycursor.execute("CREATE TABLE DOIWQGrades ("
                 "gradeID VARCHAR(20) PRIMARY KEY)," 
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO DistributionOfIncomeAndWealthQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"DOIW\",\"What does income mean?\",\"A flow of money going into factors of production\",\"Profits\",\"How much a firm pays in tax\",\"DOIWQGrades\");"
                )
db.commit()

mycursor.execute("DROP TABLE GovernmentPolicies;")
mycursor.execute("CREATE TABLE GovernmentPolicies ("
                 "ec_topicID VARCHAR(50),"
                 "FOREIGN KEY(ec_topicID) REFERENCES ec_topics(ec_topicID),"
                 "quizID VARCHAR(20) PRIMARY KEY));"
                 )
mycursor.execute("INSERT INTO GovernmentPolicies (ec_topicID , quizID) VALUES"
                 "(\"GovernmentPolicies\" , \"GP\");"
                 )
db.commit()

mycursor.execute("DROP TABLE GovernmentPoliciesQuiz;")
mycursor.execute("CREATE TABLE GovernmentPoliciesQuiz ("
                 "questions VARCHAR(200),"
                 "correct_answer VARCHAR(200),"
                 "wrong_answer1 VARCHAR(200),"
                 "wrong_answer2 VARCHAR(200),"
                 "quizID VARCHAR(20),"
                 "gradeID VARCHAR(20),"
                 "FOREIGN KEY(quizID) REFERENCES GovernmentPolicies(quizID),"
                 "FOREIGN KEY(gradeID) REFERENCES GPQGrades(gradeID));"
                )

mycursor.execute("DROP TABLE GPQGrades;")
mycursor.execute("CREATE TABLE GPQGrades ("
                 "quizID VARCHAR(20) PRIMARY KEY),"
                 "studentID int,"
                 "FOREIGN KEY(studentID) REFERENCES student(studentID),"
                 "grade VARCHAR(10));")

mycursor.execute("INSERT INTO GovernmentPoliciesQuiz (quizID,questions,correct_answer,wrong_answer1,wrong_answer2,gradeID) VALUES"
                 "(\"GP\",\"Whats an example of a government policy in micro?\",\"Indirect tax\",\"Ensuring that all firms are profitable\",\"Neither\",\"GPQGrades\");"
                )
                 
db.commit()

"""
###TESTING THE DB AND VALUES###

"""
mycursor.execute("SELECT * FROM student;")
students = mycursor.fetchall()
print("Students: ", students)

mycursor.execute("SELECT * FROM teacher;")
teachers = mycursor.fetchall()
print("Teachers: ", teachers)

mycursor.execute("SELECT * FROM classes;")
classes = mycursor.fetchall()
print("Classes: ", classes)

mycursor.execute("SELECT * FROM ComputerNetworksQuiz;")
ComputerNetworksQuiz = mycursor.fetchall()
print("Computer Networks Quiz: ", ComputerNetworksQuiz)

mycursor.execute("SELECT * FROM ComputerNetworks;")
ComputerNetworks = mycursor.fetchall()
print("Computer Networks: ", ComputerNetworks)

mycursor.execute("SELECT * FROM ComputerScience;")
ComputerScience = mycursor.fetchall()
print("Computer Science: ", ComputerScience)

mycursor.execute("SELECT * FROM ComputerSystems;")
ComputerSystems = mycursor.fetchall()
print("Computer Systems: ", ComputerSystems)

mycursor.execute("SELECT * FROM ComputerSystemsQuiz;")
ComputerSystemsQuiz = mycursor.fetchall()
print("Computer Systems Quiz: ", ComputerSystemsQuiz)

mycursor.execute("SELECT * FROM CS1;")
CS1 = mycursor.fetchall()
print("CS1: ", CS1)

mycursor.execute("SELECT * FROM CS2;")
CS2 = mycursor.fetchall()
print("CS2: ", CS2)

mycursor.execute("SELECT * FROM cs_topics;")
cs_topics = mycursor.fetchall()
print("cs_topics: ", cs_topics)

mycursor.execute("SELECT * FROM DataAndInformation;")
DataAndInformation = mycursor.fetchall()
print("Data And Information: ", DataAndInformation)

mycursor.execute("SELECT * FROM DataAndInformationQuiz;")
DataAndInformationQuiz = mycursor.fetchall()
print("Data And Information Quiz: ", DataAndInformationQuiz)

mycursor.execute("SELECT * FROM DataStructuresAndAlgorithms;")
DataStructuresAndAlgorithms = mycursor.fetchall()
print("DataStructuresAndAlgorithms: ", DataStructuresAndAlgorithms)

mycursor.execute("SELECT * FROM DataStructuresAndAlgorithmsQuiz;")
DataStructuresAndAlgorithmsQuiz = mycursor.fetchall()
print("DataStructuresAndAlgorithmsQuiz: ", DataStructuresAndAlgorithmsQuiz)

mycursor.execute("SELECT * FROM ProgrammingFundamentals;")
ProgrammingFundamentals = mycursor.fetchall()
print("ProgrammingFundamentals: ", ProgrammingFundamentals)

mycursor.execute("SELECT * FROM ProgrammingFundamentalsQuiz;")
ProgrammingFundamentalsQuiz = mycursor.fetchall()
print("ProgrammingFundamentalsQuiz: ", ProgrammingFundamentalsQuiz)

mycursor.execute("SELECT * FROM EC1;")
EC1 = mycursor.fetchall()
print("EC1: ", EC1)

mycursor.execute("SELECT * FROM EC2;")
EC2 = mycursor.fetchall()
print("EC2: ", EC2)

mycursor.execute("SELECT * FROM ec_topics;")
ec_topics = mycursor.fetchall()
print("ec_topics: ", ec_topics)

mycursor.execute("SELECT * FROM me_topics;")
me_topics = mycursor.fetchall()
print("me_topics: ", me_topics)

mycursor.execute("SELECT * FROM Media;")
Media = mycursor.fetchall()
print("Media: ", Media)


mycursor.execute("SELECT me_topicID FROM me_topics;")
topics = mycursor.fetchall()
print(topics)

mycursor.execute("SELECT ec_topicID FROM ec_topics;")
topics = mycursor.fetchall()
print(topics)

#TESTING/DEBUGGING:

username = "Zamir1"
score = 2
topic = "ComputerNetworks"

# 0 - get id of student using select student id from student where username=self.username
getStudentID = "SELECT studentID FROM student WHERE username = '" + str(username) + "';"
mycursor.execute(getStudentID)
studentID = mycursor.fetchall()[0][0]

print(studentID)

# 1: select quiz grades id from quiz table
topicQuiz = topic + "Quiz"
getQuizGradeID = "SELECT gradeID FROM " + str(topicQuiz) + ";"
mycursor.execute(getQuizGradeID)
quizGradeID = mycursor.fetchall()[0][0]

print(quizGradeID)

# 2: insert into quiz grade id score, userid
insertScore = "INSERT INTO " + str(quizGradeID) + " (gradeID, studentID, grade) VALUES (\"" + str(
    quizGradeID) + "\", \"" + str(studentID) + "\", \"" + str(score) + "\");"
mycursor.execute(insertScore)

print("done")

db.commit()

mycursor.execute("SELECT * FROM CNQGrades;")
print(mycursor.fetchall())

username = 'Alexander1'
mycursor.execute(getClass)
print(getClass)
Class = mycursor.fetchall()
Class = str(Class[0])
Class = Class.strip("()',")
print(Class)

username = "Alexander1"
classID = "CS1"

getTeacherID = "SELECT teacherID FROM teacher WHERE username = '" + username + "';"
mycursor.execute(getTeacherID)
teacherID = mycursor.fetchall()[0][0]
print("teacher id: " + str(teacherID))

getClass = "SELECT classID, teacherID FROM classes WHERE classes.teacherID ='" + str(teacherID) + "' AND classes.classID = '" + str(classID) + "';"
mycursor.execute(getClass)
test = mycursor.fetchall()
print("my test: " + str(test))

checkTeacherInClass = False

if test[0][0] == 'False':
    checkTeacherInClass = False
elif test[0][0] == classID and test[0][1] == teacherID:
    checkTeacherInClass = True

print("check teacher in class: " + str(checkTeacherInClass))


topic = "ComputerNetworks"
quiz = topic + "Quiz"
questionCount = "SELECT COUNT(*) FROM " + quiz + ";"
mycursor.execute(questionCount)
questionAmount = mycursor.fetchall()[0][0]
print("there are " + str(questionAmount) + " questions in the " + quiz)


quizName= "ComputerNetworksQuiz"
qid = "CN"
q = "whats a router"
a = "blah blah"
wa1 = "adfsdf"
wa2 = "zzzzz"
gradeID = "CNQGrades"
deleteQuestion = "DELETE FROM " + str(quizName) + " (quizID, questions, correct_answer, wrong_answer1, wrong_answer2, gradeID) VALUES (\"" + str(qid) + "\", \"" + str(q) + "\", \"" + str(a) + "\", \"" + str(wa1) + "\", \"" + str(wa2) + "\", \"" + str(gradeID) + "\");"
mycursor.execute(deleteQuestion)

print("done")


mycursor.execute("SELECT * FROM ComputerNetworksQuiz;")
q = mycursor.fetchall()
print(q)



mycursor.execute("SELECT * FROM MarketStructuresQuiz;")
print(str(mycursor.fetchall()))

n = "Tim"
a = 17
c = "EC1"
s = "Economics"
sp = "Tim123"
u = "Tim1"
g = "Male"

insertStudent = "INSERT INTO student (name,age,class,subjects,studentpassword,username,gender) VALUES (\"" + str(
    n) + "\", \"" + str(a) + "\", \"" + str(c) + "\", \"" + str(s) + "\", \"" + str(sp) + "\", \"" + str(u) + "\",\"" + str(g) + "\");"
mycursor.execute(insertStudent)
db.commit()


mycursor.execute("SELECT * FROM student;")
stu = mycursor.fetchall()
print(stu)
"""

mycursor.close()

