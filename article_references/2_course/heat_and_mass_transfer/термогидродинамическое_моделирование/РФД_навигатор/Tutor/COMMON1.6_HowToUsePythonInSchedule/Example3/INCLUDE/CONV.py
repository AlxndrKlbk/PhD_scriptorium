from datetime import datetime

def __init_script__ ():
  #Cоздание графиков для хранения числа переключаемых скважин для группы и месторождения
  create_graph (name = 'group_count', type = 'group', default_value = 0)
  create_graph (name = 'all_count', type = 'field', default_value = 0)

def convert_with_limits():
  wct_lim=0.95
  group_limit=3
  all_limit=10
  groupnames=['G1','G2','G3','G4']
  #Извлечение числа переключенных скважин
  gc=get_global_graph(name = 'group_count')
  ac=get_global_graph(name = 'all_count')
  wells=[]
  wcts=[]
  #Если число переключенных скважин для месторождения еще не исчерпано
  if ac<all_limit:
    #Для каждой группы
    for gname in groupnames:
      g=get_group_by_name(gname)
      #Если число переключенных скважин для этой группы еще не исчерпано
      if gc[g]<group_limit:
        #выбирается скважина с максимальным значением обводненности
        w=get_well_by_criterion(group=g, method='max',crit=wwct)
        if wwct[w]>wct_lim:
          wells.append(w)
          wcts.append(float(wwct[w]))
    #Из выбранных скважин (если таковые имеются)
    if len(wells)>0:
      #выбирается скважина, имеющая максимальное значение обводненности
      w=wells[wcts.index(max(wcts))]
      #и переключается на закачку с контролем по BHP
      add_keyword(
      """
      WCONINJE
      """+w.name+""" WATER OPEN BHP 2* 210 /
      /
      """
      )
      print("В",get_current_date ().strftime("%d.%m.%Y %H:%M:%S"),"скважина",w.name,"переключилась на закачку")
      gc[w.group]+=1
      if gc[w.group]==group_limit:
        print("В группе",w.group.name,"переключено на закачку предельное число скважин")
      ac+=1
      if ac==all_limit:
        print("В модели переключено на закачку предельное число скважин")
  #Обновление и сохранение числа переключенных скважин
  export(gc, name = 'group_count')
  export(ac, name = 'all_count')
