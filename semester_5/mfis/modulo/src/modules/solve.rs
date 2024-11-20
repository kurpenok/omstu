use super::{gcd::gcd, ops::mod_div};

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
}
