def off_branch_orat():
	branches=[0,1,2]		#номера стволов
	for w in get_all_wells():		#цикл по всем скважинам
		for branch in branches:		#цикл по стволам одной скважины
			result=0
			for c in w.get_connections_from_branch (branch_id = branch):
				if not c.is_opened(): continue
				result+=copr[c]				#Суммируется дебит для ствола
			print("Oil rate on branch ",branch,result)
			if result<75:					#Если дебит меньше порогового значения, закрыть ствол
				print("Closing branch",branch,"with rate",result)
				change_well_perforation(well=w.name, branch=branch, mdu=1600, mdl=2500, depth='MD', status='shut')
