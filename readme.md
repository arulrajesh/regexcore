The getregex.py generates a regular expression based on the syntax defined in the "TextIntent query Language Search Syntax Quick Reference Guide rev 2021-02.pdf"

you can use the compose method of RegexCore class by calling it as 
```
from regex_core import RegexCore
rege = RegexCore()
reg.compose('''"test* exit"''',limit=30)
```  
  
 
The input Pattern is defined in the last line of the file getregex.py.

![image](https://user-images.githubusercontent.com/4302998/125862852-3e69886a-49ef-46e5-8431-3b3d9608c042.png)

eg" "test* exit" which should match test followed by upto 6 words follwed by exit.

You can test this regex pattern behavior at regex101.com
![image](https://user-images.githubusercontent.com/4302998/125862544-eb42e743-b343-40c6-b40c-f17568d94c97.png)

Next steps:
To add features from "Insight_Search Syntax Quick Reference Guide rev 2019-09.pdf""
