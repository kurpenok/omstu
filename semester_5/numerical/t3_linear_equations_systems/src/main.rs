mod gauss;
mod inverse_matrix;

fn main() {
    let mut matrix = vec![
        vec![1.0, 2.0, 0.0, -4.0, 0.0],
        vec![2.0, 1.0, 3.0, 1.0, 3.0],
        vec![1.0, 2.0, 3.0, -4.0, 0.0],
        vec![2.0, 2.0, 5.0, -1.0, 1.0],
    ];

    let separator = "=".repeat(30);

    println!("{}", separator);

    println!("[+] Gauss method");
    println!("[+] Solution: {:?}", gauss::solve(&mut matrix));

    println!("{}", separator);

    println!("[+] Inverse matrix method");
    let matrix = vec![
        vec![1.0, 2.0, 0.0, -4.0],
        vec![2.0, 1.0, 3.0, 1.0],
        vec![1.0, 2.0, 3.0, -4.0],
        vec![2.0, 2.0, 5.0, -1.0],
    ];
    let constants = vec![0.0, 3.0, 0.0, 1.0];
    if let Some(solution) = inverse_matrix::solve(&matrix, &constants) {
        println!("[+] Solution: {:?}", solution);
    } else {
        println!("[-] System of equations has no solution!");
    }

    println!("{}", separator);
}
