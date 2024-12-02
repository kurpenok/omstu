use cli::{cli_crack::cli_crack, console_read};

mod cli;
mod modules;

static SEPARATOR: &str = "==================================================";
static EN_ABC: &str = "abcdefghijklmnopqrstuvwxyz";
static RU_ABC: &str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Crack RSA");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_crack(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
