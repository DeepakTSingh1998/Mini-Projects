def Palindrome(S): 
  ans = ''
  for i in range(-1,-len(S)-1,-1):
    ans += S[i]
    
  if S == ans:
    return 'Palindrome'
  else:
    return 'Not Palindrome'
    
