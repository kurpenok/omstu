pub mod gcd;

mod cli_gcd;

use std::io::Write;

fn main() {
    let separator = "=".repeat(50);

    println!("{}", separator);
    println!("[+] Available actions:");
    println!("[1] Find GCD");
    println!("[2] Invert by modulo");
    println!("[3] Solve comparison by modulo");
    println!("[4] Solve comparisons system by modulo");
    println!("{}", separator);

    loop {
        let mut action = String::new();
        print!("[>] Enter action number: ");
        let _ = std::io::stdout().flush();
        std::io::stdin()
            .read_line(&mut action)
            .ok()
            .expect("[-] Failed to read action number!");
        action = action.trim().to_string();

        if action == "1" {
        } else if action == "2" {
        } else if action == "3" {
        } else if action == "4" {
        } else {
        }
    }
}
