#!/bin/bash

# Script for ease of execution of Known Answer Tests against Zodiak implementation

# generate shared library object
make lib

# ---

mkdir -p tmp
pushd tmp

# download compressed NIST LWC submission of Zodiak
wget -O Zodiak.zip https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-submissions/Zodiak.zip
# uncomress
unzip Zodiak.zip

# copy Known Answer Tests outside of uncompressed NIST LWC submission directory
cp Zodiak/Implementations/crypto_hash/Zodiakround3/LWC_HASH_KAT_256.txt ../
cp Zodiak/Implementations/crypto_aead/Zodikround3/LWC_AEAD_KAT_128_128.txt ../

popd

# ---

# remove NIST LWC submission zip
rm -rf tmp

# move Known Answer Tests to execution directory
mv LWC_HASH_KAT_256.txt wrapper/python/
mv LWC_AEAD_KAT_128_128.txt wrapper/python/

# ---

pushd wrapper/python

# run tests
pytest -v

# clean up
rm LWC_*_KAT_*.txt

popd

make clean

# ---