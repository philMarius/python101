value = input('How much does that cost?\n')
value = int(value)

if value < 10:
  print("That's a great deal!")
elif 10 <= value <= 20:
  print ("I'd still pay that")
else:
  print("Wow that's too much")
