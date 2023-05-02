# without importing anything, function to add X amount of days to a date to find the new date
birthdate = input("Enter what date you want to check  ex(4/01/2003)  : ")
days = int(input("Number of days to add: "))

def how_many_days_after(birthdate,days):
  months = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
  
  counter = 0
  string1 =  str(days) + ' days from ' + birthdate + ' will be: '
  x = birthdate.split('/')
  birth_month = int(x[0])
  birth_day = int(x[1])
  birth_year = int(x[2])
  
  difference = months[str(birth_month)] - birth_day
  if days <= difference:
    birth_day += days
    birthdate = str(birth_month) + '/' + str(birth_day) + '/' + str(birth_year)
    return string1 + birthdate
  for i in months:
    if int(i) < birth_month:
      counter += months[i]
    if int(i)== birth_month:
      counter += birth_day
  # days = 40
  #  6/18/2003
  days += counter
  while days > 0:
    if birth_year%4 == 0:
      months['2'] = 29
    else:
      months['2'] = 28
    for i in months:
      if days < months[i]:
        birth_month = i
        birth_day = days
        
        if birth_day == 0:
          birth_day += 1
        birthdate = str(birth_month) + '/' + str(birth_day) + '/' + str(birth_year)
        return string1 + birthdate
      days -= months[i]
      
    birth_year += 1
      
print(how_many_days_after(birthdate,days))
