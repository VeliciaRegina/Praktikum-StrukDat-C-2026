data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for x in range(len(data_aktivitas)):
   if data_aktivitas[x][1] > 80:
      print (f'{data_aktivitas[x][0]} mendapat Gold')

   elif 50 < data_aktivitas[x][1] <= 80:
      print (f'{data_aktivitas[x][0]} mendapat Silver')

   else:
      print (f'{data_aktivitas[x][0]} mendapat Bronze')
