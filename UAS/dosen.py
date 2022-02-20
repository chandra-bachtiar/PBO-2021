from database import DBConnection as mydb

class Dosen:

    def __init__(self):
        self.__id=None
        self.__nip=None
        self.__nama=None
        self.__alamat=None
        self.__email=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "NIP:" + self.__nip + "\n" + "Nama:" + self.__nama + "\n" + "Alamat" + self.__alamat + "\n" + "Email :" + self.__email
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__alamat, self.__email)
        sql="INSERT INTO dosen (nip, nama, alamat, email) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__alamat, self.__email, id)
        sql="UPDATE dosen SET nip = %s, nama = %s, alamat=%s, email=%s WHERE iddosen=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__alamat, self.__email,nip)
        sql="UPDATE dosen SET nama = %s, alamat=%s, email=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE iddosen='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nip):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE iddosen='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__email = self.result[3]
        self.__alamat = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__email = self.result[3]
            self.__alamat = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__alamat = ''
            self.__email = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dosen"
        self.result = self.conn.findAll(sql)
        return self.result
