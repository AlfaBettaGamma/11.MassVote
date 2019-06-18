def MassVote(N, Votes):
  g = 0
  x = 0
  n = 0
  res = []
  sort = []
  fin = ''
  if N == 1:
    return 'majority winner 1'
  if N == len(Votes):
    for i in range(N):
      if Votes[i] < 0:
        print('Неверно введенные данные!')
        break
      g = g + Votes[i]
    for i in range(N):
      x = (100*Votes[i])/g
      x = round(x,2)
      res.append(x)
      sort.append(x)
    for i in range(0,N-1):
      for j in range(0,N-i-1):
        if sort[j] < sort[j+1]:
          sort[j],sort[j + 1] = sort[j + 1], sort[j]
    for i in range(N):
      if sort[0] == res[i] :
        n = i
    for i in range(N):
      if sort[i] > sort[i + 1] and sort[i] > 50 :
        fin = 'majority winner '+ str(n + 1)
        return fin
      elif sort[i] > sort[i + 1] and sort[i] < 50 :
        fin = 'minority winner '+ str(n + 1)
        return fin
      else:
        return 'no winner'
  else:
    return print('Неверно введенные данные!')