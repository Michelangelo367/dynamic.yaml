# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Mon Jan 25 08:07:51 2016"
###     last: lastmod="Mon Jan 25 08:07:51 2016"
###     tags: python, ddyaml, runner
###     dreftymacid: "sue_wireworm_venusian"
###     lastupdate:  ""
###     filetype: "py"
###     seealso: |
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"
###     desc: |
###         * TODO ;; ff_resolvepath_read ff_resolvepath_path -- why keep both of these?
### <end-file_info>

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
  ## init py
  import base64
  import codecs
  import csv
  import json
  import platform
  import markdown
  import random
  import requests
  import shutil
  import StringIO
  import time
  import uuid
  import xlrd
  import zipfile
  import textwrap
  import string
  import sys
  import jinja2
  import glob
  import datetime
  import re
  import os
  import yaml
  import zipfile
  from collections import defaultdict

  ## pprint
  import pprint
  oDumper = pprint.PrettyPrinter(indent=4);
  ## oDumper.pprint( directives )
  ## ddyaml
  import JinjaFilterDynamicYAML

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### DynamicYAML
if('python_region'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Thu Jul 16 13:22:13 2015"
###!  dreftymacid: vadodara_glen_bird
###!  goal:     |
###!       __blank__
###!  result:   |
###!       __blank__
###!  tags:     __tags__
###!  seealso: |
###!          * __blank__
###!  desc: |
###!          __desc__
###!  wwbody: |
      class DynamicYAML(object):

        ##
        def __init__(self,options={},**kwargs):

          ## init defaults (TODO ;; code refactor use self.options instead of options)
          self.JFiltMain  = JinjaFilterDynamicYAML.JinjaFilterDynamicYAML()
          self.metadata   = {}
          self.options    = {}
          self.options['ddyaml_end_marker']         = '__yaml__'
          self.options['ddyaml_process_twopass']        = True
          ## support for jinja2.FileSystemLoader ;;
          self.options['filesystemloader_paths']        = []
          self.options['jinja2_globals']                = {}

          ## bring in any globals
          try:
            for item in options['globals']:
              self.options['jinja2_globals'][item[0]] = item[1]
          except:
            pass
          ##;;

          ## jinja2_globals
          if(not 'debugging_alerts_01'):
            print "### nicer_simply_haze ------------------------------------------------------------------------"
            print self.options['jinja2_globals']
          ##;;

          ## allow for overriding defaults
          for tmpname, tmpvarr in kwargs.items():
              self.options[tmpname] = tmpvarr
          ##;;

          ##
          # self.metadata['zipfile_aod_table']      = []
          # self.metadata['directives_aod_table']   = []
          self.metadata['directives_meta_table']  = []
          ##;;

          ##
          self.options['block_start_string'   ] = options.get('block_start_string'    , '{%')
          self.options['block_end_string'     ] = options.get('block_end_string'      , '%}')
          self.options['variable_start_string'] = options.get('variable_start_string' , '{{')
          self.options['variable_end_string'  ] = options.get('variable_end_string'   , '}}')
          self.options['comment_start_string' ] = options.get('comment_start_string'  , '{#')
          self.options['comment_end_string'   ] = options.get('comment_end_string'    , '#}')
          ##;;

          ##
          self.primaryYamlPath    =   options.get('path', '')          ## primaryYamlPath
          self.addonFilters       =   options.get('addonFilters', [])  ## addonFilterClasses
          ##
          if(self.primaryYamlPath.__str__() != ''):
            self.ffpath_main  =   self.primaryYamlPath.__str__()
            self.ffpath_norm  =   "/".join( self.ffpath_main.split("\\") )
            self.ffpath_pdir  =   "/".join( self.ffpath_norm.split("/")[0:-1] )
            self.ddffpath = {
              'main': self.ffpath_main,
              'norm': self.ffpath_norm,
              'pdir': self.ffpath_pdir,
            }
          elif(True):
            sgtemp = ("""
            \n## primaryYamlPath file not specified or unreachable
            """)
            ## print sgtemp

          ## self settings
          if(not 'debugging_alerts_01'):
            print "### intently_grins_lament ------------------------------------------------------------------------"
            oDumper.pprint( self.options )
            print '''
            ## self.ddffpath
            main:   {main}
            norm:   {norm}
            pdir:   {pdir}
            '''.format(** self.ddffpath )
          ##;;

        ##enddef

        def provision_jinja2_environment(self):
          '''
          provision a jinja2 environment
          this is a prerequisite for rendering jinja2 output
          '''
          ## init jinja_environment
          self.Environment = jinja2.Environment(
            extensions=[
              'jinja2.ext.do',
              'jinja2.ext.loopcontrols',
              ]
            ## bkmk001
            ,loader=jinja2.FileSystemLoader( self.options['filesystemloader_paths'] )
            #,finalize=self.oenv_finalize
            )
          self.oenv = self.Environment
          ##;;

          # print "### ------------------------------------------------------------------------"
          # print "bkmk001 :: symbiote_security_dna"
          # print self.oenv.loader.list_templates()

          ## init jinja_globals
          ## supports variables that are accessible to every jinja template
          #self.oenv.globals = {"noop" : ""}
          try:
             for ddkey in self.options['jinja2_globals']:
                 self.oenv.globals[ddkey] = self.options['jinja2_globals'][ddkey]
          except:
             pass
          ##;;

          ## jinja2_globals
          if(not 'debugging_alerts_01'):
            print "### wizardly_vaselike_virility ------------------------------------------------------------------------"
            print self.oenv.globals
          ##;;

          ## init ;; jinja_config
          ## standard initializtion parameters for jinja2
          '''
          syntaxconfig          ;; syncondesc    ;; syncondefault
          block_start_string    ;; blockstart    ;; '{%'
          block_end_string      ;; blockend      ;; '%}'
          variable_start_string ;; variablestart ;; '{{'
          variable_end_string   ;; variableend   ;; '}}'
          comment_start_string  ;; commentstart  ;; '{#'
          comment_end_string    ;; commentend    ;; '#}'
          '''
          self.oenv.block_start_string    = self.options['block_start_string'   ]
          self.oenv.block_end_string      = self.options['block_end_string'     ]
          self.oenv.variable_start_string = self.options['variable_start_string']
          self.oenv.variable_end_string   = self.options['variable_end_string'  ]
          self.oenv.comment_start_string  = self.options['comment_start_string' ]
          self.oenv.comment_end_string    = self.options['comment_end_string'   ]
          self.oenv.cache_size            = '0'
          ##;;

          ## init custom filters for self.oenv
          for addonclass in self.addonFilters:
            self.oenv = addonclass.attach_filters( self.oenv )
              ## see href="./JinjaFilterBase.py"
              ## see href="./JinjaFilterDynamicYAML.py"
            pass
          ##;;

          ##
          #return self.oenv
        ##enddef

        #@ figure out optimal use of jinja finalize
        #@ def oenv_finalize(self,vinput):
        #@   vout = ''
        #@   if not (vinput is not None):
        #@     vout = '__blank__'
        #@   ##
        #@   return vout
        #@ ##enddef

        def py_mergedict(self, dict1, dict2):
          '''
          ## desc
          python addon function for merging nested dictionaries

          ## see also:
          * http://stackoverflow.com/a/7205672/42223
          '''
          for ppk in set( dict1.keys()).union(dict2.keys() ):
              if ppk in dict1 and ppk in dict2:
                  if isinstance(dict1[ppk], dict) and isinstance(dict2[ppk], dict):
                      yield (ppk, self.dict(py_mergedict(dict1[ppk], dict2[ppk])))
                  else:
                      # If one of the values is not a dict, you can't continue merging it.
                      # Value from second dict overrides one in first and we move on.
                      yield (ppk, dict2[ppk])
                      # Alternatively, replace this with exception raiser to alert you of value conflicts
              elif ppk in dict1:
                  yield (ppk, dict1[ppk])
              else:
                  yield (ppk, dict2[ppk])
        ##enddef

        ##
        def data_struct_merge(self,ob001,ob002,path=None):
          """
          ### main:
          ###   - date: created="Thu Jul 16 13:04:13 2015"
          ###     last: lastmod="Thu Jul 16 13:04:13 2015"
          ###     tags:           tags
          ###     author:         created="__author__"
          ###     dreftymacid:    "lastly_oxen_unearth"
          ###     seealso: |
          ###         *
          ###     desc: |
          ###         merges ob002 into ob001
          ###         * TODO ;; move this to datahelperutils
          """
          ##
          vout  =  dict( self.py_mergedict(ob001,ob002) )
          return vout
        ##enddef

        ##
        def ff_resolvepath_read(self,spath=''):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:    read a string filepath with path that is potentially relative to path of strYamlCustomEndSection
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         string content of file at spath
          ###     details: |
          ###         _details_
          ###     example: |
          ###         _example_
          ###     seealso: |
          ###         regain://python_is_readable
          '''
          ##
          sscurr      =   ''
          getpath     =   ''
          spath_mod01 =   '/'.join( [self.ffpath_pdir,'/',spath]  )
          ## check if spath is readable without modification
          if(os.access(spath,os.R_OK)):
            getpath = spath
          ## check if spath is readable as relative to path of strYamlCustomEndSection
          if(os.access(spath_mod01,os.R_OK)):
            getpath = spath_mod01
          ## try to read the file
          if(sscurr ==  '' and (not getpath == '')):
            try:
              sscurr = open(getpath,'rb').read() + "\n"
            except Exception:
              pass
          return sscurr
        ##enddef

        ##
        def ff_resolvepath_path(self,spath=''):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:    resolve and return a file path where path is potentially relative to strYamlCustomEndSection
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         fully_qualified_path
          ###     details: |
          ###         _details_
          ###     example: |
          ###         _example_
          ###     seealso: |
          ###         regain://python_is_readable
          '''
          ##
          sscurr      =   ''
          getpath     =   ''
          spath_mod01 =   '/'.join( [self.ffpath_pdir,'/',spath]  )
          spath_mod01 =   re.sub(r'/+',"/",spath_mod01) ## why multipleslashes showingup?
          ## check if spath is readable without modification
          if(os.access(spath,os.R_OK)):
            getpath = spath
          ## check if spath is readable as relative to path of strYamlCustomEndSection
          if(os.access(spath_mod01,os.R_OK)):
            getpath = spath_mod01
          ##
          return getpath
        ##enddef

        ##
        def ff_filepath_to_dirpath(self,spath=''):
          '''
          ### main:
          ###   - date: created="2016-03-25T16:36:26"
          ###     desc: >
          ###       take a path that points to a file and convert it to path
          ###       that points to the parent directory of that file
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         string path
          ###     details: |
          ###         _details_
          ###     example: |
          ###         _example_
          ###     seealso: |
          ###         *
          '''
          ##
          sscurr      =   ''
          getpath     =   ''
          spath_mod01 =   '/'.join( [self.ffpath_pdir,'/',spath]  )
          ## check if spath is readable without modification
          if(True
              and os.access(spath,os.R_OK)
              and os.path.isdir(spath)
              ):
            getpath = spath
          ##;;

          ## check if spath points to a file
          if(True
              and os.access(spath,os.R_OK)
              and os.path.isfile(spath)
              ):
            getpath = os.path.dirname(spath)
          ##;;

          ##
          return getpath
        ##enddef

        def dict_smartupdate( self, ddmaster={} , ddreplica={} ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * do a dictionary update
              * never let a non_blank name_value_pair be overwritten by a blank name_value_pair
            funcparams: |
              * argname ;; argtype ;; argdesc
            seealso: |
              * regain://dictionary smartmerge
            last: lastmod="2017-01-01"
            date: created="2017-01-01"
            dreftymacid: pydictsmartmerge_crop_viewer_amaz
          '''
          atest   =   dict( ddmaster  )
          btest   =   dict( ddreplica )
          btest   =   dict( [(vk,vv) for vk,vv in btest.items() if str(vv) and vv is not None] )
          atest.update( btest )
          ##
          return atest
        ##;; enddef

        def dict_aliaskeys( self, ddmaster={} , aakeys=[] ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * return a dict with alias_keys name_value_pairs populated from master_key name_value_pair
              * master_key name_value_pair must be nonempty string
            funcparams: |
              * argname ;; argtype ;; argdesc
            last: lastmod="2017-01-01"
            date: created="2017-01-01"
            dreftymacid: pydict_rioter_counter_fatalism
          '''
          ##
          vxdata  = None

          try:
            vxdata = ddmaster[aakeys[0]]
          except Exception as msg:
            vout  =   ddmaster

          try:
            if(str(vxdata) != '' and vxdata is not None):
              for vxkey in list(ddmaster.keys()):
                if( vxkey in aakeys ):
                  ddmaster[vxkey] = vxdata
              vout = ddmaster
          except Exception as msg:
            vout = ddmaster

          ##
          return ddmaster
        ##;; enddef

        def proc_convert_str_to_dict( self, ssraw='', sskey='', ddmain={} ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * change string into a dictionary
            funcparams: |
              * ssraw ;; string ;; raw_string_value
              * sskey ;; string ;; dictionary key to use in the dict
              * ddmain ;; dict ;; dictionary name_value_pairs
            funcreturn: |
              * pydict ;; output dictionary
            last: lastmod="2017-01-02"
            date: created="2017-01-02"
            dreftymacid: pystrtodict_over_boils_volt
          '''
          ddmain[sskey] = ssraw
          vout = dict(ddmain)
          ##
          return vout
        ## enddef

        ## bkmk002
        def proc_directive_load_outputfile( self, row_proc_directive=None , tmpkey='' ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * send default template output to zero_or_more files
            funcdetail: |
              ## details
              * the directive accepts the following name_value_pairs
                  * path ;; the filepath to perform filewrite
                  * mode ;; the output mode for filewrite
                    * create    ;; create file if not already_exists, do_nothing if already_exists
                    * replace   ;; create file if not already_exists, overwrite if already_exists
                    * append    ;; create file if not already_exists, append if already_exists
            example: |
              * href="smartpath://mytrybits/m/trymyclip/myclip.raw/drupal7/d7_contenttype_add/ddgen-baseconf-html-000.twig" find="vitod3fazak"
            funcparams: |
              * argname ;; argtype ;; argdesc
            funcreturn: |
              * table_aod ;; directive specification for later processing
            last: lastmod="2017-01-02"
            date: created="2017-01-02"
            dreftymacid: ddyoutfile_citizen_bogs
          '''

          ##
          vout  = None
          tmptable          = []
          tmp_row_empty     = dict({ "path": '', "mode": '', })
          tmp_row_default   = dict({ "path": '', "mode": 'create', })

          ##
          if( (tmpkey) in row_proc_directive ):
            ##
            tmpval          = row_proc_directive[tmpkey]
            tmptable        = self.proc_directive_aod_load( tmpval, 'path', tmp_row_empty , tmp_row_default )

            ## finalize
            if(len(tmptable) > 0):
              vout = tmptable
            ##;;

          ##
          return vout
        ##enddef

        ##
        def proc_directive_load_outputzip( self, row_proc_directive=None , tmpkey='' ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * send default template output to a zip archive
            funcdetail: |
              ## details
              * the directive accepts the following name_value_pairs
                  * path ;; the filepath to perform filewrite within the zip archive
                  * zip  ;; the filepath to the zip archive
                  * mode ;; the output mode for filewrite
                    * create    ;; create file if not already_exists, do_nothing if already_exists
                    * replace   ;; create file if not already_exists, overwrite if already_exists
                    * append    ;; create file if not already_exists, append if already_exists
            funcparams: |
              * argname ;; argtype ;; argdesc
            funcreturn: |
              * table_aod ;; directive specification for later processing
            seealso: |
              * regain://"mckay_planets_richer"
            last: lastmod="2017-01-02"
            date: created="2017-01-02"
            dreftymacid: ddyoutfile_citizen_bogs
          '''

          ##
          vout  = None
          tmptable          = []
          tmp_row_empty     = dict({ "path": '', "zip": '', })
          tmp_row_default   = dict({ "path": '', "zip": '', })

          ##
          if( (tmpkey) in row_proc_directive ):
            ##
            tmpval          = row_proc_directive[tmpkey]
            tmptable        = self.proc_directive_aod_load( tmpval, 'path', tmp_row_empty , tmp_row_default )

            ## finalize
            if(len(tmptable) > 0):
              vout = tmptable
            ##;;

          ##
          return vout
        ##enddef

        def proc_directive_load_templateinclude( self, row_proc_directive=None , tmpkey='' ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * load zero_or_more addon templates from zero_or_more external filepaths
            funcdetail: |
              ## details
              * the directive accepts the following name_value_pairs
                  * path ;; the readfile filepath which contains the template text
                  * section ;; where to load the addon templates relative to the default template
                    * head   ;; load addon template before the default_template
                    * foot   ;; load addon template after the default_template
            funcparams: |
              * argname ;; argtype ;; argdesc
            funcreturn: |
              * table_aod ;; directive specification for later processing
            last: lastmod="2017-01-02"
            date: created="2017-01-02"
            dreftymacid: ddtemplinc_coin_bloke
          '''
          ##
          vout = None
          tmptable          = []
          tmp_row_empty     = dict({ "section":'',        "path":     '', })
          tmp_row_default   = dict({ "section":'foot',    "path":     '', })
          ##
          if( (tmpkey) in row_proc_directive ):
            ##
            tmpval          = row_proc_directive[tmpkey]
            tmptable        = self.proc_directive_aod_load( tmpval, 'path', tmp_row_empty , tmp_row_default )

            ## add txtbody fields based on row['path']
            for row in tmptable:
              try:
                row['txtbody']   = str( self.ff_resolvepath_read( row['path'] ) )
              except:
                raise ValueError('err: teams_crumble_mire error proccessing templateinclude {0}'.format( row ))
              pass
            ##;;

            ## finalize
            if(len(tmptable) > 0):
              vout = tmptable
            ## print tmpval
            ##;;
          ##
          return vout
          pass
        ##enddef

        def proc_directive_aod_load( self, vloaded=None , ssdefault='path' , ddmyminimal={'path':''} , ddmydefault={'path':''} ):
          '''
          - rectype:  "rrfuncdocsmall"
            funcdesc: |
              * some directives accept either single_string or table_aod as their input data
              * these are called directive_aod_node
              * load a directive_aod_node and ensure it is table_aod
              * return a table_aod
            funcparams: |
              * vloaded ;; various ;; user_supplied value provided to the function
              * ssdefault ;; string ;; the default dict_key to apply to single_string value
              * ddmyminimal ;; dict ;; the minimum_required fields for the rows in the table_aod
              * ddmydefault ;; dict ;; dictionary with default values, for any required name_value_pairs
            funcreturn: |
              * pylist ;; table_aod ;; python list of dictionary (aka array_of_dictionary) (aka table_aod)
            last: lastmod="2017-01-01"
            date: created="2017-01-01"
            dreftymacid: ddyamlfunc_insects_nearing_oil
          '''
          ## init vars
          table_aod = []
          vout = None
          ##;;

          ## process
          if(None is True):
            pass

          elif( type(vloaded) is str ):
            tmp_row_curr    =   self.proc_convert_str_to_dict( vloaded, ssdefault, dict(ddmyminimal) )
            tmp_row_curr    =   self.dict_smartupdate(tmp_row_curr,ddmydefault)
            table_aod       =   [ tmp_row_curr ]

          elif( type(vloaded) is list ):
            rowiter = list( vloaded )
            for datarow in rowiter:
              if(None is True):
                pass
              elif( type(datarow) is str ):
                datarow   =   self.proc_convert_str_to_dict( datarow, ssdefault, dict(ddmyminimal))
                datarow   =   self.dict_smartupdate(datarow,ddmydefault)
                table_aod.append( datarow )
              elif( type(datarow) is dict ):
                datarow   =   self.dict_smartupdate(ddmydefault,datarow)
                table_aod.append( datarow )
          ##;;

          vout = list(table_aod)
          ##
          return vout
        ## enddef

        #@@ ## TODO ;; refactor this ;; parasitic inheritance method that just returns the result of
        #@@ ##    firstpass multipass processing
        #@@ ##    YamlEmbedJinja.template_render_1stpass
        def ddexport(self,txtbody):
          from YamlEmbedJinja import YamlEmbedJinja ### "./YamlEmbedJinja.py"
          parser01        =   YamlEmbedJinja()
          ddexport_vout   =   parser01.template_render_1stpass(yaml=txtbody)
          return ddexport_vout
        ##enddef

        ##
        def ddtransform(self):
          """
          ### main:
          ###   - date: created="Thu Jul 16 13:55:43 2015"
          ###     last: lastmod="Thu Jul 16 13:55:43 2015"
          ###     tags:         tags
          ###     dreftymacid:  "darken_doubts_brains"
          ###     seealso: |
          ###         *
          ###     desc: |
          ###         desc
          """
          ## placeholder syntax
          sgg_dynamicyaml_key     =   self.options['ddyaml_end_marker']
          sgg_dynamicyaml_key     =   sgg_dynamicyaml_key.lower()
          sgg_directiveprefix_str =   ''
          ##;;

          ## init vars
          ddtransform_aaout   =   []
          ssgpath             =   ''
          originalconfig      =   {}
          ##;;

          ### TODO ;; adopt the conventions from yamlembedjinja ;; yamlregions
          ###     href="./YamlEmbedJinja.py" find="blast_tinworks_reply"
          ###     href="./YamlEmbedJinja.py" find="yamlregions_primary"
          ### TODO ;; get strYamlCustomEndSection and svirtualtemplate sorted out
          ###     the use between these variables is sub-optimal
          ### ------------------------------------------------------------------------
          if('load_attempt_stora'):
            ##
            bload_stora_success       =   False
            strYamlCustomEndSection   =   ''

            ## get strYamlCustomEndSection from primaryYamlPath
            try:
              ssgpath = self.ffpath_norm
            except Exception:
              #return ''
              pass
            ##;;

            ##
            if(not bload_stora_success):
              ###
              try:
                strYamlCustomEndSection     =     codecs.open(ssgpath, 'r', 'utf-8').read()
                if( self.options['ddyaml_process_twopass'] ):
                  strYamlCustomEndSection   =     self.ddexport(strYamlCustomEndSection)
                originalconfig        =     yaml.safe_load(strYamlCustomEndSection) or originalconfig
                #self.metadata['directives_meta_table'] = originalconfig[self.options['ddyaml_end_marker']]
                bload_stora_success   =     True
              except:
                pass
              ###;;;
            ##;;
          ## endif

          ##
          if( not 'debugging_alerts_01'):
            print originalconfig              ## endsection_as_data
            print strYamlCustomEndSection     ## endsection_as_string
            #print svirtualtemplate
          ## endif

          ### ------------------------------------------------------------------------
          ## init directives_dictionary
          directives = {}
          directives['default_data']            = ''
          directives['default_tpl_with_procs']  = ''
          directives['current_data']            = ''
          directives['current_template']        = ''
          directives['default_data']            = originalconfig.copy()
          ##;;

          ##
          try:
            ## remove the sgg_dynamicyaml_key from default data
            del(directives['default_data'][sgg_dynamicyaml_key])
          except:
            pass
          ##;;

          ##
          if( not 'debugging_alerts_01'):
            oDumper.pprint( directives ) ## directives_as_clean_init
          ##endif

          ## <beg-process01>
          if('region::process01'):
            try:
              ## set default_tpl_with_procs
              ##    use this as the default template if one not specified
              if( directives['default_tpl_with_procs'].__str__() == ''):
                directives['default_tpl_with_procs'] = strYamlCustomEndSection
              ##;;

              ## prepare to iterate_directives ;; tmp_processing_directives
              tmp_processing_directives = originalconfig.pop(sgg_dynamicyaml_key,[])
              if (tmp_processing_directives.__len__() == 0):
                tmp_render  =   self.ddexport(strYamlCustomEndSection)
                ## ddtransform_aaout.append ;; accumulate_final_output
                ddtransform_aaout.append( tmp_render )
                self.metadata['directives_meta_table'].append( tmp_render )

              ## bkmk003
              ## iterate_directives ;; tmp_processing_directives
              for row_proc_directive in tmp_processing_directives:
                directives['current_template']    = directives['default_tpl_with_procs']
                directives['current_data']        = directives['default_data']

                ### ********************
                ## process row

                ## @@@ usedataroot directive ;; wrap all the template data in a common 'dataroot' element
                ## (eg) usedataroot: "myworkbook"
                ## (eg) usedataroot: "datarootf"
                tmpname = ['use','dataroot']
                tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row[tmpkey]
                  if(str(tmpval).strip() != ''):
                    directives["".join(tmpname)] = str(tmpval)
                ##;;

                ## @@@ processthis directive ;; skip this entire processing row if processthis evals to false
                tmpname = ['process','this']
                tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row_proc_directive[tmpkey]
                  if(bool(tmpval) == False): continue;
                ##;;

                ## @@@ templatefile directive ;; we get a template from a single external file
                tmpname = ['template','file']
                tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  #print tmpval
                  tmpval = self.ff_resolvepath_path( row_proc_directive[tmpkey] )
                  # exit()
                  directives['current_'+tmpname[0]]   =   textwrap.dedent(open(tmpval,'rb').read())
                  ## print tmpval
                ##;;

                ## @@@ template directive ;; we get template from strYamlCustomEndSection
                tmpname = ['template','']
                tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row_proc_directive[tmpkey]
                  directives['current_'+tmpname[0]]   =   textwrap.dedent(tmpval)
                  ## print tmpval
                ##;;

                ## bkmk002
                ## @@@ outputfile directive ;; output content to a text file
                tmpname = "".join(  ['output','file'] )
                tmpkey  = sgg_directiveprefix_str + tmpname
                directives['current_'+tmpname] = self.proc_directive_load_outputfile( row_proc_directive,tmpkey )
                ##;;

                ## @@@ outputzip directive ;; output content to a zip archive file
                tmpname = "".join(  ['output','zip'] )
                tmpkey  = sgg_directiveprefix_str + tmpname
                directives['current_'+tmpname] = self.proc_directive_load_outputzip( row_proc_directive,tmpkey )
                ##;;

                ## @@@ templateinclude directive ;; we get one_or_more template from one_or_more external file
                ## and merge with strYamlCustomEndSection
                tmpname   =   "".join(['templateinclude'])
                tmpkey    =   sgg_directiveprefix_str + tmpname
                directives['current_'+tmpname] = self.proc_directive_load_templateinclude( row_proc_directive,tmpkey )
                ##;; endif

                ## bkmk001
                ## @@@ pathinclude directive ;; we get one_or_more path for use with jinja.FileSystemLoader
                tmpname =   ['pathinclude']
                tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row_proc_directive[tmpkey]

                  ## iterate includes ;; force_scalar_to_list
                  sstemp = ''
                  if(tmpval is None):
                    tmpval = ['']
                  if(  type(tmpval) == str ):
                    tmpval = [tmpval] ## force_scalar_to_list

                  ## iterate items ;; miner_starts_guava
                  for spath in tmpval:
                    ## return readable path or else empty string
                    sscurr = self.ff_resolvepath_path(spath)
                    sscurr = self.ff_filepath_to_dirpath(sscurr)
                    # print " bkmk001 ### ------------------------------------------------------------------------ "
                    # print sscurr
                    #print os.path.dirname(sscurr)

                    ## err_quiet
                    if(sscurr == ''):
                      continue
                    ## err_verbose
                    if(sscurr ==  ''):
                      raise ValueError('wenga_hsiw_repel: failed to access file content at %s '%(spath))
                    elif(True):
                      self.options['filesystemloader_paths'].append( sscurr )
                      # print " bkmk001 :: directs_dozer_forums ### ------------------------------------------------------------------------ "
                      # print sscurr
                ##;;

                ## @@@ datainclude directive ;; concatenate multiple yaml files to input additional data
                ## and merge it with strYamlCustomEndSection
                tmpname =   ['datainclude','']
                tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row_proc_directive[tmpkey]

                  ## iterate includes ;; force_scalar_to_list
                  sstemp = ''
                  if(tmpval is None):
                    tmpval = ['']
                  if(  type(tmpval) == str ):
                    tmpval = [tmpval]     ## force_scalar_to_list

                  ## iterate items
                  for spath in tmpval:
                    sscurr        =   ''
                    sscurr        =   self.ff_resolvepath_read(spath)
                    ## err_quiet
                    if(sscurr == ''):
                      continue
                    ## err_verbose
                    if(sscurr ==  ''):
                      raise ValueError('undid_sail_unleash: failed to access file content at %s '%(spath))
                    elif(True):
                      sscurr    = self.ddexport(sscurr) ##;; apply firstpass transform to embedded datainclude
                      sstemp    += sscurr
                  ##
                  if(sstemp != ''):
                    ## print sstemp
                    directives['current_'+tmpname[0]]   =   yaml.safe_load(sstemp)
                  ## print tmpval
                ##;; endif

                ### TODO ;; NOT_YET_SUPPORTED
                ### @@@ dataurl directive ;; we get a data from an included url

                ## @@@ data directive ;; we get data from strYamlCustomEndSection
                tmpname = ['data','']
                tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
                #print row
                if( (tmpkey) in row_proc_directive ):
                  tmpval = row_proc_directive[tmpkey]
                  directives['current_'+tmpname[0]]   =   yaml.safe_load(tmpval)
                ##;;

                ### ------------------------------------------------------------------------
                ## begin_

                ## preproc directives
                if('current_templateinclude' in directives and (type(directives['current_templateinclude'])) is list):
                  tmptable = []
                  tmptable.extend( directives['current_templateinclude'] )
                  directives['current_template'] = ( ''
                    + "".join( [row['txtbody'] for row in tmptable if( row['section']== 'head')] )
                    + directives['current_template']
                    + "".join( [row['txtbody'] for row in tmptable if( row['section']== 'foot')] )
                    )

                if('current_datainclude' in directives):
                  directives['current_data'] = self.data_struct_merge(directives['current_datainclude'],directives['current_data'])

                if('usedataroot' in directives):
                  tmpname = directives['usedataroot']
                  directives['current_data'] = {tmpname: directives['current_data']}
                ##;;

                ## debug before render
                #oDumper.pprint( directives )
                #print yaml.safe_dump( directives )
                #print json.dumps(directives, sort_keys=True,indent=4, separators=(',', ': '))
                #print yaml.safe_dump(directives, default_flow_style=False)
                if(not 'debugging_alerts_01'):
                  mykeys = directives.keys()
                  mykeys.sort()
                  for tmpkey in mykeys:
                    print "\n\n\n"
                    print "### ------------------------------------------------------------------------"
                    print "### %s" %(tmpkey)
                    print "### ------------------------------------------------------------------------"
                    print directives[tmpkey]
                  exit()

                ### ------------------------------------------------------------------------
                ## begin_

                ## render output
                ## TODO ;; allow customizable data merge semantics
                directives['default_data'].update(directives['current_data'])
                ## bkmk001
                self.provision_jinja2_environment()
                #oEnv  =  self.oenv
                otemplate_data  =   directives['default_data']
                mystring        =   textwrap.dedent(directives['current_template'])
                template        =   self.oenv.from_string(mystring)
                tmpout          =   template.render(otemplate_data)

                if(not 'debugging_alerts_01'):
                  print "### ------------------------------------------------------------------------"
                  print "\n\n\n"
                  print "%s" %( mystring )
                  print "\n\n\n"
                  print "### ------------------------------------------------------------------------"
                  exit()

                ## force unix line endings
                if(True):
                  tmpout = string.replace(tmpout, '\r\n', '')
                  tmpout = string.replace(tmpout, '\r', '')
                ## ddtransform_aaout.append ;; accumulate_final_output
                ddtransform_aaout.append( tmpout )
                row_proc_directive['rendered_template'] = tmpout
                self.metadata['directives_meta_table'].append( row_proc_directive )
            ##;;
            ## exception ;; process01
            except Exception as msg:
              print 'EXCEPTION voyeur_foulest_weirdly msg@%s'%(msg.__repr__())
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              print(exc_type, fname, exc_tb.tb_lineno)
            ##;; endtry

            ### ------------------------------------------------------------------------
            ## begin_

            ## postproc directives
            try:
              ##
              tmpname = "_".join(['current','outputfile'])
              if(tmpname in directives and (type(directives[tmpname]) is list) ):
                for tmprow in list(directives[tmpname]):
                  self.JFiltMain.jjtofile(tmpout,tmprow['path'],tmprow['mode'],usebom=False)
              ##;;
            except Exception as msg:
              ##
              print 'EXCEPTION ariser_twister_teams msg@%s'%(msg.__repr__())
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              print(exc_type, fname, exc_tb.tb_lineno)
              ##;;
            ##;; endtry

          ##;; <end-process01>
          #oDumper.pprint( directives )
          ##endfor::iterate_yaml

          #print yaml.safe_dump( ddtransform_aaout , default_flow_style=False  )
          ##vjj = "\n"
          vjj   = ""
          ddtransform_aaout  = [vjj +  vxx for vxx in ddtransform_aaout]
          ddtransform_aaout  = "".join(ddtransform_aaout)
          ##;;

          ## handle output file directives
          ## zipfile directives have to be handled last so zip paths all go to the same archive file
          tmptable = self.metadata['directives_meta_table']

          for tmprow in tmptable:
            if (not 'outputfile' in tmprow): continue
            subtable = tmprow['outputfile']
            ## TODO ;; fix this ;; code changes broke the string-to-dictionary functionality
            for subrow in subtable:
              self.JFiltMain.jjtofile(tmprow['rendered_template'],subrow['path'],subrow['mode'],usebom=False)

          for tmprow in tmptable:
            if (not 'outputzip' in tmprow): continue
            subtable = tmprow['outputzip']
            for subrow in subtable:
              self.JFiltMain.jjtozipfile(tmprow['rendered_template'],subrow['path'],subrow['zip'])
          ##;;

          ##
          return ddtransform_aaout
        ##enddef
      ##endclass
###!}}}
