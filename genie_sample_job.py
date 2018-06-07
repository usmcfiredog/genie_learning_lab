'''
Sample Genie Job File
'''

# Author
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2018, Cisco Systems Inc.'
__contact__ = ['asg-genie-support@cisco.com']
__date__= 'June 2018'


# ATS & Genie
from ats.datastructures.logic import And, Not, Or
from genie.harness.main import gRun


def main(runtime):

    gRun(mapping_datafile='/genie_tests/mapping_datafile.yaml',
         trigger_uids=And('TriggerClearBgpNeighbor'),
         verification_uids=And('Verify_BgpAllNeighbors'),
         )
