#!/bin/bash

sed -i y/$(printf "%s" {a..z})/$(printf "%s" {i..z} {a..h})/ test.txt
sed -i y/$(printf "%s" {i..z} {a..h})/$(printf "%s" {a..z})/ test.txt

