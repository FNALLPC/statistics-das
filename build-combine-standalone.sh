#!/bin/bash
# ---------------------------------------------------------
# Description: Build combine with LCG
# Created: January 2024 for CMSDAS 2024 Harrison B. Prosper
# Based on the instructions at 
# https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#standalone-compilation-with-lcg
# ---------------------------------------------------------
# Step 1: Download package
# ------

echo
echo " STEP 1: Download"
echo

rm -rf HiggsAnalysis
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit

if [ ! -d HiggsAnalysis ]; then
	echo "** HiggsAnalysis not found!"
	return
fi

echo 
echo " STEP 2: Set LCG Version"
echo 

# Step 2: Use correct LCG version (echo $LCG_VERSION)
# ------

echo "LCG VERSION: $LCG_VERSION"

cd HiggsAnalysis/CombinedLimit
 
export LCG_SETUP_OLD=`grep "cvmfs" env_lcg.sh | cut -d" " -f2`

export LCG_SETUP_NEW=`echo "$LCG_VIEW/setup.sh"`
    
echo "LCG setup: $LCG_SETUP_NEW"

sed -e "s|$LCG_SETUP_OLD|$LCG_SETUP_NEW|" env_lcg.sh > setup.sh.2
        
echo "unset CPLUS_INCLUDE_PATH" > setup.sh.1
    
cat setup.sh.1 setup.sh.2 > setup-combine.sh
    
rm -rf setup.sh.*

# Step 3: Build combine with LCG 
# ------

echo
echo " STEP 3: Build combine"
echo

source setup-combine.sh    
make clean
make LCG=1 -j2

echo
which combine
echo

echo "---------------------------------------------"
echo "To set the PATH to combine"
echo "  1. navigate to HiggsAnalysis/CombinedLimit"
echo "  2. then"
echo "       source setup-combine.sh" 
echo "---------------------------------------------"
echo ""
