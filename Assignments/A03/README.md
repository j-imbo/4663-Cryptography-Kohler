## A03 Frequency Analysis
### James Kohler
### Description:

Using a frequency analysis to decrypt simple substitution cyphers.

### Files

| # |File|Description|
|:-:|-|-|
|1|[freqs.py](./freqs.py)|Determine frequencies.|
|2|[subs.py](./subs.py)|Perform substitutions.|
|3|[cyphertext_1](./cyphertext_1.txt)|First input cyphertext.|
|4|[cyphertext_1_freq](./cyphertext_1_freq.txt)|First input frequency data.|
|5|[sub_1]|(./sub_1.txt)|First input's key.|
|6|[decrypted_1](./decrypted_1.txt)|First cyphertext decrypted.|
|7|[cyphertext_2](./cyphertext_2.txt)|Second input cyphertext.|
|8|[cyphertext_2_freq](./cyphertext_2_freq.txt)|Second input frequency data.|
|9|[sub_2]|(./sub_2.txt)|Second input's key.|
|10|[decrypted_2](./decrypted_2.txt)|Second cyphertext decrypted.|
|11|[notes](./notes.txt)|Process notes for decryption.|
|12|[decyphersheet](./decyphersheet.ods)|Spreadsheet used to decypher. See notes.|

### Instructions

- This project was compiled using Python 3.8

### Sources

- Statistical distributions of English text:
  - https://web.archive.org/web/20040603075055/http://www.data-compression.com/english.html

I used the source to create lists for frequency comparisons, and then I used those lists to decrypt the cyphers.