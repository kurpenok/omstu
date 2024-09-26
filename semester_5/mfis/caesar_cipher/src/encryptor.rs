pub fn encrypt(abc: &Vec<char>, s: &String, key: usize) -> String {
    let mut encrypted_s = String::new();
    let key = key % abc.len();

    for c in s.chars() {
        let c_position = abc.iter().position(|symbol| *symbol == c);
        if c_position.is_none() {
            encrypted_s.push(c);
        } else {
            let encrypted_c_index = (c_position.unwrap() + key) % abc.len();
            encrypted_s.push(abc[encrypted_c_index]);
        }
    }

    encrypted_s
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_encrypt_english_string() {
        let abc = "abcdefghijklmnopqrstuvwxyz".chars().collect::<Vec<char>>();

        assert_eq!(encrypt(&abc, &"abc".to_string(), 1), "bcd");
        assert_eq!(encrypt(&abc, &"xyz".to_string(), 1), "yza");
    }

    #[test]
    fn test_encrypt_russian_string() {
        let abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            .chars()
            .collect::<Vec<char>>();

        assert_eq!(encrypt(&abc, &"абв".to_string(), 1), "бвг");
        assert_eq!(encrypt(&abc, &"эюя".to_string(), 1), "юяа");
    }
}
