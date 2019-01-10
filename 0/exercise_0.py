#!/usr/bin/env python
#-------------------------------------------------------------
# File: exercise_0.py
# Description: A Python/PyRoot/RooFit tutorial!
#              Implementation of Glen Cowan's exercise:
#
# Fit an exponential to data
#
# Created: 4 June 2013 Harrison B. Prosper
#          INFN SOS 2013, Vietri sul Mare, Italy
#
#    Adapted for CMSDAS 2016, LPC Fermilab
#
# Python notes
# ------------
# 1. The first line of this file tells the operating system which program
#    is to be used to interpret the instructions that follow. You can
#    make this program executable with the command
#
#          chmod +x exercise_0.py
#
#    and execute the program using
#
#          ./exercise_0.py
#
# 2. PLEASE TAKE NOTE: Python uses indentation to create program blocks.
#    Semicolons are not needed as in C++. It is convenient to use
#    an editor such as emacs that is Python-aware. This will help
#    minimize indentation errors.
#
# 3. Python handles pointers for you! Also use "." as in
#
#           TMath.Prob
#
#    instead of TMath::Prob
#
# 4. There are wwo basic ways to load program modules into memory, e.g.:
#
#          import os
#    and
#          from string import replace
#
# 5. Strings can be initialized either with single or double quotes,
#    'ABC' or "ABC". This is useful when "ABC" needs to be embedded within
#    a string. Use \ to continue strings onto a new line:
#
#            poem = 'The time has come the walrus said\n'\
#                   'To speak of many things'
#
# 6. WARNING: Python uses dynamic typing, which means that the type of
#    a variable is detemined at runtime by its value. Consequently,
#    a variable's type is, well, variable!
#
#    x = 0     x is an integer
#    x = 0.0   x is now a float
#    x ='0'    x is now a string
#
#    Also (in Python 2.7.X) beware of
#
#    x = 42
#    y = x / 84
#
#    The answer will be y = 0 because x is an integer!
#
# 7. Insert sys.exit() to stop program at any line. Useful for
#    debugging.
#
#-------------------------------------------------------------
# Load the operating system and system modules into memory
import os,sys

# Load the sleep function from the time module
from time import sleep

# Import all functions from the math module if you are sure there
# will be no name collisions
from math import *

