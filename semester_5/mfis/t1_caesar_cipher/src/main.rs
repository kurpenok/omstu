mod cli;
mod modules;

use cli::{cli_decrypt::cli_decrypt, cli_encrypt::cli_encrypt, console_read};

static SEPARATOR: &str = "==================================================";
static EN_ABC: &str = "abcdefghijklmnopqrstuvwxyz";
static RU_ABC: &str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Encrypt text");
    println!("[2] Decrypt text");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_encrypt(),
            "2" => cli_decrypt(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
