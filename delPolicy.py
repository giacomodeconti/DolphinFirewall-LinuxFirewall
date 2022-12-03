def delPolicy():
      import os
      from nameCheck import nameCheck
      from seekRule import seekRule

      # input for delete policy
      respond = input("Do you want to delete an Input or Output rule? (I/O) >>> ")
      string_input=input("\nInsert name of Policy to delete:\n")

      # file finder by input
      if respond == "I":
         file_chosen = "InBound.txt"

      elif respond == "O":
         file_chosen = "OutBound.txt"

      # call nameCheck function
      occurrencies = nameCheck(string_input,file_chosen)

      print("There are files that have the same name, which one do you want to delete?")
      for idx,name in enumerate(occurrencies):
         print(f" {idx + 1} >>> {name}")
      
      del_rule = int(input("Which rule do you want to delete?"))
      
      with open(file_chosen, "r") as inputd:
         with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in inputd:
               rule = line.split(" ")
               if occurrencies[del_rule-1] != rule[0]:
                  output.write(line)

      rule_p = seekRule(occurrencies[del_rule-1], file_chosen)

      '''
      if respond == "I":
         os.system(f"sudo iptables -D INPUT -s {rule_p[1]} -j {rule_p[4]}")
      elif respond == "O":
         os.system(f"sudo iptables -D OUTPUT -s {rule_p[1]} -j {rule_p[4]}")'''

      if respond == "I":
    #icmp requests
         if rule_p[4]=='icmp':
               os.system(f"sudo iptables -D INPUT -s {rule_p[1]} -d {rule_p[2]} -p {rule_p[4]} -j {rule_p[5]} --icmp-type echo-request")
         elif rule_p[4] == 'all':
               os.system(f"sudo iptables -D INPUT -s {rule_p[1]} -d {rule_p[2]} -p tcp --dport {rule_p[3]} -j {rule_p[5]}")
               os.system(f"sudo iptables -D INPUT -s {rule_p[1]} -d {rule_p[2]} -p udp --dport {rule_p[3]} -j {rule_p[5]}")
         else:
               os.system(f"sudo iptables -D INPUT -s {rule_p[1]} -d {rule_p[2]} -p {rule_p[4]} --dport {rule_p[3]} -j {rule_p[5]}")

      elif respond == "O":
         if rule_p[4] == 'icmp':
               os.system(f"sudo iptables -D OUTPUT -s {rule_p[1]} -d {rule_p[2]} -p {rule_p[4]} -j {rule_p[5]} --icmp-type echo-reply")
         elif rule_p[4] == 'all':
               os.system(f"sudo iptables -D OUTPUT -s {rule_p[1]} -d {rule_p[2]} -p tcp --dport {rule_p[3]} -j {rule_p[5]}")
               os.system(f"sudo iptables -D OUTPUT -s {rule_p[1]} -d {rule_p[2]} -p udp --dport {rule_p[3]} -j {rule_p[5]}")
         else:
               os.system(f"sudo iptables -D OUTPUT -s {rule_p[1]} -d {rule_p[2]} -p {rule_p[4]} --dport {rule_p[3]} -j {rule_p[5]}")
      
      print('POLICY Deleted')

      # replace file with original name
      os.replace('temp.txt', file_chosen)