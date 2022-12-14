from django.db import models

class mhs(models.Model):
    Nama = models.CharField(max_length=30)
    NPM = models.CharField(max_length=20)
    Prodi = models.CharField(max_length=30)
    Tanggal_lahir = models.DateField()
    Alamat = models.TextField()
    Kode_pos = models.CharField(max_length=5)

    def __str__(self):
        return "{}. {}".format(self.id,self.Nama)

class skripsi(models.Model):
    Nama = models.ForeignKey(mhs, on_delete=models.CASCADE)
    NPM = models.CharField(max_length=20)
    Judul_skripsi = models.CharField(max_length=20)
    Abstrak = models.CharField(max_length=500)
    Pembimbing = models.CharField(max_length=30)
    Kode_skripsi = models.IntegerField(null=True)

    def __str__(self):
        return "{}. {}".format(self.id,self.Nama)
class th(models.Model):
    NAMA = models.ForeignKey(mhs, on_delete=models.CASCADE)
    Kode_matakuliah = models.CharField(max_length=7)
    Nilai_angka = models.FloatField()
    Nilai_huruf = models.CharField(max_length=2)

    def __str__(self):
        return "{}. {}".format(self.id,self.NAMA)