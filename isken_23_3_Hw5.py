data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
codes = []
designations = []
operators = {}
a = 0
for datat in data:
    a = a + 1
    if datat[0] =='0':
        codes.append(datat)
    else:
        designations.append(datat)
a = (a // 2) - 1
while a >= 0:
    operators[designations[a]] = [codes[a]]
    a = a - 1
del operators["Katel"]
del operators['Fonex']
for i in operators:
 if i == 'O!':
  operators[i].append('0700')
  operators[i].append('0500')
  print(f'{i} - {set(operators[i])}')
 elif i == 'Beeline':
  operators[i].append('0222')
  operators[i].append('0777')
  print(f'{i} - {set(operators[i])}')
 else:
  operators[i].append('0555')
  operators[i].append('0999')
  print(f'{i} - {set(operators[i])}')

