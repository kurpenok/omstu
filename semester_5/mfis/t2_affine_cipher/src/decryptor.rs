use modulo::invert::*;
use modulo::ops::*;

#[derive(Debug, PartialEq)]
pub struct DecryptResult {
    pub a: i32,
    pub b: i32,
    pub s: String,
}

fn decrypt_helper(abc: &Vec<char>, s: &String, a: i32, b: i32) -> DecryptResult {
    let mut decrypted_s = String::new();

    for c in s.chars() {
        match abc.iter().position(|&symbol| symbol == c) {
            Some(c_index) => match invert(a as i32, abc.len() as i32) {
                Some(inverted_a) => {
                    let c_index = c_index as i32;
                    let m = abc.len() as i32;
                    decrypted_s
                        .push(abc[mod_add(0, inverted_a * (c_index - b as i32), m) as usize]);
                }
                None => continue,
            },
            None => decrypted_s.push(c),
        }
    }

    DecryptResult {
        a: a as i32,
        b: b as i32,
        s: decrypted_s,
    }
}

pub fn decrypt(abc: &Vec<char>, s: &String, a: Option<i32>, b: Option<i32>) -> Vec<DecryptResult> {
    match (a, b) {
        (Some(a), Some(b)) => return vec![decrypt_helper(abc, s, a, b)],
        (None, None) => {
            let mut decrypted_results: Vec<DecryptResult> = Vec::new();

            for a in 0..abc.len() {
                for b in 0..abc.len() {
                    decrypted_results.push(decrypt_helper(abc, s, a as i32, b as i32));
                }
            }

            decrypted_results
        }
        _ => vec![],
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_decrypt_english_string() {
        let abc = "abcdefghijklmnopqrstuvwxyz".chars().collect::<Vec<char>>();

        assert_eq!(
            decrypt_helper(&abc, &"ulc".to_string(), 17, 20),
            DecryptResult {
                a: 17,
                b: 20,
                s: "abc".to_string()
            }
        );
        assert_eq!(
            decrypt_helper(&abc, &"szg".to_string(), 7, 13),
            DecryptResult {
                a: 7,
                b: 13,
                s: "xyz".to_string()
            }
        );
    }

    #[test]
    fn test_decrypt_russian_string() {
        let abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            .chars()
            .collect::<Vec<char>>();

        assert_eq!(
            decrypt_helper(&abc, &"удф".to_string(), 17, 20),
            DecryptResult {
                a: 17,
                b: 20,
                s: "абв".to_string()
            }
        );
        assert_eq!(
            decrypt_helper(&abc, &"шяё".to_string(), 7, 13),
            DecryptResult {
                a: 7,
                b: 13,
                s: "эюя".to_string()
            }
        );
    }
}
