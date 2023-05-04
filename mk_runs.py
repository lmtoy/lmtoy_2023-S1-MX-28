#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-MX-28"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["TYC_2597_735_1"] =  [ 109471, 109472,]                       # may 4

pars1 = {}

pars1["TYC_2597_735_1"] = ""

pars2 = {}

pars2["TYC_2597_735_1"] = "pix_list=-3"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
