use clap::Parser;
use cli_actions::{cli_gcd, cli_invert};
use cli_args::{Cli, Commands};

pub mod gcd;
pub mod invert;
pub mod ops;

mod cli_actions;
mod cli_args;

fn main() {
    // Usage:
    // cargo run -- gcd --a <a> --b <b>
    // cargo run -- invert --a <a> --m <m>

    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Gcd(data)) => cli_gcd(data),
        Some(Commands::Invert(data)) => cli_invert(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}
