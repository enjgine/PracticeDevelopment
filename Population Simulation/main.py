import numpy

age_groups = {}
for i in range(0,101):
	age_groups[i] = 0

print("Enter details")
start_age = int(input("Start age: "))
end_age = int(input("End age: "))
start_pop = int(input("Number of pop: "))
sim_len = int(input("Simulation years: "))
avg_ls = int(input("Average Lifespan: "))
fr_start = int(input("Age of first birth: "))
fr_num = int(input("Fertility rate: "))
fr_end = int(input("Seperation of births: "))

pop_div = end_age - start_age

for i in range(start_age, end_age+1):
	age_groups[i] = pop_div

for i in range(sim_len):
	