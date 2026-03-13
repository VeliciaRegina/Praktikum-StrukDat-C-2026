from kurs import kursUang

def IDR_ke_kurs_asing(nominal, kursHasil):
   return nominal/kursUang[kursHasil]

def kurs_asing_ke_IDR(nominal, kursAsal):
   return nominal* kursUang[kursAsal]

def asing_ke_asing(nominal, kursAsal, kursHasil):
   return nominal * (kursUang[kursAsal] / kursUang[kursHasil])