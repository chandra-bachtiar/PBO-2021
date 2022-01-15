from db import DBConnection as mydb

class Mahasiswa:
    def __init__(self):
        self.__idmhs = None
        self.__nim = None
        self.__nama = None
        self.__jk = None
        self.__prodi = None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "Nim:" + self.__nim + "\n" + "Nama:" + self.__nama + "\n" + "Kelamin:" + self.__jk + "\n" + "Kode Prodi:" + self.__prodi
        else:
            return self.__info

    @property
    def id(self):
        return self.__idmhs
    
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value
    
    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__jk,self.__prodi)
        print(val)
        sql="INSERT INTO MAHASISWA(NIM,NAMA,JK,KODE_PRODI) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__jk,self.__prodi, id)
        sql="UPDATE MAHASISWA SET NIM=%s, NAMA=%s, JK=%s, KODE_PRODI=%s WHERE IDMHS=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__jk,self.__prodi, nim)
        sql="UPDATE MAHASISWA SET NIM=%s, NAMA=%s, JK=%s, KODE_PRODI=%s WHERE NIM=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM MAHASISWA WHERE IDMHS='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql="DELETE FROM MAHASISWA WHERE NIM='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM MAHASISWA WHERE IDMHS='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]                   
        self.__nama = self.result[2]                   
        self.__jk = str(self.result[3])                   
        self.__prodi = self.result[4]                   
        self.conn.disconnect
        return self.result
        
    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM MAHASISWA WHERE NIM='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]                   
            self.__nama = self.result[2]                   
            self.__jk = str(self.result[3])                   
            self.__prodi = self.result[4]                   
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''                  
            self.__nama = ''                  
            self.__jk = ''                  
            self.__prodi = ''                  
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM MAHASISWA"
        self.result = self.conn.findAll(sql)
        return self.result