use cli::{
    cli_decrypt::cli_decrypt, cli_encrypt::cli_encrypt, cli_keygen::cli_keygen, console_read,
};

mod cli;
mod modules;

static SEPARATOR: &str = "==================================================";
static EN_ABC: &str = "abcdefghijklmnopqrstuvwxyz";
static RU_ABC: &str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

fn main() {
    println!("{}", SEPARATOR);
    println!("[+] Available actions (0 for quit):");
    println!("[1] Generate keys");
    println!("[2] Encrypt text");
    println!("[3] Decrypt text");
    println!("{}", SEPARATOR);

    loop {
        match console_read("[>] Enter action number: ").as_str() {
            "0" => break,
            "1" => cli_keygen(),
            "2" => cli_encrypt(),
            "3" => cli_decrypt(),
            _ => println!("[-] Incorrect value!"),
        }
    }
}
