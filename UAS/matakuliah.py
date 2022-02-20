from database import DBConnection as mydb

class Matakuliah:

    def __init__(self):
        self.__id=None
        self.__kodemk=None
        self.__namamk=None
        self.__sks=None
        self.__kode_prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "kode:" + self.__kodemk + "\n" + "Nama:" + self.__namamk + "\n" + "SKS" + self.__sks + "\n" + "prodi :" + self.__kode_prodi
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamk(self):
        return self.__namamk

    @namamk.setter
    def namamk(self, value):
        self.__namamk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodemk, self.__namamk, self.__sks, self.__kode_prodi)
        sql="INSERT INTO matakuliah (kodemk, namamk, sks, kode_prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kodemk, self.__namamk, self.__sks, self.__kode_prodi, id)
        sql="UPDATE matakuliah SET kodemk = %s, namamk = %s, sks=%s, kode_prodi=%s WHERE idmk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODE(self, kode):
        self.conn = mydb()
        val = (self.__namamk, self.__sks, self.__kode_prodi,kode)
        sql="UPDATE matakuliah SET namamk = %s, sks=%s, kode_prodi=%s WHERE kodemk=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM matakuliah WHERE idmk='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODE(self, kode):
        self.conn = mydb()
        sql="DELETE FROM matakuliah WHERE kodemk='" + str(kode) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM matakuliah WHERE idmk='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodemk = self.result[1]
        self.__namamk = self.result[2]
        self.__sks = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByKODE(self, kode):
        a=str(kode)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM matakuliah WHERE kodemk='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodemk = self.result[1]
            self.__namamk = self.result[2]
            self.__sks = self.result[3]
            self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodemk = ''
            self.__namamk = ''
            self.__sks = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result
