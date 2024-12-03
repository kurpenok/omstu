use modulo::ops::mod_add;

fn is_quadratic_residue(a: usize, m: usize) -> bool {
    mod_add(0, a.pow((m as u32 - 1) / 2) as i32, m) == mod_add(0, -1, m)
}

pub fn factorize(n: usize, a: usize, b: usize, c: usize) -> usize {
    let left = (n as f64).sqrt().ceil() as usize;
    let right = (n / 2) + 1;

    for i in left..=right {
        let a_quadratic_residue = !is_quadratic_residue(i.pow(2) - n, a);
        let b_quadratic_residue = !is_quadratic_residue(i.pow(2) - n, b);
        let c_quadratic_residue = !is_quadratic_residue(i.pow(2) - n, c);

        if a_quadratic_residue && b_quadratic_residue && c_quadratic_residue {
            let z = (i.pow(2) - n) as f64;
            let y = z.sqrt();
            if y.fract() == 0.0 {
                return i + y as usize;
            }
        }
    }

    0
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_factorize() {
        assert_eq!(factorize(667, 3, 5, 7), 29);
    }
}
