use modulo::{inverse::get_inverse, ops::mod_add};

#[derive(Debug, PartialEq)]
pub struct DecryptResult {
    pub a: usize,
    pub b: usize,
    pub decrypted_s: String,
}

pub fn decrypt(abc: &Vec<char>, s: &String, a: usize, b: usize) -> String {
    let mut decrypted_s = String::new();

    for c in s.chars() {
        match abc.iter().position(|&symbol| symbol == c) {
            Some(c_index) => match get_inverse(a, abc.len()) {
                Some(inverse_a) => {
                    let new_c_index = inverse_a as i32 * (c_index as i32 - b as i32);
                    decrypted_s.push(abc[mod_add(0, new_c_index, abc.len())]);
                }
                None => continue,
            },
            None => decrypted_s.push(c),
        }
    }

    decrypted_s
}

#[cfg(test)]
mod test {
    use crate::{EN_ABC, RU_ABC};

    use super::*;

    #[test]
    fn test_decrypt_english_string() {
        let abc = EN_ABC.chars().collect::<Vec<char>>();

        assert_eq!(decrypt(&abc, &"ulc".to_string(), 17, 20), "abc".to_string());
        assert_eq!(decrypt(&abc, &"szg".to_string(), 7, 13), "xyz".to_string());
    }

    #[test]
    fn test_decrypt_russian_string() {
        let abc = RU_ABC.chars().collect::<Vec<char>>();

        assert_eq!(decrypt(&abc, &"удф".to_string(), 17, 20), "абв".to_string());
        assert_eq!(decrypt(&abc, &"шяё".to_string(), 7, 13), "эюя".to_string());
    }
}
