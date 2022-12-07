def seekRule(input, file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
      lines = f.readlines()
      for line in lines:
        rule = line.split(" ")
        if rule[0] == input:
          return rule

 