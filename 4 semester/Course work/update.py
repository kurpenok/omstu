import random

# Функция для генерации начальной популяции геномов
def generate_population(size, n_jobs):
    population = []
    for i in range(size):
        genome = list(range(n_jobs))
        random.shuffle(genome)
        population.append(genome)
    return population

# Функция для вычисления суммарного запаздывания выполнения всех заданий
def calculate_delay(genome, processing_times, due_dates):
    n_jobs = len(genome)
    machine_times = [0] * n_jobs
    delays = [0] * n_jobs
    for job in genome:
        machine_times[job] += processing_times[job]
        delay = max(0, machine_times[job] - due_dates[job])
        delays[job] = delay
    return sum(delays)

# Функция для выполнения селекции родительских геномов
def selection(population, fitness_fn):
    fits = [fitness_fn(genome) for genome in population]
    return random.choices(population, fits, k=2)

# Функция для выполнения скрещивания родительских геномов
def crossover(parents):
    p1, p2 = parents
    n = len(p1)
    c1, c2 = [-1] * n, [-1] * n
    a, b = random.sample(range(n), 2)
    if a > b:
        a, b = b, a
    c1[a:b+1], c2[a:b+1] = p1[a:b+1], p2[a:b+1]
    idx1, idx2 = 0, 0
    for i in range(n):
        if i < a or i > b:
            while p2[idx1] in c1:
                idx1 += 1
            while p1[idx2] in c2:
                idx2 += 1
            c1[i], c2[i] = p2[idx1], p1[idx2]
    return c1, c2

# Функция для выполнения мутации потомков
def mutation(genome, mutation_rate):
    n = len(genome)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randint(0, n-1)
            genome[i], genome[j] = genome[j], genome[i]
    return genome

# Функция для выполнения генетического алгоритма
def genetic_algorithm(processing_times, due_dates, population_size=100, generations=100, mutation_rate=0.1):
    n_jobs = len(processing_times)
    population = generate_population(population_size, n_jobs)
    for i in range(generations):
        new_population = []
        for j in range(population_size):
            parents = selection(population, lambda genome: calculate_delay(genome, processing_times, due_dates))
            offspring = crossover(parents)
            child1 = mutation(offspring[0], mutation_rate)
            child2 = mutation(offspring[1], mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    best_genome = min(population, key=lambda genome: calculate_delay(genome, processing_times, due_dates))
    best_delay = calculate_delay(best_genome, processing_times, due_dates)
    return best_genome, best_delay

processing_times = [2, 4, 3, 6]
due_dates = [10, 7, 12, 8]

best_genome, best_delay = genetic_algorithm(processing_times, due_dates, population_size=100, generations=100, mutation_rate=0.1)

print("Лучший найденный геном: ", best_genome)
print("Соответствующее суммарное запаздывание: ", best_delay)
