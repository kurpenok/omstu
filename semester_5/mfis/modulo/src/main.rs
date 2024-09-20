use clap::Parser;
use cli_actions::cli_invert;
use cli_args::{Cli, Commands};

pub mod invert;
pub mod ops;

mod cli_actions;
mod cli_args;
mod gcd;

fn main() {
    // Usage:
    // cargo run -- invert --a "<a>" --m "<m>"

    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Invert(data)) => cli_invert(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}
