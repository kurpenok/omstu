pub mod modules;

mod cli;

use cli::{cli_gcd::cli_gcd, cli_invert::cli_invert, cli_solve::cli_solve, console_read};

static SEPARATOR: &str = "==================================================";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Find GCD");
    println!("[2] Get inverse by modulo");
    println!("[3] Solve comparison by modulo");
    println!("[4] Solve comparisons system by modulo");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_gcd(),
            "2" => cli_invert(),
            "3" => cli_solve(false),
            "4" => cli_solve(true),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
