use rand::rng;
use rand::Rng;

// Structure of individual with genes and fitness index
#[derive(Debug, Clone)]
struct Individual {
    genes: Vec<f64>,
    fitness: f64,
}

impl Individual {
    // Creating new individual with random genes
    fn new(num_genes: usize, rng: &mut impl Rng) -> Self {
        let genes = (0..num_genes)
            .map(|_| rng.random_range(-5.0..5.0))
            .collect();
        Self {
            genes,
            fitness: 0.0,
        }
    }

    // Calculation of fitness (minimizing the sum of squares)
    fn calculate_fitness(&mut self) {
        let sum_squares: f64 = self.genes.iter().map(|x| x.powi(2)).sum();
        self.fitness = 1.0 / (1.0 + sum_squares); // Conversion to maximize
    }
}

// Generation of initial population
fn generate_population(size: usize, num_genes: usize, rng: &mut impl Rng) -> Vec<Individual> {
    (0..size).map(|_| Individual::new(num_genes, rng)).collect()
}

// Parents' selection by roulette method
fn select_parent<'a>(population: &'a [Individual], rng: &mut impl Rng) -> &'a Individual {
    let total_fitness: f64 = population.iter().map(|ind| ind.fitness).sum();
    let mut threshold = rng.random_range(0.0..total_fitness);

    for ind in population {
        threshold -= ind.fitness;
        if threshold <= 0.0 {
            return ind;
        }
    }
    population.last().unwrap()
}

// Single-point crossover
fn crossover(p1: &Individual, p2: &Individual, rng: &mut impl Rng) -> (Individual, Individual) {
    let point = rng.random_range(0..p1.genes.len());
    let (mut c1_genes, mut c2_genes) = (Vec::new(), Vec::new());

    for i in 0..p1.genes.len() {
        if i <= point {
            c1_genes.push(p1.genes[i]);
            c2_genes.push(p2.genes[i]);
        } else {
            c1_genes.push(p2.genes[i]);
            c2_genes.push(p1.genes[i]);
        }
    }

    (
        Individual {
            genes: c1_genes,
            fitness: 0.0,
        },
        Individual {
            genes: c2_genes,
            fitness: 0.0,
        },
    )
}

// Mutation with given probability
fn mutate(ind: &mut Individual, rate: f64, strength: f64, rng: &mut impl Rng) {
    ind.genes.iter_mut().for_each(|g| {
        if rng.random_bool(rate) {
            *g += rng.random_range(-strength..strength);
        }
    });
}

fn main() {
    let mut rng = rng();
    let params = (
        100,  // Population size
        3,    // Problem dimension (3 variables)
        0.15, // Probability of mutation
        0.5,  // Power of mutation
        200,  // Number of generations
    );

    // Initialization of the population
    let mut population = generate_population(params.0, params.1, &mut rng);
    population
        .iter_mut()
        .for_each(|ind| ind.calculate_fitness());

    for gen in 0..params.4 {
        let mut next_gen = Vec::with_capacity(params.0);

        // Generation of descendants
        while next_gen.len() < params.0 {
            let p1 = select_parent(&population, &mut rng);
            let p2 = select_parent(&population, &mut rng);
            let (mut c1, mut c2) = crossover(p1, p2, &mut rng);

            // Apply a mutation
            mutate(&mut c1, params.2, params.3, &mut rng);
            mutate(&mut c2, params.2, params.3, &mut rng);

            // Recalculation of fitness
            c1.calculate_fitness();
            c2.calculate_fitness();

            next_gen.push(c1);
            next_gen.push(c2);
        }

        // Pruning to population size
        next_gen.truncate(params.0);
        population = next_gen;

        // Report on best result
        let best = population
            .iter()
            .max_by(|a, b| a.fitness.partial_cmp(&b.fitness).unwrap())
            .unwrap();
        println!("Generation {}: best fitness {:.4}", gen, best.fitness);
    }
}
