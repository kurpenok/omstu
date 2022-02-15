#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

template <typename T>
void split(const std::string &s, char delimiter, T result) {
    std::istringstream iss(s);
    std::string item;

    while (std::getline(iss, item, delimiter)) {
        *result++ = item;
    }
}

std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> elements;
    split(s, delimiter, std::back_inserter(elements));
    return elements;
}

int main() {
    std::string text = "word word word1 word2";
    
    std::cout << "[>] Input string: " << text << std::endl;

    std::vector<std::string> words = split(text, ' ');

    std::set<std::string> uwords;
    for (std::string word: words) {
        uwords.insert(word);
    }
    
    std::cout << "[+] Ouput string: ";
    for (std::string uword: uwords) {
        std::cout << uword << ' ';
    }
    std::cout << std::endl;

    return 0;
}

