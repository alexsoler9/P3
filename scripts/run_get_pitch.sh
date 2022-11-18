#!/bin/bash
umaxnorm=${1:+-m $1}
u1norm=${2:+-u $2}
# Put here the program (maybe with path)
GETF0="get_pitch $umaxnorm $u1norm"

for fwav in pitch_db/train/*.wav; do
    ff0=${fwav/.wav/.f0}
    echo "$GETF0 $fwav $ff0 ----"
    $GETF0 $fwav $ff0 > /dev/null || (echo "Error in $GETF0 $fwav $ff0"; exit 1)
done

exit 0
