use modulo::ops::*;

pub fn encrypt(abc: &Vec<char>, s: &String, a: usize, b: usize) -> String {
    let mut encrypted_s = String::new();

    for c in s.chars() {
        match abc.iter().position(|&symbol| symbol == c) {
            Some(c_index) => {
                encrypted_s.push(abc[mod_add(0, (a * c_index + b) as i32, abc.len())]);
            }
            None => encrypted_s.push(c),
        }
    }

    encrypted_s
}

#[cfg(test)]
mod test {
    use crate::{EN_ABC, RU_ABC};

    use super::*;

    #[test]
    fn test_encrypt_english_string() {
        let abc = EN_ABC.chars().collect::<Vec<char>>();

        assert_eq!(encrypt(&abc, &"abc".to_string(), 17, 20), "ulc");
        assert_eq!(encrypt(&abc, &"xyz".to_string(), 7, 13), "szg");
    }

    #[test]
    fn test_encrypt_russian_string() {
        let abc = RU_ABC.chars().collect::<Vec<char>>();

        assert_eq!(encrypt(&abc, &"абв".to_string(), 17, 20), "удф");
        assert_eq!(encrypt(&abc, &"эюя".to_string(), 7, 13), "шяё");
    }
}
