pub mod gcd;
pub mod ops;

mod cli;
mod cli_gcd;

use cli::console_read;
use cli_gcd::cli_gcd;

static SEPARATOR: &str = "==================================================";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions:");
    println!("[1] Find GCD");
    println!("[2] Invert by modulo");
    println!("[3] Solve comparison by modulo");
    println!("[4] Solve comparisons system by modulo");
    println!("{}", SEPARATOR);

    loop {
        let action = console_read("[>] Enter action number: ");

        if action == "1" {
            cli_gcd();
        } else if action == "2" {
        } else if action == "3" {
        } else if action == "4" {
        } else {
        }
    }
}
