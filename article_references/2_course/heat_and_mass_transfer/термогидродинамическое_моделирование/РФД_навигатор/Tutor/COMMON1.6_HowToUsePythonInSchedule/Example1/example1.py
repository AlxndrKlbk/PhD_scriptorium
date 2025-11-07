def change_layer():
  script_set_options(max_exec_count=360, calculation_start=True)
  increase_execute_count()
  if get_execute_count()==1: return   #Don't start at the first step
  #For all producing wells:
  for w in get_all_wells(type="prod"):
    #If the gas rate is below threshold,
    if wgpr[w]<100:
      #we close the lower connections and open the upper ones:
      add_keyword(
      """
      COMPDATMD
      """+w.name+"""     1*     2020     2030     MD     SHUT     /
      """+w.name+"""     1*     2000     2010     MD     OPEN     2*        0.168        1*        0        1*        1        /
      /
      """)
      print("At",get_current_date().strftime("%d.%m.%Y %H:%M:%S"),"well",w.name,"was switched to the upper reservoir")
