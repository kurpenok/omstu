# Modular arithmetic library

#### Usage

<details>
    <summary>Add library to Cargo.toml</summary>

```toml
[dependencies]
modulo = { path = "../modulo/" }
```
</details>

<details>
    <summary>Find greater common divisor</summary>

```rust
use modulo::gcd::gcd;
use modulo::gcd::extended_gcd;

let a: usize = 6;
let b: usize = 4;

let result = gcd(a, b);
// result: 2

let coefs = BezuCoefs::new();
let result = extended_gcd(a, b, &mut coefs);
// result: 2
// coefs.alpha: 1
// coefs.beta: -1
```
</details>

<details>
    <summary>Find inverse element in ring modulo</summary>

```rust
use modulo::inverse::get_inverse;

let a: i32 = -3;
let m: usize = 5;

let inverse_a = get_inverse(a, m);
// inverse_a: 3
```
</details>

<details>
    <summary>Solving simple comparison by modulo</summary>

```rust
use modulo::solve::solve_comparison;

let a: i32 = 6;
let b: i32 = 8;
let m: usize = 10;

let solutions = solve_comparison(a, b, m);
// solutions: Some(vec![3, 8])
```
</details>

<details>
    <summary>Solving comparison system by modulo</summary>

```rust
use modulo::solve::solve_comparisons_system;

let a: i32 = 14;
let b: i32 = 8;
let c: i32 = 5;
let d: i32 = 19;
let m: usize = 32;

let solutions = solve_comparison(a, b, c, d, m);
// solutions: Some(vec![vec![13, 18]])
```
</details>
