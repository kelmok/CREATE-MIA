def fact(x):
  if x > 0:
    rtn = 1
    for i in range(1, (x+1)):
      rtn *= i

    return rtn

  else:
    return None
