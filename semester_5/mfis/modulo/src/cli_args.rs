use clap::Args;
use clap::Parser;
use clap::Subcommand;

#[derive(Args)]
pub struct Gcd {
    #[arg(long)]
    pub a: i32,

    #[arg(long)]
    pub b: i32,
}

#[derive(Args)]
pub struct Invert {
    #[arg(long)]
    pub a: i32,

    #[arg(long)]
    pub m: i32,
}

#[derive(Subcommand)]
pub enum Commands {
    Invert(Invert),
    Gcd(Gcd),
}

#[derive(Parser)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,
}
