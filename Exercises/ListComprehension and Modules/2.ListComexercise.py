colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

appendedList1 = [(c,s) for c in colors for s in sizes]

soledOut = [('Black', 'm'), ('White', 's')]
appendedList2 = [(c,s) for c in colors for s in sizes if(c,s) not in soledOut]