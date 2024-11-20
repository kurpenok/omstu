pub struct BezuCoefs {
    pub alpha: i32,
    pub beta: i32,
}

impl BezuCoefs {
    pub fn new() -> BezuCoefs {
        BezuCoefs { alpha: 0, beta: 0 }
    }
}

pub fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

pub fn extended_gcd(a: usize, b: usize, coefs: &mut BezuCoefs) -> usize {
    if a == 0 {
        coefs.alpha = 0;
        coefs.beta = 1;
        return b;
    }

    let mut temp_coefs = BezuCoefs { alpha: 0, beta: 0 };
    let divider = extended_gcd(b % a, a, &mut temp_coefs);

    coefs.alpha = temp_coefs.beta - (b / a) as i32 * temp_coefs.alpha;
    coefs.beta = temp_coefs.alpha;

    divider
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_gcd() {
        assert_eq!(gcd(6, 4), 2);
        assert_eq!(gcd(10, 5), 5);
        assert_eq!(gcd(19, 17), 1);
        assert_eq!(gcd(20, 20), 20);
    }

    #[test]
    fn test_extended_gcd() {
        let mut coefs = BezuCoefs::new();

        assert_eq!(extended_gcd(3, 7, &mut coefs), 1);
        assert_eq!(coefs.alpha, -2);
        assert_eq!(coefs.beta, 1);
    }
}
