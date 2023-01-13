#include "Zodiak.hpp"
extern "C"
{
    void hash(const uint8_t* const __restrict,
            const size_t,
            uint8_t* const __restrict);
    void encrypt(const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const size_t,
                 const uint8_t* const __restrict,
                 uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 uint8_t* const __restrict);
    bool decrypt(const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 const size_t,
                 const uint8_t* const __restrict,
                 uint8_t* const __restrict,
                 const uint8_t* const __restrict,
                 uint8_t* const __restrict
                 const size_t);
}
extern "C"
{
    void hash(const uint8_t* const __restrict msg,
              const size_t m_len,
              uint8_t* const __restrict digest
    )
    {
        Zodiak::hash(msg, m_len, digest);
    }
    void encrypt(
        const uint8_t* const __restrict key, 
        const uint8_t* const __restrict nonce,
        const uint8_t* const __restrict data,
        const size_t dt_len,
        const uint8_t* const __restrict text,
        uint8_t* const __restrict cipher,
        const size_t ct_len,
        uint8_t* const __restrict tag 
    )
    {
        Zodiak::encrypt(key, nonce, data, dt_len, text, cipher, ct_len, tag);
    }
    bool decrypt(
                const uint8_t* const __restrict key, 
        const uint8_t* const __restrict nonce,
        const uint8_t* const __restrict data,
        const size_t dt_len,
        const uint8_t* const __restrict text,
        uint8_t* const __restrict cipher,
        const size_t ct_len,
        uint8_t* const __restrict tag
    )
    {
        bool f = false;
        f = Zodiak::decrypt(key, nonce, tag, data, dt_len, cipher, text, ct_len);
        return f;
    }
}