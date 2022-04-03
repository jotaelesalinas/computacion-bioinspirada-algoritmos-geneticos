##########################################################################
# hiperparámetros
##########################################################################

# define el numero de iteraciones (generaciones)
n_iteraciones = 200
# define el tamaño de la población
t_poblacion = 100
# ratio de intercambio
r_intercambio = 0.9
# multiplicador del ratio de mutación
m_r_mutacion = 1.0
# número de contendientes para pasar a la siguiente generación
n_k = 3

##########################################################################
# parámetros del problema
##########################################################################

def func1(x):
    return 6.0 * x**4 + 20.0 * x**3 - 5 * x 

def func2(x):
    return 3 * x 

def func3(x):
    return 2.0 * x**4 - 10.0 * x**3 + 3.0 * x**2 - 5.0 * x 

def objective(values):
    return func1(values[0]) + func2(values[0]) + func3(values[0])

n_values = 1

n_bits = n_values * [20]

rangos = n_values * [[-5.0, 5.0]]

##########################################################################
# parámetros que dependen de los hiperparámetros y del problema
##########################################################################

# ratio de mutación
r_mutacion = m_r_mutacion / float(sum(n_bits))

##########################################################################
# funciones de ayuda
##########################################################################

# desempaqueta el bitstring y lo convierte en números dentro de rangos
def desempaqueta(rangos, n_bits, bitstring):
	decoded = list()
	for i in range(len(n_bits)):
		# extract the substring
		start, end = i * n_bits[i], (i * n_bits[i]) + n_bits[i]
		substring = bitstring[start:end]
		# convert bitstring to a string of chars
		chars = ''.join([str(s) for s in substring])
		# convert string to integer
		integer = int(chars, 2)
		# scale integer to desired range
		largest = 2**n_bits[i]
		value = rangos[i][0] + (integer/largest) * (rangos[i][1] - rangos[i][0])
		# store
		decoded.append(value)
	return decoded

##########################################################################
# algoritmo genético
##########################################################################

# genetic algorithm search of the one max optimization problem
from numpy.random import randint
from numpy.random import rand

# tournament selection
def selection(pop, scores, k):
	# first random selection
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]
 
# crossover two parents to create two children
def crossover(p1, p2, r_intercambio):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if rand() < r_intercambio:
		# select crossover point that is not on the end of the string
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]
 
# mutation operator
def mutation(bitstring, r_mutacion):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mutacion:
			# flip the bit
			bitstring[i] = 1 - bitstring[i]
 
# genetic algorithm
def genetic_algorithm(objective, rangos, n_bits, n_iteraciones, t_poblacion, r_intercambio, r_mutacion, n_k):
	# initial population of random bitstring
	pop = [randint(0, 2, sum(n_bits)).tolist() for _ in range(t_poblacion)]
	# keep track of best solution
	best, best_eval = 0, objective(desempaqueta(rangos, n_bits, pop[0]))
	# enumerate generations
	for gen in range(n_iteraciones):
		# decode population
		decoded = [desempaqueta(rangos, n_bits, p) for p in pop]
		# evaluate all candidates in the population
		scores = [objective(d) for d in decoded]
		# check for new best solution
		for i in range(t_poblacion):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
		# select parents
		selected = [selection(pop, scores, n_k) for _ in range(t_poblacion)]
		# create the next generation
		children = list()
		for i in range(0, t_poblacion, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			for c in crossover(p1, p2, r_intercambio):
				# mutation
				mutation(c, r_mutacion)
				# store for next generation
				children.append(c)
		# replace population
		pop = children
	return [best, best_eval]

# perform the genetic algorithm search
best, score = genetic_algorithm(objective, rangos, n_bits, n_iteraciones, t_poblacion, r_intercambio, r_mutacion, n_k)
print('Done!')
decoded = desempaqueta(rangos, n_bits, best)
print('f(%s) = %f' % (decoded, score))
