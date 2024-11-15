mod blocks;
mod cli_actions;
mod cli_args;
mod crack;
mod decoder;
mod decryptor;
mod encoder;
mod encryptor;
mod gcd;
mod invert;
mod keygen;
mod prime;

use clap::Parser;
use cli_actions::{cli_crack, cli_decrypt, cli_encrypt, cli_generate};
use cli_args::{Cli, Commands};

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Generate(data)) => cli_generate(data),
        Some(Commands::Encrypt(data)) => cli_encrypt(data),
        Some(Commands::Decrypt(data)) => cli_decrypt(data),
        Some(Commands::Crack(data)) => cli_crack(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}
