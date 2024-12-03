mod cli;
mod modules;

use cli::{cli_logarithm::cli_logarithm, console_read};

static SEPARATOR: &str = "==================================================";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Find discrete logarithm");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_logarithm(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
