### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
      ## init py
      import base64
      import codecs
      import csv
      import datetime
      import glob
      import jinja2
      import json
      import platform
      import os
      import random
      import requests
      import re
      import shutil
      import string
      import StringIO
      import sys
      import textwrap
      import time
      import uuid
      import xlrd
      import yaml
      import zipfile
      
      ##
      from JinjaFilterBase import JinjaFilterBase
      from DataHelperUtils import DataHelperUtils
      from DataHelperDiceware import DataHelperDiceware

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### new_function_snippet
"""
        def __caption__(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      __caption__
            date:         lastmod="__lastmod__"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  __dreftymacid__
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''
        
          ##
          vout = jjinput.__str__()
        
          ##
          try:
            vout = vout
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        
          ##
          return vout
        ##enddef
"""

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### jinja helper JinjaFilterJJrun
if('python_region'):
###!{{{
###!- caption:  JinjaFilterJJrun
###!  date:     created="Thu Jul 16 13:21:33 2015"
###!  dreftymacid: glint_unjam_cheapen
###!  goal:     |
###!       set of default jinja filters that come with ddyaml out of the box
###!  result:   |
###!       __blank__
###!  tags:     ddyaml, filter, addon, jinja
###!  seealso: |
###!          * __blank__
###!  desc: |
###!          Currently assumes jinja2 as the templating engine for ddyaml
###!
###!
###!          
###!  wwbody: |
      class JinjaFilterJJrun(JinjaFilterBase):

        ### ------------------------------------------------------------------------
        ### begin_: 

        def jjrun_popen(self,jjinput,scmd=''):
          '''
          ##beg_func_docs
          - caption:      jjrun_popen
            date:         lastmod="2016-01-04T16:35:22"
            grp_maj:      python
            grp_med:      interop
            grp_min:      popen
            desc:         run a command using python's os.popen command
            dreftymacid:  charcoal_endanger_finger
            example:
              - 
            seealso:
              - href="smartpath://mytrybits/p/trypython2/lab2014/py/barebones_interop.py" find="sank_ceram_trim"
            detail: |
              __detail__
            dependencies:
                - import os
            params:
             - param: jjinput   ;; optional ;; command input
             - param: scmd      ;; optional ;; command input if jjinput is blank
          ##end_func_docs
          '''

          ##
          vout  = ''
          if(jjinput):
            scmd  =  jjinput
          ##;;

          ##
          try:
              # scmd = [
              #   ''
              #   ,'c:/programs/cygwin/bin/mintty.exe'
              #   ,'--exec c:/programs/cygwin/bin/bash --login -i'
              #   ,'-c "find /cygdrive/c/sm/docs/mydaydirs/2015"'
              # ]
              # scmd  =   " ".join(scmd)
              os.popen(scmd)
          except Exception as msg:
            vout = ''
            print 'EXCEPTION charcoal_endanger_finger msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;
          
          ##
          return vout
        ##enddef

      ##endclass
###!}}}
