## Current Status:


#####08/01/17
Played aorund with a manually edited opml file and found two causes of teh error code:

1. Any `&` in the title strings
2. Any url ending in (for example) `.../default?start-index=26&max-results=25`. It was the `=` that was the problem.

I manually cleaned the file and then had the `arg_nullreferenceexception` response which translated means `you're on your own pal`.


#####06/01/17
The code now generates an opml file cleanly. 

It will import successfully into desktop (linux) apps but will not import into a windows mobile app (kind of the point of the code really). 

The error complains of a `malformed opml file` but no hints on locations within the file.

/posts/default?start-index=26&max-results=25"

