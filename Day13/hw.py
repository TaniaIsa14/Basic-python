def fabonic(n):
    if n<=1:
        return n
    else:
      return fabonic(n-1)+fabonic(n-2)
print(fabonic(9))