use cli::{cli_entropy::cli_entropy, console_read};

mod cli;
mod modules;

static SEPARATOR: &str = "==================================================";
static EN_ABC: &str = "abcdefghijklmnopqrstuvwxyz";
static RU_ABC: &str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Make entropy plot");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_entropy(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
