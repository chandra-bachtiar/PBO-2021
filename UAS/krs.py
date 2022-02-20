from database import DBConnection as mydb
class Krs:
    def __init__(self):
        self.__idkrs= None
        self.__nomor_bukti= None
        self.__nim= None
        self.__nidn= None
        self.__tanggal= None
        self.__tahun_akademik= None
        self.__tipe_semester= None
        self.__kode_prodi= None
        self.__kodemk_1= None
        self.__kodemk_2= None
        self.__kodemk_3= None
        self.__kodemk_4= None
        self.__kodemk_5= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idkrs(self):
        return self.__idkrs
    
    @property
    def nomor_bukti(self):
        return self.__nomor_bukti

    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value
    
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value
    
    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    
    @property
    def nidn(self):
        return self.__nidn

    @nidn.setter
    def nidn(self, value):
        self.__nidn = value
    
    @property
    def tahun_akademik(self):
        return self.__tahun_akademik

    @tahun_akademik.setter
    def tahun_akademik(self, value):
        self.__tahun_akademik = value

    @property
    def tipe_semester(self):
        return self.__tipe_semester

    @tipe_semester.setter
    def tipe_semester(self, value):
        self.__tipe_semester = value
    
    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value
    
    @property
    def kodemk_1(self):
        return self.__kodemk_1

    @kodemk_1.setter
    def kodemk_1(self, value):
        self.__kodemk_1 = value
    
    @property
    def kodemk_2(self):
        return self.__kodemk_2

    @kodemk_2.setter
    def kodemk_2(self, value):
        self.__kodemk_2 = value

    
    @property
    def kodemk_3(self):
        return self.__kodemk_3

    @kodemk_3.setter
    def kodemk_3(self, value):
        self.__kodemk_3 = value

    @property
    def kodemk_4(self):
        return self.__kodemk_4

    @kodemk_4.setter
    def kodemk_4(self, value):
        self.__kodemk_4 = value

    @property
    def kodemk_5(self):
        return self.__kodemk_5

    @kodemk_5.setter
    def kodemk_5(self, value):
        self.__kodemk_5 = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__nim,self.__nidn,self.__tanggal,self.__tipe_semester,self.__tahun_akademik,self.__kode_prodi,self.__kodemk_1,self.__kodemk_2,self.__kodemk_3,self.__kodemk_4,self.__kodemk_5)
        sql="INSERT INTO krs (nomor_bukti,nim,nidn,tanggal,tipe_semester,tahun_akademik,kode_prodi,kodemk1,kodemk2,kodemk3,kodemk4,kodemk5) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__nim,self.__nidn,self.__tipe_semester,self.__tahun_akademik,self.__tanggal,self.__kode_prodi,self.__kodemk_1,self.__kodemk_2,self.__kodemk_3,self.__kodemk_4,self.__kodemk_5,id)
        sql="UPDATE krs SET nomor_bukti=%s, nim=%s, nidn=%s,tipe_semester=%s,tahun_akademik = %s, tanggal=%s, kode_prodi=%s, kodemk1=%s, kodemk2=%s, kodemk3=%s,kodemk4=%s,kodemk5=%s WHERE idsks=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__tanggal,self.__nim,self.__nidn,self.__tahun_akademik,self.__tipe_semester,self.__kodemk_1,self.__kodemk_2,self.__kodemk_3,self.__kodemk_4,self.__kodemk_5,self.__kode_prodi, nomor_bukti)
        sql="UPDATE krs SET nomor_bukti=%s,tanggal=%s, nim=%s, nidn=%s,tahun_akademik=%s, tipe_semester=%s, kodemk1=%s, kodemk2=%s, kodemk3=%s,kodemk4=%s,kodemk5=%s,kode_prodi=%s WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM krs WHERE idkrs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        sql="DELETE FROM krs WHERE nomor_bukti='" + str(nomor_bukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM krs WHERE idkrs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_bukti = self.result[1]
        self.__tanggal = str(self.result[2])
        self.__nim = self.result[3]
        self.__nidn = self.result[4]
        self.__tahun_akademik = self.result[5]
        self.__tipe_semester = self.result[6]
        self.__kodemk_1 = self.result[7]
        self.__kodemk_2 = self.result[8]
        self.__kodemk_3 = self.result[9]
        self.__kodemk_4 = self.result[10]
        self.__kodemk_5 = self.result[11]
        self.__kode_prodi = self.result[12]                   
        self.conn.disconnect
        return self.result
        
    def getByNOMOR_BUKTI(self, nomor_bukti):
        a=str(nomor_bukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM krs WHERE nomor_bukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_bukti = self.result[1]
            self.__tanggal = str(self.result[2])
            self.__nim = self.result[3]
            self.__nidn = self.result[4]
            self.__tahun_akademik = self.result[5]
            self.__tipe_semester = self.result[6]
            self.__kodemk_1 = self.result[7]
            self.__kodemk_2 = self.result[8]
            self.__kodemk_3 = self.result[9]
            self.__kodemk_4 = self.result[10]
            self.__kodemk_5 = self.result[11]
            self.__kode_prodi = self.result[12]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_bukti = ''
            self.__tanggal = ''
            self.__nim = ''
            self.__nidn = ''
            self.__tahun_akademik = ''
            self.__tipe_semester = ''
            self.__kodemk_1 = ''
            self.__kodemk_2 = ''
            self.__kodemk_3 = ''
            self.__kodemk_4 = ''
            self.__kodemk_5 = ''
            self.__kode_prodi = ''               
            self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM krs"
        self.result = self.conn.findAll(sql)
        return self.result