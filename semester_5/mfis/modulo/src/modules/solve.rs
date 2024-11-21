use super::{
    gcd::gcd,
    ops::{mod_add, mod_div},
};

pub fn solve_comparison(a: usize, b: usize, m: usize) -> Option<Vec<usize>> {
    let divisor = gcd(a, m);
    if b % divisor != 0 {
        return None;
    }

    let mut solutions: Vec<usize> = Vec::new();
    if divisor == 1 {
        let solution = mod_div(b, a, m);
        if solution.is_none() {
            println!("[-] No inverse for given number!");
            return None;
        }
        solutions.push(solution.unwrap());
    } else {
        let new_a = a / divisor;
        let new_b = b / divisor;
        let new_m = m / divisor;

        let solution = mod_div(new_b, new_a, new_m);
        if solution.is_none() {
            println!("[-] No inverse for given number!");
            return None;
        }

        for i in 0..divisor {
            solutions.push(solution.unwrap() + (i * new_m));
        }
    }

    Some(solutions)
}

pub fn solve_comparisons_system(
    a: usize,
    b: usize,
    c: usize,
    d: usize,
    m: usize,
) -> Option<Vec<Vec<usize>>> {
    let mut solutions: Vec<Vec<usize>> = Vec::new();

    let mut solutions_x: Vec<usize> = Vec::new();
    let (new_a, new_b) = if a < c {
        (c - a, mod_add(0, d as i32 - b as i32, m))
    } else {
        (a - c, mod_add(0, b as i32 - d as i32, m))
    };

    match solve_comparison(new_a, new_b, m) {
        Some(solutions) => {
            for s in solutions {
                solutions_x.push(s);
            }
        }
        None => (),
    }

    for x in solutions_x {
        let y = mod_add(0, b as i32 - a as i32 * x as i32, m);
        solutions.push(vec![x, y]);
    }

    if solutions.len() == 0 {
        return None;
    }
    Some(solutions)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_simple_comparison_solve() {
        assert_eq!(solve_comparison(4, 6, 8), None);
        assert_eq!(solve_comparison(5, 7, 15), None);

        assert_eq!(solve_comparison(1, 2, 3), Some(vec![2]));
        assert_eq!(solve_comparison(6, 8, 10), Some(vec![3, 8]));
    }

    #[test]
    fn test_comparison_system_solve() {
        assert_eq!(solve_comparisons_system(0, 9, 8, 15, 32), None);
        assert_eq!(solve_comparisons_system(10, 9, 6, 3, 8), None);

        assert_eq!(
            solve_comparisons_system(18, 9, 5, 7, 15),
            Some(vec![vec![14, 12]]),
        );
        assert_eq!(
            solve_comparisons_system(14, 8, 5, 19, 32),
            Some(vec![vec![13, 18]]),
        );
    }
}
