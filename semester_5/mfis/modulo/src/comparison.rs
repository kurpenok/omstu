use crate::{
    gcd::gcd,
    ops::{mod_add, mod_div},
};

fn solve_comparison(a: i32, b: i32, m: i32) -> Option<Vec<Vec<i32>>> {
    let divisor = gcd(a, m);
    if b % divisor != 0 {
        return None;
    }

    let mut solutions: Vec<Vec<i32>> = Vec::new();
    if divisor == 1 {
        let solution = mod_div(b, a, m);
        if solution.is_none() {
            println!("[-] No inverse for given number!");
            return None;
        }
        solutions.push(vec![solution.unwrap()]);
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
            solutions.push(vec![solution.unwrap() + (i * new_m)]);
        }
    }

    Some(solutions)
}

fn solve_comparison_system(a: i32, b: i32, c: i32, d: i32, m: i32) -> Option<Vec<Vec<i32>>> {
    let mut solutions = Vec::new();

    // ATTENTION!
    // Coefficients of first function must be GREATER than second function!
    let solutions_1 = solve_comparison((a - c).abs(), mod_add(0, b - d, m), m);
    let solutions_2 = solve_comparison((a - c).abs(), mod_add(0, d - b, m), m);

    if solutions_1.is_none() && solutions_2.is_none() {
        return None;
    }

    if solutions_1.is_some() {
        for solution in &solutions_1.unwrap() {
            solutions.push(vec![solution[0], mod_add(0, b - a * solution[0], m)]);
        }
    }

    if solutions_2.is_some() {
        for solution in &solutions_2.unwrap() {
            solutions.push(vec![solution[0], mod_add(0, d - a * solution[0], m)]);
        }
    }

    Some(solutions)
}

pub fn solve(a: i32, b: i32, c: Option<i32>, d: Option<i32>, m: i32) -> Option<Vec<Vec<i32>>> {
    match (c, d) {
        (None, None) => solve_comparison(a, b, m),
        (Some(c), Some(d)) => solve_comparison_system(a, b, c, d, m),
        _ => {
            println!("[-] Incorrect args!");
            return None;
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_incorrect_comparison_solve() {
        assert_eq!(solve(4, 6, None, Some(2), 8), None);
        assert_eq!(solve(5, 7, Some(2), None, 15), None);
    }

    #[test]
    fn test_simple_comparison_solve() {
        assert_eq!(solve(4, 6, None, None, 8), None);
        assert_eq!(solve(5, 7, None, None, 15), None);

        assert_eq!(solve(1, 2, None, None, 3), Some(vec![vec![2]]));
        assert_eq!(solve(6, 8, None, None, 10), Some(vec![vec![3], vec![8]]));
    }

    #[test]
    fn test_comparison_system_solve() {
        assert_eq!(solve(0, 9, Some(8), Some(15), 32), None);
        assert_eq!(solve(10, 9, Some(6), Some(3), 8), None);

        assert_eq!(
            solve(18, 9, Some(5), Some(7), 15),
            Some(vec![vec![14, 12], vec![1, 4]])
        );
        assert_eq!(
            solve(14, 8, Some(5), Some(19), 32),
            Some(vec![vec![13, 18], vec![19, 9]])
        );
    }
}
