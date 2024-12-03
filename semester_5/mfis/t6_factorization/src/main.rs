mod cli;
mod modules;

use cli::{cli_factorization::cli_factorization, console_read};

static SEPARATOR: &str = "==================================================";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Factorize number");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_factorization(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
