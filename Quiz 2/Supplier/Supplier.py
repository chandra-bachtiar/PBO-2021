from db import DBConnection as mydb

class Supplier:
    def __init__(self):
        self.__idsupplier = None
        self.__kodesupplier = None
        self.__namasupplier = None
        self.__cp = None
        self.__telp = None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "kodeSupplier:" + self.__kodesupplier + "\n" + "namaSupplier:" + self.__namasupplir + "\n" + "kontakPerson" + self.__cp + "\n" + "Telpon:" + self.__telp
        else:
            return self.__info

    @property
    def id(self):
        return self.__idsupplier
    
    @property
    def kodesupplier(self):
        return self.__kodesupplier

    @kodesupplier.setter
    def kodesupplier(self, value):
        self.__kodesupplier = value
    
    @property
    def namasupplier(self):
        return self.__namasupplier

    @namasupplier.setter
    def namasupplier(self, value):
        self.__namasupplier = value
    
    @property
    def cp(self):
        return self.__cp

    @cp.setter
    def cp(self, value):
        self.__cp = value
    
    @property
    def telp(self):
        return self.__telp

    @telp.setter
    def telp(self, value):
        self.__telp = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kodesupplier,self.__namasupplier,self.__cp,self.__telp)
        sql="INSERT INTO supplier (kode_supplier,nama_supplier,kontak_person,telpon) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kodesupplier,self.__namasupplier,self.__cp,self.__telp, id)
        sql="UPDATE supplier SET kode_supplier=%s, nama_supplier=%s, kontak_person=%s, telpon=%s WHERE idsupplier=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKodeSupplier(self, kodesupplier):
        self.conn = mydb()
        val = (self.__kodesupplier,self.__namasupplier,self.__cp,self.__telp, kodesupplier)
        sql="UPDATE supplier SET kode_supplier=%s, nama_supplier=%s, kontak_person=%s, telpon=%s WHERE kode_supplier=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM supplier WHERE idsupplier='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByKodeSupplier(self, kodesupplier):
        self.conn = mydb()
        sql="DELETE FROM supplier WHERE kode_supplier='" + str(kodesupplier) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM supplier WHERE idsupplier='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodesupplier = self.result[1]                   
        self.__namasupplier = self.result[2]                   
        self.__cp = str(self.result[3])                   
        self.__telp = self.result[4]                   
        self.conn.disconnect
        return self.result
        
    def getByKodeSupplier(self, kodesupplier):
        a=str(kodesupplier)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM supplier WHERE kode_supplier='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodesupplier = self.result[1]                   
            self.__namasupplier = self.result[2]                   
            self.__cp = str(self.result[3])                   
            self.__telp = self.result[4]                   
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodesupplier = ''                  
            self.__namasupplier = ''                  
            self.__cp = ''                  
            self.__telp = ''                  
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM supplier"
        self.result = self.conn.findAll(sql)
        return self.result