#!/bin/zsh

# Test script by Miccah Castorina
# Call with path to test directory, e.g. `$ ./test_directory.sh ./projects/01`

# path to HardwareSimulator.sh
hw_sim='/Users/lauratessin/recurse_center/nand2tetris/tools/HardwareSimulator.sh'

_red='\e[0;31m'
_grn='\e[0;32m'
_rst='\e[39;49m'

function compare_results {
    local have_file="$1.out"
    local want_file="$1.cmp"
    local failure_line=$(wc -l "$have_file" | cut -d' ' -f1)
    echo -e ">>> expected\n${_grn}$(sed -n ${failure_line}p "$want_file")$_rst"
    echo -e ">>> got\n${_red}$(tail -n 1 "$have_file")$_rst\n"
}

if [[ -z $1 ]]; then
    echo "please provide a directory containing *.tst files"
    exit 1
fi

cd "$1"
total_count=0
pass_count=0
fail_names=""
for file in *.tst; do
    printf "%-20s" "${file%.tst}"
    result=$($hw_sim $PWD/$file 2>&1)
    # echo $result
    if [[ $? -eq 0 ]]; then
        echo -e "${_grn}ok${_rst}"
        pass_count=$((pass_count + 1))
    elif [[ ! "$result" =~ "Comparison failure" ]]; then
        # syntax error
        echo -ne "${_red}fail: "
        echo -e "$result${_rst}" | sed -e "s#/.*/projects/##"
        fail_names="$fail_names, ${file%.tst}"
    else
        echo -e "${_red}fail${_rst}"
        compare_results "${file%.tst}"
        fail_names="$fail_names, ${file%.tst}"
    fi
    total_count=$((total_count + 1))
done

echo "========================================="
if [[ $pass_count -ne $total_count ]]; then
    echo "Failing modules: ${fail_names#, }" | fmt | sed -e '2,$s/^/                 /' | fmt
    echo -n '        '
fi
echo "Summary: $pass_count/$total_count passing"
