#!/bin/bash

THIS=$PWD

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

cd $THIS
git commit -a --amend -C HEAD
git push --force origin gh-pages

exit
