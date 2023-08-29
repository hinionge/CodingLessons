
# use Bash interpreter

#!/usr/bin/env bash

# Some error escapes
#set -euo pipefail


# Read the file into a variable
chapter=$(cat MDCh1.txt)

# First convert the odd dashes into something nicer to read in terminal:

chapter="${chapter//—/ -- }"

# Now a Caesar cipher, A=I etc.

echo "$chapter" | tr 'A-Za-z' 'I-ZA-Hi-za-h'