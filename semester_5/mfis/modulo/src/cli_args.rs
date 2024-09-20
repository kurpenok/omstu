use clap::Args;
use clap::Parser;
use clap::Subcommand;

#[derive(Args)]
pub struct Invert {
    #[arg(long)]
    pub a: String,

    #[arg(long)]
    pub m: String,
}

#[derive(Subcommand)]
pub enum Commands {
    Invert(Invert),
}

#[derive(Parser)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,
}
