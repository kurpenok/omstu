pub fn decrypt(abc: &Vec<char>, s: &String, key: usize) -> String {
    let mut decrypted_s = String::new();
    let key = key % abc.len();

    for c in s.chars() {
        let decrypted_c_index = ((abc.len() as i32
            + (abc.iter().position(|symbol| *symbol == c).unwrap() as i32 - key as i32))
            % abc.len() as i32) as usize;

        decrypted_s.push(abc[decrypted_c_index]);
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

        assert_eq!(decrypt(&abc, &"bcd".to_string(), 1), "abc");
        assert_eq!(decrypt(&abc, &"yza".to_string(), 1), "xyz");
    }

    #[test]
    fn test_decrypt_russian_string() {
        let abc = RU_ABC.chars().collect::<Vec<char>>();

        assert_eq!(decrypt(&abc, &"бвг".to_string(), 1), "абв");
        assert_eq!(decrypt(&abc, &"юяа".to_string(), 1), "эюя");
    }
}
