from db import DBConnection as mydb

class Barang:
    def __init__(self):
        self.__idbarang = None
        self.__kodebarang = None
        self.__namabarang = None
        self.__merk = None
        self.__harga = None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "kodeBarang:" + self.__kodebarang + "\n" + "namaBarang:" + self.__namabarang + "\n" + "merk" + self.__merk + "\n" + "harga:" + self.__harga
        else:
            return self.__info

    @property
    def id(self):
        return self.__idbarang
    
    @property
    def kodebarang(self):
        return self.__kodebarang

    @kodebarang.setter
    def kodebarang(self, value):
        self.__kodebarang = value
    
    @property
    def namabarang(self):
        return self.__namabarang

    @namabarang.setter
    def namabarang(self, value):
        self.__namabarang = value
    
    @property
    def merk(self):
        return self.__merk

    @merk.setter
    def merk(self, value):
        self.__merk = value
    
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kodebarang,self.__namabarang,self.__merk,self.__harga)
        sql="INSERT INTO barang (kode_barang,nama_barang,merk,harga) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kodebarang,self.__namabarang,self.__merk,self.__harga, id)
        sql="UPDATE barang SET kode_barang=%s, nama_barang=%s, merk=%s, harga=%s WHERE idbarang=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKodeBarang(self, kodebarang):
        self.conn = mydb()
        val = (self.__kodebarang,self.__namabarang,self.__merk,self.__harga, kodebarang)
        sql="UPDATE barang SET kode_barang=%s, nama_barang=%s, merk=%s, harga=%s WHERE kode_barang=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM barang WHERE idbarang='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByKodeBarang(self, kodebarang):
        self.conn = mydb()
        sql="DELETE FROM barang WHERE kode_barang='" + str(kodebarang) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM barang WHERE idbarang='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kodebarang = self.result[1]                   
        self.__namabarang = self.result[2]                   
        self.__merk = str(self.result[3])                   
        self.__harga = self.result[4]                   
        self.conn.disconnect
        return self.result
        
    def getByKodeBarang(self, kodebarang):
        a=str(kodebarang)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM barang WHERE kode_barang='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kodebarang = self.result[1]                   
            self.__namabarang = self.result[2]                   
            self.__merk = str(self.result[3])                   
            self.__harga = self.result[4]                   
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodebarang = ''                  
            self.__namabarang = ''                  
            self.__merk = ''                  
            self.__harga = ''                  
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM barang"
        self.result = self.conn.findAll(sql)
        return self.result