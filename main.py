is_magician = False
is_expert = True
  #checking if magician & expert:
if is_expert and is_magician:
  print("You are a master magician!")
   #checking if magician but not expert:
elif is_expert or is_magician:
  print('Atleast you are getting there!')
  #checking if not a magician:
elif not is_magician:
  print("You need magic powers!")

is_magician = True
is_expert = False
  #checking if magician & expert:
if is_expert and is_magician:
  print("You are a master magician!")
   #checking if magician but not expert:
elif is_expert and not is_magician:
  print('Atleast you are getting there!')
  #checking if not a magician:
elif not is_magician:
  print("You need magic powers!")

is_magician = True
is_expert = True
if is_magician and is_expert:
  print('You are a magician and an expert!')
elif is_magician and not is_expert:
  print('You are a magician, but not an expert!')
elif not is_magician and is_expert:
  print('You are not a magician, but you are an expert!')
else:
  print('You are not a magician and not an expert!')

is_magician = False
is_expert = True
if is_magician and is_expert:
  print('You are a magician and an expert!')
elif is_magician and not is_expert:
  print('You are a magician, but not an expert!')
elif not is_magician and is_expert:
  print('You are not a magician, but you are an expert!')
else:
  print('You are not a magician and not an expert!')
