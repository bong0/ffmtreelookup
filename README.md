# ffmtreelookup

source: `http://www.offenedaten.frankfurt.de/dataset/73c5a6b3-c033-4dad-bb7d-8783427dd233/resource/7a73520b-961a-4aad-a582-449e676c247c/download/baumbestandveroffentlichung2.zip`

## encode fixing

    dos2unix baumbestand_fromzip.csv
    iconv -f CP437 -t UTF-8 baumbestand_fromzip.csv > baeume.csv
