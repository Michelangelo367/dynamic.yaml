### <beg-file_info>
### main:
###   - date: created="Thu Mar 17 17:32:46 2016"
###     last: lastmod="Thu Mar 17 17:32:46 2016"
###     tags:   url, requests, http, web, scraping, bsoup,
###     author: created="__author__"
###     dreftymacid: "hornet_krause_blinds"
###     filetype: "yaml"
###     seealso: |
###         *
###     desc: |
###         * demo web crawling and scraping
### <end-file_info>
## href="smartpath://mytrybits/y/tryyaml/dynamicyaml/devlog.txt"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/readme.md"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyamlrunner.py"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"


links_table:
  - { "site":  "http://www.example.com",   }
  - { "site":  "http://www.alpha.com",   }
  - { "site":  "http://www.bravo.com",   }

__yaml__:

  - &uuid002
    caption:     jjurl_exists ;; test for existence
    processthis: 1
    uuid:         uuid002
    template: |
      ### ------------------------------------------------------------------------
      ### jjurl_exists
      {% for row in links_table -%}
      {{ ''|jjurl_exists(row.site) }}
      {% endfor %}

  - &uuid001
    caption:      jjurl_request ;; get the requested url
    processthis:  1
    uuid:         uuid001
    template: |
      ### ------------------------------------------------------------------------
      ### jjurl_request
      {%- set ttfindtag = 'title'  -%}
      {% for row in links_table -%}
      {{ ''|jjurl_request(row.site) |jjhtml_findall(ttfindtag) }}
      {% endfor %}


