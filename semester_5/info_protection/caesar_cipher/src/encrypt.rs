pub fn encrypt(s: String, key: u32) -> String {
    let mut encrypted_s = String::new();
    let key = key % 26;

    for c in s.chars() {
        let c_code = c as u32;
        let mut encrypted_c_code = c_code + key;
        if encrypted_c_code > 122 {
            encrypted_c_code = 96 + (encrypted_c_code - 122);
        }
        encrypted_s.push(char::from_u32(encrypted_c_code).unwrap());
    }

    encrypted_s
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_case_1() {
        assert_eq!(encrypt("abc".to_string(), 1), "bcd");
    }

    #[test]
    fn test_case_2() {
        assert_eq!(encrypt("xyz".to_string(), 1), "yza");
    }
}
