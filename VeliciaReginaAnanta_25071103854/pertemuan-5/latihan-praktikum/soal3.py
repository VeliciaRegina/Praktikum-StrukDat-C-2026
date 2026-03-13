ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

coding = ukm_coding - ukm_robotik
print(coding)

set2 = ukm_coding | ukm_robotik
print(set2)

if "Andi" in ukm_robotik:
   print('True')