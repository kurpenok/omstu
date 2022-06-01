#pragma once

#include <cmath>

class RSA {
public:
    RSA(long long, long long);
    ~RSA();

    long long* generate_private();
    long long* generate_public();

    long long encrypt(long long, long long*&);
    long long decrypt(long long, long long*&);

private:
    long long p_;
    long long q_;
    long long n_;
    long long euler_;

    long long k_;
    long long public_exp_;
    long long private_exp_;

    long long* public_key_;
    long long* private_key_;
};

inline RSA::RSA(long long p, long long q) {
    p_ = p;
    q_ = q;

    n_ = p_ * q_;

    euler_ = (p_ - 1) * (q_ - 1);

    k_ = 2;
    public_exp_ = 3;
    private_exp_ = (1 + (k_ * euler_)) / public_exp_;
}

inline RSA::~RSA() {
    delete private_key_;
    delete public_key_;
}

inline long long* RSA::generate_private() {
    private_key_ = new long long[2];
    private_key_[0] = private_exp_;
    private_key_[1] = n_;

    return private_key_;
}

inline long long* RSA::generate_public() {
    public_key_ = new long long[2];
    public_key_[0] = public_exp_;
    public_key_[1] = n_;

    return public_key_;
}

inline long long RSA::encrypt(long long message, long long*& public_key) {
    long long e = public_key[0];
    long long n = public_key[1];

    return static_cast<long long>(std::pow(message, e)) % n;
}

inline long long RSA::decrypt(long long code, long long*& private_key) {
    long long d = private_key[0];
    long long n = private_key[1];

    return static_cast<long long>(std::pow(code, d)) % n;
}

