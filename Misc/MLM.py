# MLM n-ary commission distribution

def get_init(totalsum,r,n,levels):
	factor_sum = 0

	for i in range(levels):
		factor_sum += pow(r,i)*pow(n,(levels-1)-i)

	init = totalsum/factor_sum
	return init


totalsum = 10
r = 1.20
levels = 3
n = 2

a = get_init(totalsum,r,n,levels)

team_strength = 0
remaining = totalsum

for i in range(levels):
	
	ps = a*pow(r,i)
	lm = pow(n,(levels-1)-i)

	print("levels",levels-i," members = ",lm," profit share per member = ",ps," amount remaining = ", remaining)
	remaining -= (lm*ps) 
	team_strength += lm

print("\nremaining amount = ",remaining)
print("total team members = ", team_strength)
print("level increment = ",r*100-100," % ")


