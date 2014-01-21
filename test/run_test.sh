cd `dirname $0`
./fast-upstream.py | ../non_blocking_pipe ./slow-downstream.py
