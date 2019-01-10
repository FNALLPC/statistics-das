#!/usr/bin/env python
#-------------------------------------------------------------
# File: exercise_1.py
# Description: Analyze the following Run I CMS H -> 4l data:
#
#   N        = 25
#   b_hat_zz =  6.8 +/- 0.3
#   b_hat_zx =  2.6 +/- 0.4
#   s_hat    = 17.3 +/- 1.3 (mH = 125 GeV)
#            = 19.6 +/- 1.3 (mH = 126 GeV)
#
# which pertains to data in the range 121.5 <= mH <= 130.5 GeV
# for 7 and 8 TeV data.
#
# Created: 18-Dec-2015 CMSDAS 2016, LPC Fermilab HBP
#-------------------------------------------------------------
import os,sys,re
from time import sleep
from math import *
from ROOT import *
#-------------------------------------------------------------
def check(o, message):
    if o == None:
        sys.exit(message)
#-------------------------------------------------------------        
def createWorkspace(wsname, wsfilename):
    # The most convenient way to use RooFit/RooStats is to 
    # make a workspace so that we can use its factory method
    wspace = RooWorkspace(wsname)

    #-----------------------------------------------------
    # Create parameters
    #
    # Use the factory method of the RooWorkspace to create
    # parameters
    #
    # syntax:
    #        <name>[value, min-value, max-value]
    #-----------------------------------------------------
    # observations
    params = [('N',       25,     0,  50),
    # ZZ background estimate        
              ('b_hat_zz', 6.8,   0,  15),
              ('db_zz',    0.3,   0,   5),
    # Z+X background estimate
              ('b_hat_zx', 2.6,   0,  15),
              ('db_zx',    0.3,   0,   5),
    # signal estimate (mH=125 GeV)       
              ('s_hat',   17.3,   0,  25),
              ('ds',       1.3,   0,   5),
    # nuisance parameters
              ('b_zz',    6.8,    0,  15),
              ('b_zx',    2.6,    0,  10),
              ('s',      17.3,    0,  25),
    # parameter of interest
              ('mu',      1.0,    0,   4)]

    for t in params:
        cmd = '%s[%f, %f, %f]' % t
        wspace.factory(cmd)        
    wspace.var('mu').SetTitle('#mu')

    # fix all background and signal parameters
    for t in params[1:-4]:
        name = t[0]
        print '=> make %8s = %5.1f constant' % (name,
                                                wspace.var(name).getVal())
        wspace.var(name).setConstant()

    #-----------------------------------------------------
    # Create expressions
    #
    # syntax:
    #        expr::<name>("expression", var1, var2, ...)
    #-----------------------------------------------------
    express = ['B_zz("(b_hat_zz/db_zz)^2", b_hat_zz, db_zz)',
               'tau_zz("b_hat_zz/db_zz^2", b_hat_zz, db_zz)',
               
               'B_zx("(b_hat_zx/db_zx)^2", b_hat_zx, db_zx)',
               'tau_zx("b_hat_zx/db_zx^2", b_hat_zx, db_zx)',
                              
               'S("(s_hat/ds)^2",   s_hat, ds)',
               'tau_s("s_hat/ds^2", s_hat, ds)',

               'tau_zzb_zz("tau_zz*b_zz", tau_zz, b_zz)',
               'tau_zxb_zx("tau_zx*b_zx", tau_zx, b_zx)',
               'tau_ss("tau_s*s", tau_s, s)',
               'n("mu*s + b_zz + b_zx", mu, s, b_zz, b_zx)']
        
    for t in express:
        cmd = 'expr::%s' % t
        wspace.factory(cmd)

    print '\neffective counts and scale factors'
    print 'B_zz = %8.2f, tau_zz = %8.2f' % (wspace.function('B_zz').getVal(),
                                            wspace.function('tau_zz').getVal())

    print 'B_zx = %8.2f, tau_zx = %8.2f' % (wspace.function('B_zx').getVal(),
                                            wspace.function('tau_zx').getVal())

    print 'S    = %8.2f, tau_s  = %8.2f' % (wspace.function('S').getVal(),
                                            wspace.function('tau_s').getVal())

    #-----------------------------------------------------
    # Create pdfs
    #
    # syntax:
    #        pdf_name::<name>(var1, var2, ...)
    #
    # where the "Roo" prefix is dropped in pdf_name, e.g.
    #-----------------------------------------------------
    pdfs = [('Poisson', 'pN',    '(N, n)'),
            # allow non-integer B_zz
            ('Poisson', 'pB_zz', '(B_zz, tau_zzb_zz, 1)'), 
            ('Poisson', 'pB_zx', '(B_zx, tau_zxb_zx, 1)'),
            ('Poisson', 'pS',    '(S,    tau_ss,     1)')]

    prodpdf = ''
    for t in pdfs:
        wspace.factory('%s::%s%s' % t)
        name = t[1]
        prodpdf += "%s, " % name
    prodpdf = prodpdf[:-2] # remove last ", "
    
    # multiply the pdfs together. use upper case PROD to
    # do this
    wspace.factory('PROD::model(%s)' % prodpdf)

    # create a prior, since one is needed in Bayesian
    # calculations
    wspace.factory('Uniform::prior({mu, s, b_zz, b_zx})')

    #-----------------------------------------------------
    # Define a few useful sets. Now we need to decide
    # whether or not to include B and S in the set obs of
    # observations. 
    #-----------------------------------------------------
    sets = [('obs',  'N'),           # observations
            ('poi',  'mu'),          # parameter of interest
            ('nuis', 's,b_zz,b_zx')] # nuisance parameters (leave no spaces)
    for t in sets:
        name, parlist = t
        wspace.defineSet(name, parlist)
    
    #-----------------------------------------------------        
    # create a dataset
    #-----------------------------------------------------    
    data = RooDataSet('data', 'data', wspace.set('obs'))
    data.add(wspace.set('obs'))
    # import dataset into workspace
    # need last argument to workaround a PyROOT "feature".
    # the last argument ensures the correct version of
    # the import method is called.
    getattr(wspace, 'import')(data, RooCmdArg())
        
    #-----------------------------------------------------
    # Create model configuration. This is needed for the
    # statistical analyses
    #-----------------------------------------------------
    cfg = RooStats.ModelConfig('cfg')
    cfg.SetWorkspace(wspace)
    cfg.SetPdf(wspace.pdf('model'))
    cfg.SetPriorPdf(wspace.pdf('prior'))
    cfg.SetParametersOfInterest(wspace.set('poi'))
    cfg.SetNuisanceParameters(wspace.set('nuis'))

    # import model configuration into workspace
    getattr(wspace, 'import')(cfg)

    wspace.Print()
    
    # write out workspace
    wspace.writeToFile('single_count.root')
