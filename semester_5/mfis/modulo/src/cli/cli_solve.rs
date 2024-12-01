use crate::{
    modules::{
        ops::mod_add,
        solve::{solve_comparison, solve_comparisons_system},
    },
    SEPARATOR,
};

use super::console_read;

pub fn cli_solve(system: bool) {
    if !system {
        let a = console_read("[>] Enter number a: ").parse::<i32>();
        let b = console_read("[>] Enter number b: ").parse::<i32>();
        let m = console_read("[>] Enter modulo: ").parse::<usize>();

        if a.is_err() || b.is_err() || m.is_err() {
            println!("[-] Incorrect values!");
            return;
        }

        let m = m.unwrap();
        let a = mod_add(0, a.unwrap(), m);
        let b = mod_add(0, b.unwrap(), m);

        match solve_comparison(a, b, m) {
            Some(solutions) => println!("[+] Solutions: {:?}", solutions),
            None => println!("[-] Comparison has no solutions!"),
        }
    } else {
        let a = console_read("[>] Enter number a: ").parse::<i32>();
        let b = console_read("[>] Enter number b: ").parse::<i32>();
        let c = console_read("[>] Enter number c: ").parse::<i32>();
        let d = console_read("[>] Enter number d: ").parse::<i32>();
        let m = console_read("[>] Enter modulo: ").parse::<usize>();

        if a.is_err() || b.is_err() || c.is_err() || d.is_err() || m.is_err() {
            println!("[-] Incorrect values!");
            return;
        }

        let m = m.unwrap();
        let a = mod_add(0, a.unwrap(), m);
        let b = mod_add(0, b.unwrap(), m);
        let c = mod_add(0, c.unwrap(), m);
        let d = mod_add(0, d.unwrap(), m);

        match solve_comparisons_system(a, b, c, d, m) {
            Some(solutions) => println!("[+] Solutions: {:?}", solutions),
            None => println!("[-] Comparison has no solutions!"),
        }
    }
    println!("{}", SEPARATOR);
}
