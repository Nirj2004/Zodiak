#include "ZODIAK.hpp"
#include <iostream>
int
main()
{
  constexpr size_t msg_len = 64ul;

  uint8_t* msg = static_cast<uint8_t*>(std::malloc(msg_len));
  uint8_t* out = static_cast<uint8_t*>(std::malloc(xoodyak::DIGEST_LEN));

  random_data(msg, msg_len);

  xoodyak::hash(msg, msg_len, out);

  std::cout << "Message         : " << to_hex(msg, msg_len) << std::endl;
  std::cout << "ZODIAK Digest  : " << to_hex(out, xoodyak::DIGEST_LEN)
            << std::endl;

  std::free(msg);
  std::free(out);

  return EXIT_SUCCESS;
}