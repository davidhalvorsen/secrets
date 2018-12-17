The quake_BrainGeo1 download page says this is what the dataset contains:

Number of files: 1411
Total size: 217 GB

My system is reading the dataset as 231.6 GB.
Ubuntu says there are 2,338 "items" in there ... wayyyy higher than I would expect.
I think it's counting folders. A Python script I wrote counted 1405 files, so that's what I'm going with.

I changed line 87 and 88 of the .html FROM:
<b>Number of files:</b> 1411<br>
<b>Total size:</b> 217 GB<p>

CHANGED TO:
<b>Number of files:</b> 1405<br>
<b>Total size:</b> 231.6 GB<p>
