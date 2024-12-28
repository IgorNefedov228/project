from weightgain_brek import *
from weightgain_lun import *
from weightgain_din import *
from weightgain_sna import *
from loss_brek import *
from loss_lun import *
from loss_din import *
from loss_sna import *
from dry_brek import *
from dry_lun import *
from dry_din import *
from dry_sna import *
from question import *


if q1 == 'gain':
    brek = wbc
    lun = wlc
    din = wdc
    sna = wsc
    all = wbc + wlc + wdc + wsc
elif q1 == 'dry':
    brek = dbc
    lun = dlc
    din = ddc
    sna = dsc
    all = dbc + dlc + ddc + dsc
else:
    brek = lbc
    lun = llc
    din = ldc
    sna = lsc
    all = lbc + llc + ldc + lsc

if q1 == 'gain':
    proteine = wbp + wlp + wdp + wsp
else:
    proteine = dbp + dlp + ddp + dsp

   