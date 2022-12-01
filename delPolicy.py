def delPolicy():
      import os
      from seekRule import seekRule

      respond = input("Do you want to delete an Input or Output rule? (I/O) >>> ")
      string_input=input("\nInsert name of Policy to delete:\n")
      
      if respond == "I":
         file_chosen = "InBound.txt"

      elif respond == "O":
         file_chosen = "OutBound.txt"

      with open(file_chosen, "r") as inputd:
         with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in inputd:
                  # if substring contain in a line then don't write it
                  if string_input not in line.strip("\n"):
                     output.write(line)
      rule_properties = seekRule(string_input, file_chosen)
      
      if respond == "I":
         os.system(f"sudo iptables -D INPUT -s {rule_properties[1]} -j {rule_properties[4]}")
      elif respond == "O":
         os.system(f"sudo iptables -D OUTPUT -s {rule_properties[1]} -j {rule_properties[4]}")
      
      print('POLICY Deleted')

      # replace file with original name
      os.replace('temp.txt', file_chosen)
