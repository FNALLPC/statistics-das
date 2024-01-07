#!/bin/bash
CMSSW_VER=CMSSW_11_3_4

source /cvmfs/cms.cern.ch/cmsset_default.sh 
cmsrel $CMSSW_VER
pushd $CMSSW_VER/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit -b 112x
scram b -j 4
popd
tar --exclude-caches-all --exclude-vcs -zcf ${CMSSW_VER}.tar.gz -C ${CMSSW_VER}/.. $CMSSW_VER --exclude=tmp
xrdcp -f ${CMSSW_VER}.tar.gz root://cmseos.fnal.gov//store/user/cmsdas/2023/short_exercises/Statistics/${CMSSW_VER}.tar.gz
# only about 10M
