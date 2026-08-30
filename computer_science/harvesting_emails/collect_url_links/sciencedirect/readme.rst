================================================
Harvesting emails from sciencedirect search page
================================================

extracts from article link
~~~~~~~~~~~~~~~~~~~~~~~~~~~
extract_vcf_from_article_link.js


advanced extracting from search page of a journal
-------------------------------------------------
open a journal search page, like
https://www.sciencedirect.com/search?pub=Computational%20and%20Theoretical%20Chemistry&cid=270466&qs=ab%20initio%20calculations&offset=175

type F12 and copy and paste the most recent script:

extracting_from_search_10.js

into the search page console

and type openAllArticles() 

In ideal case all extracted emails from each open tab (journal article) will download in a vcf file with unique name.

Otherwise type  downloadEmails() .


TODO: 
in each open search page : 
-  extend the script for closing open tabs from where email(s) were sucessfully extracted
- when all emails got downloaded or progress is stalled CONTINUE to next search batch and initiate harvesting from open tabs




