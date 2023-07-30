### TODOs
- send data to SQL DB as well
- preform historical analysis on numbers(N day moving average)

### Function Descriptions from getCoinPrice.py
```python
parse( s )
```
- extract the price from the string
- given pattern '1\s([A-Z]{3})\s=\s(([0-9]|,|\.)*)'
- matches: 
  - the number one
  - exactly 3 capitalized chars as capture group 1
  - " " (space) (\s is the whitespace meta character)
  - the equal sign
  - " " (space)
  - "take as many digits, commas, and dot"

```python
get_link_price( link, content )
```
- link contains the constructed the attribute values
- the 'a' or anchor tag has an href attribute of the value...
		'comparison/bitcoin-price.html'
- content.find_all() 
  - find all the HTML element with the same name and attributes
		log the raw text between the tags > ...raw text... <

---
### Scheduled Tasks:
- call getCoinPrice once an hour
- push getCoinPrice log to git once a day
- re-run viz with new data once a day(use custom get git file)
---
#### launchctl notes
https://launchd.info/

```shell
$ launchctl load CryptoStream.plist

$ launchctl start CryptoStream.plist

$ launchctl list |awk '/Crypto/ || NR == 1'
PID	Status	Label
578	0	com.apple.CryptoTokenKit.ahp.agent
-	0	CryptoStream

$ launchctl list CryptoStream
{
	"LimitLoadToSessionType" = "Aqua";
	"Label" = "CryptoStream";
	"OnDemand" = true;
	"LastExitStatus" = 0;
	"Program" = "/usr/local/bin/python3";
	"ProgramArguments" = (
		"/usr/local/bin/python3";
		"/Users/g_joss/Documents/Computation/getCoinPrice/getCoinPrice.py";
	);
};
```
---

