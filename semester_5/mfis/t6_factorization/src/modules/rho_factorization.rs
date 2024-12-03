use modulo::{gcd::gcd, ops::mod_add};

fn f(x: usize) -> usize {
    x.pow(2) + 1
}

pub fn factorize(n: usize) -> usize {
    let mut x = 1;
    let mut y = 1;
    let mut p = 1;

    while p == 1 || p == n {
        x = mod_add(0, f(x) as i32, n);
        y = mod_add(0, f(f(y)) as i32, n);
        p = gcd((x as i32 - y as i32).abs() as usize, n);
    }

    p
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_factorize() {
        assert_eq!(factorize(667), 23);
    }
}
