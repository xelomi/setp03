def tri_pascal(n):
	if n==0:
		print ("[1]")
		return [1]
	else:
		nivel=[1]
		base_anterior=tri_pascal(n-1)
		for i in range(len(base_anterior)-1):
			nivel.append(base_anterior[i]+base_anterior[i+1])
		nivel.append(1)
		print(nivel)
		return nivel


n=eval(input("pedido usuario "))
nivelfinal=tri_pascal(n)
