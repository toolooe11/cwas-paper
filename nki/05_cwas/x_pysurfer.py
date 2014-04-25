#!/usr/bin/env python

import sys
sys.path.append("/home2/data/Projects/CWAS/share/lib/surfwrap")

import os
from os import path
from surfwrap import SurfWrap


strategy = "compcor"
scans = ["medium"]

for scan in scans:
    print "strategy: %s; scan: %s" % (strategy, scan)


    basedir = "/home2/data/Projects/CWAS/nki/cwas"
    #mname = "iq_age+sex+meanFD.mdmr"
    #mname = "iq_age+sex+meanFD+meanGcor.mdmr"
    mname = "meanGcor_iq+age+sex+meanFD.mdmr"
    cname = "cluster_correct_v05_c05"
    factor = "medium_meanGcor"    
	#factor = "FSIQ"

    ks = {
        #"roi2roi": [25, 50, 100, 200, 400, 800, 1600, 3200, 6400], 
        #"roi2vox": [25, 50, 100, 200, 400, 800, 1600, 3200, 6400], 
        #"roi2vox": [3200], 
        "vox2vox": ["voxs_fwhm08"]
    }

    for name,kset in ks.iteritems():
        print name
        for k in kset:
            print k
            # Distance Directory    
            if name == "vox2vox":
                dirname = "%s_k%s_to_k%s" % (strategy, k, k)
            elif name == "roi2vox":
                dirname = "%s_rois_random_k%04i" % (strategy, k)
            elif name == "roi2roi":
                dirname = "%s_only_rois_random_k%04i" % (strategy, k)
            else:
                raise Exception("whoops")
            distdir = path.join(basedir, scan, dirname)
        
            # Input pfile
            mdmrdir = path.join(distdir, mname)
            pfile = path.join(mdmrdir, cname, "clust_logp_%s.nii.gz" % factor)
        
            # Output oprefix
            odir = path.join(mdmrdir, cname, "images")
            if not path.exists(odir): os.mkdir(odir)
            oprefix = path.join(odir, path.basename(pfile).replace(".nii.gz", ""))
        
            # Surface Viz
            sw = SurfWrap(name=factor, infile=pfile, cbar="red-yellow", 
                          outprefix=oprefix)
            sw.run(compilation="box")
    
            # import pysurfer
            # pysurfer = reload(pysurfer)
            # SurfWrap = pysurfer.SurfWrap

    


