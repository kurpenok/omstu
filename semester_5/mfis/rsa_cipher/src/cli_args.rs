use clap::Args;
use clap::Parser;
use clap::Subcommand;

#[derive(Args)]
pub struct Generate {
    #[arg(long)]
    pub p: i32,

    #[arg(long)]
    pub q: i32,

    #[arg(long)]
    pub e: Option<i32>,
}

#[derive(Args)]
pub struct Encrypt {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,

    #[arg(long)]
    pub e: i32,

    #[arg(long)]
    pub n: i32,
}

#[derive(Args)]
pub struct Decrypt {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,

    #[arg(long)]
    pub d: i32,

    #[arg(long)]
    pub n: i32,
}

#[derive(Subcommand)]
pub enum Commands {
    Generate(Generate),
    Encrypt(Encrypt),
    Decrypt(Decrypt),
}

#[derive(Parser)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,
}
