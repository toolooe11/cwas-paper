#!/usr/bin/env bash

basedir="/home2/data/Projects/CWAS"
indir="${basedir}/share/development+motion"
outdir="${basedir}/development+motion"

connectir_mdmr.R -i ${outdir}/cwas/rois_random_k3200 \
    --formula "sex + tr + age" \
    --model ${indir}/subinfo/02_details.csv \
    --factors2perm "age" \
    --permutations 1999 \
    --forks 1 --threads 8 \
    --memlimit 8 \
    --save-perms \
    --ignoreprocerror \
    perms02k_age_sex+tr.mdmr

connectir_mdmr.R -i ${outdir}/cwas/rois_random_k3200 \
    --formula "sex + tr + mean_FD + age" \
    --model ${indir}/subinfo/02_details.csv \
    --factors2perm "age,mean_FD" \
    --permutations 1999 \
    --forks 1 --threads 8 \
    --memlimit 8 \
    --save-perms \
    --ignoreprocerror \
    perms02k_age+motion_sex+tr.mdmr


# Not going to use the cwas_regress_motion dealio below

connectir_mdmr.R -i ${outdir}/cwas_regress_motion/rois_random_k3200 \
    --formula "sex + tr + age" \
    --model ${indir}/subinfo/02_details.csv \
    --factors2perm "age" \
    --permutations 1999 \
    --forks 1 --threads 8 \
    --memlimit 8 \
    --save-perms \
    --ignoreprocerror \
    perms02k_age_sex+tr.mdmr

connectir_mdmr.R -i ${outdir}/cwas_regress_motion/rois_random_k3200 \
    --formula "sex + tr + mean_FD + age" \
    --model ${indir}/subinfo/02_details.csv \
    --factors2perm "age,mean_FD" \
    --permutations 14999 \
    --forks 1 --threads 8 \
    --memlimit 8 \
    --save-perms \
    --ignoreprocerror \
    perms02k_age+motion_sex+tr.mdmr
