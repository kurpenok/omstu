use crate::{gcd::gcd, ops::mod_div};

fn solve_comparison(a: i32, b: i32, m: i32) -> Option<Vec<i32>> {
    let divisor = gcd(a, m);
    if b % divisor != 0 {
        return None;
    }

    let mut solutions: Vec<i32> = Vec::new();
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

//fn solve_comparison_system(a: i32, b: i32, c: i32, d: i32, m: i32) -> Option<Vec<i32>> {
//    todo!()
//}

pub fn solve(a: i32, b: i32, c: Option<i32>, d: Option<i32>, m: i32) -> Option<Vec<i32>> {
    match (c, d) {
        (None, None) => solve_comparison(a, b, m),
        //(Some(c), Some(d)) => solve_comparison_system(a, b, c, d, m),
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

        assert_eq!(solve(1, 2, None, None, 3), Some(vec![2]));
        assert_eq!(solve(6, 8, None, None, 10), Some(vec![3, 8]));
    }
}
