use clap::Parser;
use cli_actions::{cli_gcd, cli_invert, cli_solve};
use cli_args::{Cli, Commands};

pub mod comparison;
pub mod gcd;
pub mod invert;
pub mod ops;

mod cli_actions;
mod cli_args;

fn main() {
    // Usage:
    // cargo run -- gcd --a <a> --b <b>
    // cargo run -- invert --a <a> --m <m>
    // cargo run -- solve --a <a> --b <b> --m <m>
    // cargo run -- solve --a <a> --b <b> --c <c> --d <d> --m <m>

    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Gcd(data)) => cli_gcd(data),
        Some(Commands::Invert(data)) => cli_invert(data),
        Some(Commands::Solve(data)) => cli_solve(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}
