def delPolicy():
      import os
      from seekRule import seekRule

	
      string_input=input("\nInsert name of Policy to delete:\n")

      #ricerca 
      with open("InBound.txt", "r") as inputd:
         ### INSERISCI IL CONTROLLO - APPENA VIENE DECISO QUALE REGOLA ALLORA PARTE
         with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in inputd:
                  # if substring contain in a line then don't write it
                  if string_input not in line.strip("\n"):
                     output.write(line)

      ## funzione che ricerca e restituisce i valori della regola in base al nome inserito
      ## Questo per fare in modo che il file 
      rule_properties = seekRule(string_input, "InBound.txt")
      os.system(f"sudo iptables -D INPUT -s {rule_properties[1]} -j {rule_properties[4]}")
      print('POLICY Deleted')

      #cancellazione definitiva
      # replace file with original name
      os.replace('temp.txt', 'InBound.txt')