#------------------------------------------------------------------
def analyzeWorkspace(wsname, wsfilename):

    # Open workspace file
    wsfile = TFile(wsfilename)
    if not wsfile.IsOpen():
        sys.exit("*** can't open file %s" % wsfilename)

    # Get workspace
    wspace = wsfile.Get(wsname)
    check(wspace, "*** can't access workspace %s" % wsname) 

    # Get data
    data = wspace.data('data')
    check(data, "*** can't access workspace data")

    # Get model configuration    
    cfg  = wspace.obj('cfg')
    check(cfg, "*** can't access model configuration cfg")

    #-----------------------------------------------------    
    # Fit model to data
    #-----------------------------------------------------
    results = wspace.pdf('model').fitTo(data, RooFit.Save())
    results.Print()
    
    #-----------------------------------------------------    
    # Compute interval based on profile likelihood
    #-----------------------------------------------------
    # suppress some (apparently) innocuous warnings
    msgservice = RooMsgService.instance()
    msgservice.setGlobalKillBelow(RooFit.FATAL)
        
    print 'compute interval using profile likelihood'
    plc = RooStats.ProfileLikelihoodCalculator(data, cfg)
    CL  = 0.683
    plc.SetConfidenceLevel(CL)
    plcInterval= plc.GetInterval()
    lowerLimit = plcInterval.LowerLimit(wspace.var('mu'))
    upperLimit = plcInterval.UpperLimit(wspace.var('mu'))

    print '\tPL %4.1f%s CL interval = [%5.2f, %5.2f]' % \
      (100*CL, '%', lowerLimit, upperLimit)

    # compute an 95% upper limit on mu by
    # computing a 90% central interval and
    # ignoring the lower limit
    CL = 0.90
    plc.SetConfidenceLevel(CL)
    plcInterval = plc.GetInterval()
    upperLimit = plcInterval.UpperLimit(wspace.var('mu'))

    CL = 0.95
    print '\tPL %4.1f%s upper limit = %5.2f\n' % \
      (100*CL, '%', upperLimit)      
      
    plcplot = RooStats.LikelihoodIntervalPlot(plcInterval)
    plccanvas = TCanvas('fig_PL', 'plc', 10, 10, 400, 400)
    plcplot.Draw()
    plccanvas.Update()
    
    #-----------------------------------------------------    
    # Compute interval based on Bayesian calculator
    #-----------------------------------------------------
    print 'compute interval using Bayesian calculator'
    bc = RooStats.BayesianCalculator(data, cfg)
    CL  = 0.683
    bc.SetConfidenceLevel(CL)
    bcInterval = bc.GetInterval()
    lowerLimit = bcInterval.LowerLimit()
    upperLimit = bcInterval.UpperLimit()

    print '\tBayes %4.1f%s CL interval = [%5.2f, %5.2f]' % \
      (100*CL, '%', lowerLimit, upperLimit)

    # calculate posterior density at 50 points
    print "\t\t...be patient...!"
    bc.SetScanOfPosterior(50)
    bcplot = bc.GetPosteriorPlot()
    bccanvas = TCanvas('fig_Bayes', 'Bayes', 500, 10, 850, 400)
    bccanvas.Divide(2, 1)
    bccanvas.cd(1)
    bcplot.Draw()
    bccanvas.Update()

    # compute an 95% upper limit on mu
    CL  = 0.950
    bc.SetConfidenceLevel(CL)
    # 0   = upper limit
    # 0.5 = central limits (default)
    # 1   = lower limit
    bc.SetLeftSideTailFraction(0)
    bcInterval = bc.GetInterval()
    upperLimit = bcInterval.UpperLimit()

    print '\tBayes %4.1f%s upper limit = %5.2f\n' % \
      (100*CL, '%', upperLimit)      

    # calculate posterior density at 50 points
    bc.SetScanOfPosterior(50)
    bcplot2 = bc.GetPosteriorPlot()
    bccanvas.cd(2)
    bcplot2.Draw()
    bccanvas.Update()

    # save canvases
    plccanvas.SaveAs('.png')
    bccanvas.SaveAs('.png')
    
    sleep(5)  
#------------------------------------------------------------------
def main():
    # Suppress all messages except those that matter
    msgservice = RooMsgService.instance()
    msgservice.setGlobalKillBelow(RooFit.WARNING)
    print "="*80

    if len(sys.argv) < 2:
        createWorkspace('CMSDAS16', 'single_count.root')
    else:
        analyzeWorkspace('CMSDAS16', 'single_count.root')

#------------------------------------------------------------------
try:
    main()
except KeyboardInterrupt:
    print
    print "ciao!"
    print



