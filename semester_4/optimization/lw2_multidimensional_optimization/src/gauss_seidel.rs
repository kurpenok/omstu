use crate::golden_ratio::golden_ratio_search;

pub fn gauss_seidel_search<F>(f: F, x_0: &[f64], eps: f64, max_iter: usize) -> (Vec<f64>, f64)
where
    F: Fn(&[f64]) -> f64,
{
    let mut x: Vec<f64> = x_0.to_vec();

    for _ in 0..max_iter {
        let x_old = x.clone();

        for i in 0..x_0.len() {
            let f_1d = |x_i: f64| {
                let mut x_temp = x_old.clone();
                x_temp[i] = x_i;
                f(&x_temp)
            };
            x[i] = golden_ratio_search(f_1d, x[i] - 1.0, x[i] + 1.0, eps).0;
        }

        let diff: f64 = x
            .iter()
            .zip(x_old.iter())
            .map(|(new, old)| (new - old).abs())
            .sum();
        if diff < eps {
            break;
        }
    }

    (x.clone(), f(&x))
}
