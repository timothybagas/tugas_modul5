class userService(object):    
    def __init__(self, email, password):#pembuatan constructor
        self.email = email
        self.password = password
        self.data = {
            "syahrulkelompok45@gmail.com" : {
                "email"     : "syahrulkelompok45@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },
            "timothykelompok45@gmail.com" : {
                "email"     : "timothykelompok45@gmail.com",
                "password"  : "12345",
                "role"      : "user"
            }
        }
        self.history = {
            "syahrulkelompok45@gmail.com" : {
                "peminjaman_buku" : {"Fisika Dasar", "Dasar Komputer dan Pemrograman"},
                "tanggal_pinjam"  : "26-04-2020"
            },
            "timothykelompok45@gmail.com" : {
                "peminjaman_buku" : {"Kalkulus", "Dasar Komputer dan Pemrograman", "Kosep Jaringan Komputer"},
                "tanggal_pinjam"  : "26-04-2020"
            }
        }
    def login(self):#berfungsi sebagai pembuatan method login
        get_data = self.checkCredentials()#pembuatan variable baru
        get_history1 = self.check()
        get_history2 = self.check1()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'],"\n")
            print(get_data['email'],"meminjam buku :")
            for r in get_history1:
                print(r)
            print("Tanggal peminjaman :", get_history2)
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self): #method untuk mengecek data inputan user
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    def check(self):
        for value in self.history:
            if value == self.email:
                get_history_user = self.history[value]
                return get_history_user['peminjaman_buku']
   
    def check1(self):
        for value in self.history:
            if value == self.email:
                get_history_user = self.history[value]
                return get_history_user['tanggal_pinjam'] 

