import Zodiak as zdk
import numpy as np
u8 = np.uint8
def test_hash_kat():
    with open("LWC_HASH_KAT_256.txt", "r") as fd:
        while True:
            cnt = fd.readline()
            if not cnt: break
        msg = fd.readline()
        md = fd.readline()
        cnt = int([i.strip() for i in cnt.split("=")][-1])
        msg = [i.strip() for i in msg.split("=")][-1]
        md = [i.strip() for i in md.split("=")][-1]
        msg = bytes(
            [
                int(f"0x{msg[(i << 1): ((i+1) << 1)]}", base=16)
                for i in range(len(msg) >> 1)
            ]
        )
        md = bytes(
            [
                int(f"0x{md[(i << 1): ((i+1) << 1)]}", base=16)
                for i in range(len(msg) >> 1)
            ]
        )
        digest = zdk.hash(msg)
        assert (
            md == digest
        ), f"[Zodiak Hash KAT {cnt}] expected {md}, found {digest} !"
        fd.readline()
        count = cnt
    print(f"[test] passed {count} -many Zodiak Hash KAT(s)")
def test_aead_kat():
    count = 0
    with open("LWC_AEAD_KAT_128_128.txt", "r") as fd:
        while True:
            cnt = fd.readline()
            if not cnt:
                break
            key = fd.readline()
            nonce = fd.readline()
            pt = fd.readline()
            ad = fd.readline()
            ct = fd.readline()
            cnt = int([i.strip() for i in cnt.split("=")][-1])
            key = [i.strip() for i in key.split("=")][-1]
            nonce = [i.strip() for i in nonce.split("=")][-1]
            pt = [i.strip() for i in pt.split("=")][-1]
            ad = [i.strip() for i in ad.split("=")][-1]
            tag = [i.strip() for i in ct.split("=")][-1][-32:]


            key = int(f"0x{key}", base=16).to_bytes(16, "big")

            nonce = int(f"0x{nonce}", base=16).to_bytes(16, "big")
            
            pt = bytes(
                [
                    int(f"0x{pt[(i << 1): ((i+1) << 1)]}", base=16)
                    for i in range(len(pt) >> 1)
                ]
            )

            ad = bytes(
                [
                    int(f"0x{ad[(i << 1): ((i+1) << 1)]}", base=16)
                    for i in range(len(ad) >> 1)
                ]
            )

            tag = bytes(
                [
                    int(f"0x{tag[(i << 1): ((i+1) << 1)]}", base=16)
                    for i in range(len(tag) >> 1)
                ]
            )

            cipher, tag_ = zdk.encrypt(key, nonce, ad, pt)
            flag, text = zdk.decrypt(key, nonce, tag_, ad, cipher)

            assert (
                pt == text and flag
            ), f"[Zodiak KAT {cnt}] expected 0x{pt.hex()}, found 0x{text.hex()} !"

            assert (
                tag == tag_
            ), f"[Zodiak KAT {cnt}] expected tag 0x{tag.hex()}, found 0x{tag_.hex()}"


            fd.readline()

            count = cnt

    print(f"[test] passed {count} -many Zodiak KAT(s)")


if __name__ == "__main__":
    print("Run Zodiak Known Answer Tests using `pytest` !")