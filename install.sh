#!/bin/bash
echo "Copying accomplishments to $1"
rm -rf $1/accomplishments/ubuntu-desktop
mkdir -p $1/accomplishments/ubuntu-desktop
cp -r ./accomplishments/ubuntu-desktop/* $1/accomplishments/ubuntu-desktop/

rm -rf $1/scripts/ubuntu-desktop
mkdir -p $1/scripts/ubuntu-desktop
cp -r ./scripts/ubuntu-desktop/* $1/scripts/ubuntu-desktop/
echo "Done!"