# Load everything that is in PyROOT. This is fine if, again, you are
# sure there are no name collisions between PyROOT and the names
# in other modules, otherwise use the syntax:
# example:
#  from ROOT import TCanvas, TFile, kBlue
#
from ROOT import *
#-------------------------------------------------------------
# The main function can be called whatever you like. We follow
# C++ and call it main..dull, but clear!
def main():

    # We shall use a package called RooFit, compiled with ROOT,
    # in order to fit an exponential function to data.
    #
    # Suppress all messages except those that matter
    msgservice = RooMsgService.instance()
    # If a crash occurs, or things look strange,
    # comment out next line to find out more information
    # about the problem.
    msgservice.setGlobalKillBelow(RooFit.FATAL)

    # The most convenient way to use RooFit/RooStats is to 
    # make a workspace so that we can use its factory method
    wspace = RooWorkspace('CMSDAS16')

    #-----------------------------------------------------
    # Create a double-exponential model
    #-----------------------------------------------------
    # The observable is x and lies in the range [0, 20]
    xmin = 0.0 # note this is a float
    xmax =20.0 # and so is this
    
    # Use the factory method of the RooWorkspace object, just
    # created, to create an object called x that represents the
    # observable.
    # syntax:
    #        <name>[value, min-value, max-value]
    #
    # We are using Python's ability to write numbers into strings,
    # which is modeled on C
    wspace.factory('x[0,%f,%f]' % (xmin, xmax))

    #---------------------------
    # Set the NUMBER OF BINS,
    # either for display purposes
    # or for the binned fit.
    #---------------------------
    M = 15 
    wspace.var('x').setBins(M)

    # The parameters of the model are a, b, c
    wspace.factory('a[0.4, 0.0,   1.0]')
    wspace.factory('b[3.0, 0.01, 20.0]')
    wspace.factory('c[9.0, 0.01, 20.0]')
    parameters = ['a', 'b', 'c']
    
    # NUMBER OF PARAMETERS
    P = len(parameters)
    
    # The model to be fitted, called "model", is defined
    # by a probability density function (pdf) of the form
    #
    #   p(x|a, b, c) = a*exp(-x/b)/b + (1-a)*exp(-x/c)/c
    #
    # The syntax for creating a pdf, here a user-defined pdf using
    # the class RooGenericPdf, is:
    #
    # GenericPdf::<user-defined-name>("<function>", {...})
    #
    # where we always drop the "Roo" prefix. Note use of braces {..}
    # in the above to specify a list of variables
    # (modeled in RooFit by the RooArgList class).
    #
    # POWERFUL TIP: a function can be a call to a C++
    # function (with double and int arguments), compiled
    # using
    #
    #  gROOT.ProcessLine(open('<function>.cc').read())
    #
    # and made known to Python using
    #
    #  from ROOT import <function>
    #
    # The Python file open object reads the specified file as one
    # continuous string, which is then passed to ProcessLine. The
    # latter compiles it using a just-in-time compiler (in Root 6).
    # Since Root 6 uses a real compiler (rather than an interpreter),
    # the syntax of your C++ code must conform to standard C++.
    #
    # If you need to make the compiler and linker happy by including
    # headers and libraries other the the default set provided by ROOT,
    # first do
    #
    #   gSystem.AddInlcudePath('-I<path1> ...')
    #   gSystem.AddLinkedLibs('-L<libdir> -l<library> ...')
    #
    # before calling gROOT.ProcessLine

    # Note use of "\" continuation markers below

    # Here is a direct way to create the model:
    #
    # wspace.factory('GenericPdf::model'\
    #                '("a*exp(-x/b)/b + (1-a)*exp(-x/c)/c",'\
    #                '{x,a,c,c})')

    # and here is a way to do the same thing via a C++ function:
    
    gROOT.ProcessLine(open('models.cc').read())
    from ROOT import dbexp
    wspace.factory('GenericPdf::model("dbexp(x,a,b,c)", {x,a,b,c})')

                   
    # So far, the "model" is known only to the RooFit workspace.
    # Make the model known to Python also
    model = wspace.pdf('model')

    #----------------------------------------------------
    # now we generate some data from the model,
    # then try to fit the latter to these data
    #----------------------------------------------------
    # define the set obs = (x)
    wspace.defineSet('obs', 'x')

    # make the set obs known to Python
    obs  = wspace.set('obs')

    # now, generate data
    T = 400 # number of data to generate
    data = model.generate(obs, T)
    
    #----------------------------------------------------
    # Part 1: do an unbinned fit to data
    #----------------------------------------------------
    print "="*80
    print "\t\t unbinned fit to data"
    print "="*80

    # Obvious, right?!! :)
    swatch = TStopwatch()
    swatch.Start()

    # If more control is needed, you can call RooMinuit
    # directly, which is an interface to Minuit.
    # Here, we are happy to use the simpler interface "fitTo".
    # Remember to save the results of the fit
    results = model.fitTo(data, RooFit.Save())
    print "real time: %10.3f s" % swatch.RealTime()

    # Let's see what we get
    print "="*80
    results.Print()

    # Print correlation matrix as a matrix.
    # Note use of "," at the end of the print statement
    # to suppress a newline
    print "\tcorrelation matrix"
    print "%10s" % "",
    for v in parameters:
        print "%10s" % v,
    print  # use this to print a newline character
    for v1 in parameters:
        print "%-10s" % v1, # first print label and suppress a newline
        for v2 in parameters:
            cor = results.correlation(v1, v2)
            print '%10.3f' % cor,
        print # print a newline character

    #---------------------------
    # plot
    #---------------------------
    # This is how RooFit makes plots. Alas, it is not as
    # intuitive as it could have been!
    #
    # We wish to plot the distribution of the data and
    # superimpose the fitted model as a function of the
    # observable x.
    #
    # In RooFit, one does proceeds as follows:
    # 1. create a frame pertaining to x (which we call xframe)
    # 2. set the frame's attributes, of which there are many
    # 3. tell the data to place a plot of themselves on xframe
    # 4. tell the model to place a plot of itself on xframe
    # 5. tell the model to place its parameters on xframe
    # 6. tell the xframe to draw itself on the active canvas

    xframe = wspace.var('x').frame()
    xframe.SetMinimum(0)     # set minimum y-axis value 
    xframe.SetMaximum(100)   # set maximum y-axis value
    data.plotOn(xframe)
    model.plotOn(xframe)
    model.paramOn(xframe)

    # If you have trouble making the plot look exactly as you
    # wish it to look, try drawing an empty Root histogram
    # first in order to define the plotting area, then Draw
    # xframe using the "same" option.
    #
    # Place upper lefthand corner of canvas at pixel position (10, 10)
    # of your screen. (0,0) is the upper lefthand corner.

    c1 = TCanvas('fig_unbinnedFit', 'fit', 10, 10, 500, 500)
    xframe.Draw()
    c1.SaveAs('.png')

    #---------------------------------------------------
    # Part 2: do a binned fit
    #---------------------------------------------------
    # Bin the data using RooDataHist

    # note use of set obs, created above, to tell
    # RooDataHist the variable(s) with respect to
    # which the data are to be binned. the number of
    # bins is obtained from the bin count attribute of "x"
    # (see above)
    hdata = RooDataHist('hdata', 'binned data', obs)
    hdata.add(data)  # add the data to the RooDataHist and bin them
    print "="*40
    hdata.Print('verbose')
    print "="*40

    # Do a multinomial fit to the binned data by
    # turning off extended likelihood mode. If you
    # want a multi-Poisson fit, change False to True.
    # (If interested, ask what all this means!)
    results2 = model.fitTo(hdata,
                           RooFit.Save(),
                           RooFit.Extended(False))
    results2.Print()

    # Plot results of fit on a different frame
    c2 = TCanvas('fig_binnedFit', 'fit',
                 515, 10, 500, 500)

    xframe2 = wspace.var('x').frame()
    xframe2.SetMaximum(0)
    xframe2.SetMaximum(100)
    hdata.plotOn(xframe2)
    model.plotOn(xframe2)
    model.paramOn(xframe2)
    xframe2.Draw()
    c2.SaveAs('.png')
    print "="*80

    #---------------------------------------------------
    # Part 3: Let's do a bit of statistics. We shall
    # compute two goodness-of-fit (gof) measures X and Y
    #---------------------------------------------------
    # Since we have binned data, we need to create an
    # integral to integrate the model over a each x-bin
    # so that we can compare the expected count in a given
    # bin with the observed count in that bin.
    #
    # 1. Define the set of variables over which to
    # normalize the integral
    normSet = RooFit.NormSet(obs) 

    # 2. Define a range variable, call it x-bin, to
    # represent the bin boundaries.
    wspace.var('x').setRange('x-bin', xmin, xmax)

    # 3. Create integral
    integral = model.createIntegral(obs,
                                    normSet,
                                    RooFit.Range('x-bin'))

    # 4. We now compute two gof measures (with the
    # restriction that the observed count N_i > 5)
    #     i.    X = sum_i=1^M (N_i - n_i)^2 / n_i,
    #
    #    where n_i = int_bin_i f(x; theta_hat) dx
    #
    #     ii.   Y = -2 ln p(N | n) / p(N | N),
    #
    # where p(N | n) is a multinomial likelihood; N denotes the counts
    # N_1,...N_M and n denotes the mean counts. Note that n_i is
    # evaluated at theta = theta_hat, that is, at the maximum
    # likelihood (ML) estimates of the parameters of the model,
    # here a, b, and c.
    #
    # Let H_0 be the hypothesis that theta_0 are the true values
    # of the parameters theta. In practice, we estimate theta_0 using
    # ML and approximate theta_0 by theta_hat.
    #
    # According to Wilks' theorem (1938), the quantity X has
    # (asymptotically) a chi-squared distribution of N - 1 - P
    # degrees of freedom, where
    #   N - number of bins
    #   P - number of fitted parameters
    #
    # Interestingly, Y follows the same distribution asymptotically.
    #
    # Procedure:
    #   loop over bins
    #      compute integral over bin to obtain n_i
    #      accumulate X and Y with restriction that N_i > 5
    #
    #   compute p-value = Pr[X > X_obs]
    #           p-value = Pr[Y > Y_obs]
    #
    
    # Find bin width. Use float function to make sure we have
    # a float in the numerator to avoid truncation.
    dx = float(xmax-xmin)/M
    X = 0.0
    Y = 0.0
    total = 0.0 # to check the total integral (should be = T)
    print
    print "%5s\t%10s %5s %10s" % ('', 'binlow', "count", "mean")

    # range(M) = [0, 1,...M-1]
    K = 0 # count number of bins with N_i > 5
    for ii in range(M):
        # Get count in bin ii
        # Yes, this is not as tidy as it could have been!
        ibin = hdata.get(ii)   # get object that models iith bin
        Ni   = hdata.weight()  # get bin content (count)

        # Set the bin boundaries in our previously created
        # range object
        x = xmin + ii * dx
        wspace.var('x').setRange('x-bin', x, x+dx)

        # Compute the integral, with respect to x, over current
        # bin and scale result by the total observed count. This
        # gives us the mean count in current bin
        ni = T * integral.getVal()
        print "%5d\t%10.3f %5d %10.1f" % (ii+1, x, Ni, ni)
        
        total += ni
        if Ni < 5: continue
        
        # Accumulate X and Y
        K += 1
        X += (Ni - ni)**2 / ni
        Y += Ni * log(ni/Ni) 

    # Complete calculation of Y
    Y *= -2

    # 5. Assuming we are in asymptotia, compute
    #    p-value = Int_Y^infinity p(chi^2, ndf) dchi^2
    # where p(chi^2, ndf) is the chi2 density of ndf
    # degrees of freedom

    ndf    = K-P-1  # number of degrees of freedom
    
    if ndf > 0:
        pvalueX = TMath.Prob(X, ndf)
        pvalueY = TMath.Prob(Y, ndf)
    else:
        pvalueX = 1.0
        pvalueY = 1.0
    print "="*80
    print "Int p(x|xi) dx =%6.1f\n" % total

    print "ChiSq/ndf = %6.1f/%d (using X)" % (X, ndf)
    print "p-value   = %9.4f\n" % pvalueX
       
    print "ChiSq/ndf = %6.1f/%d (using Y)" % (Y, ndf)
    print "p-value   = %9.4f" % pvalueY

    sleep(8)
#------------------------------------------------------------------
try:
    main()
except KeyboardInterrupt:
    print
    print "ciao!"
    print



