pub fn decrypt(s: String, key: u32) -> String {
    let mut decrypted_s = String::new();
    let key = key % 26;

    for c in s.chars() {
        let c_code = c as u32;
        let mut decrypted_c_code = c_code - key;
        if decrypted_c_code < 97 {
            decrypted_c_code = 122 - (96 - decrypted_c_code);
        }
        decrypted_s.push(char::from_u32(decrypted_c_code).unwrap());
    }

    decrypted_s
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_case_1() {
        assert_eq!(decrypt("bcd".to_string(), 1), "abc");
    }

    #[test]
    fn test_case_2() {
        assert_eq!(decrypt("yza".to_string(), 1), "xyz");
    }
}
