def remove_chars(text, n):
   if n <= len(text):
      val = text[n:]
   else:
      val = 'n is longer than text string'
   return val


print(remove_chars("Test of the national weather system.", 5))