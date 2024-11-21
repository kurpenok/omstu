use crate::{
    modules::solve::{solve_comparison, solve_comparisons_system},
    SEPARATOR,
};

use super::console_read;

pub fn cli_solve(system: bool) {
    if !system {
        let a = console_read("[>] Enter number a: ").parse::<usize>();
        let b = console_read("[>] Enter number b: ").parse::<usize>();
        let m = console_read("[>] Enter modulo: ").parse::<usize>();

        if a.is_err() || b.is_err() || m.is_err() {
            println!("[-] Incorrect values!");
            return;
        }

        match solve_comparison(a.unwrap(), b.unwrap(), m.unwrap()) {
            Some(solutions) => println!("[+] Solutions: {:?}", solutions),
            None => println!("[-] Comparison has no solutions!"),
        }
    } else {
        let a = console_read("[>] Enter number a: ").parse::<usize>();
        let b = console_read("[>] Enter number b: ").parse::<usize>();
        let c = console_read("[>] Enter number c: ").parse::<usize>();
        let d = console_read("[>] Enter number d: ").parse::<usize>();
        let m = console_read("[>] Enter modulo: ").parse::<usize>();

        if a.is_err() || b.is_err() || c.is_err() || d.is_err() || m.is_err() {
            println!("[-] Incorrect values!");
            return;
        }

        match solve_comparisons_system(a.unwrap(), b.unwrap(), c.unwrap(), d.unwrap(), m.unwrap()) {
            Some(solutions) => println!("[+] Solutions: {:?}", solutions),
            None => println!("[-] Comparison has no solutions!"),
        }
    }
    println!("{}", SEPARATOR);
}
