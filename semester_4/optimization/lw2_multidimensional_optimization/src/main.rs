fn f(x: &[f64]) -> f64 {
    let a: f64 = 3.0;
    let b: f64 = 2.0;
    let c: f64 = 20.0;

    c - ((x[0] - a) * (-x[0] + a).exp()) - ((x[1] - b) * (-x[1] + b).exp())
}

fn main() {}
