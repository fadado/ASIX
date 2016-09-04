#!/bin/bash

cd ../asix/MP4
./zip.sh
cd ../MP9
./zip.sh
cd ../../_asix

rm -rf MP[49]

mv ../asix/MP[49]/MP?.zip .

unzip -q MP4.zip
unzip -q MP9.zip

rm *.zip
