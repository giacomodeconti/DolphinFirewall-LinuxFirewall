def delPolicy():
      import os
      from nameCheck import nameCheck
      from seekRule import seekRule

      # input for delete policy
      respond = input("Do you want to delete an Input or Output rule? (I/O) >>> ")
      string_input=input("\nInsert name of Policy to delete:\n")

      # file finder by input
      if respond == "I":
         chosen_file = "InBound.txt"
         chain = "INPUT"
         icmp_io = "request"

      elif respond == "O":
         chosen_file = "OutBound.txt"
         chain = "OUTPUT"
         icmp_io = "reply"

      # Looks for occurrencies of the rule name in the file and stores them in a list
      occurrencies = nameCheck(string_input,chosen_file)

      #TO DO: Insert a control that checks if there are similar names or if theres is none similar to the input
      print("There are files that have the same name, which one do you want to delete?")

      #Displays occurrencies of the rule name with index to let the user choose the right one
      for idx,name in enumerate(occurrencies):
         print(f" {idx + 1} >>> {name}")

      # Asking user for the rule to be deleted
      del_rule = int(input("Choose >>> "))
      # Selects the occurrency chosen by user (name of the rule that will be deleted)
      to_be_del = occurrencies[del_rule-1]

      # Fetch the file and Tranforms all the properties of the rule that has to be deleted in a list
      del_rule_props = seekRule(to_be_del, chosen_file)

      #Defining all rule properties from del_rule_props (will be used in )
      r_prop = {
        "policyName": del_rule_props[0],
        "IPs": del_rule_props[1],
        "IPd": del_rule_props[2],
        "port": del_rule_props[3],
        "protocol": del_rule_props[4],
        "traffic": del_rule_props[5]
      }

      with open(chosen_file, "r") as inputd:
         with open("temp.txt", "w") as output:
            # reading all lines of the file
            for line in inputd:
               rule = line.split(" ")
               #Looks in the file for the rule name of the rule that has to be deleted
               cline_rule_name = rule[0]
               if cline_rule_name == to_be_del:
                  #If the rule name of the current line (cline_rule_name) is the same of the the rule that has to be deleted (to_be_del),
                  if r_prop['protocol'] == "icmp":
                    os.system(f"sudo iptables -D {chain} -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} -j {r_prop['traffic']} --icmp-type echo-{icmp_io}")
                  else:
                    os.system(f"sudo iptables -D {chain} -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} --dport {r_prop['port']} -j {r_prop['traffic']}")

               if cline_rule_name != to_be_del:
                  #If the rule name of the current line is different from the rule name of the rule that has to be deleted, it writes it on the temporary file that will then be swapped with the current file
                  output.write(line)

      # replace file with original name
      os.replace('temp.txt', chosen_file)

      print('POLICY Deleted')


"""

      if respond == "I":
    #icmp requests
         if r_prop['protocol']=='icmp':
               os.system(f"sudo iptables -D INPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} -j {r_prop['traffic']} --icmp-type echo-request")
         elif r_prop['protocol'] == 'all':
               os.system(f"sudo iptables -D INPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p tcp --dport {r_prop['port']} -j {r_prop['traffic']}")
               os.system(f"sudo iptables -D INPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p udp --dport {r_prop['port']} -j {r_prop['traffic']}")
         else:
               os.system(f"sudo iptables -D INPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} --dport {r_prop['port']} -j {r_prop['traffic']}")

      elif respond == "O":
         if r_prop['protocol'] == 'icmp':
               os.system(f"sudo iptables -D OUTPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} -j {r_prop['traffic']} --icmp-type echo-reply")
         elif r_prop['protocol'] == 'all':
               os.system(f"sudo iptables -D OUTPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p tcp --dport {r_prop['port']} -j {r_prop['traffic']}")
               os.system(f"sudo iptables -D OUTPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p udp --dport {r_prop['port']} -j {r_prop['traffic']}")
         else:
               os.system(f"sudo iptables -D OUTPUT -s {r_prop['IPs']} -d {r_prop['IPd']} -p {r_prop['protocol']} --dport {r_prop['port']} -j {r_prop['traffic']}")

"""
