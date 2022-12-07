def nameCheck(choice, file):
  occurrencies = []
  with open(file, 'r', encoding='utf-8') as f:
      lines = f.readlines()
      for line in lines:
          rule = line.split(" ")
          if choice in rule[0]:
              occurrencies.append(rule[0])

  return occurrencies
