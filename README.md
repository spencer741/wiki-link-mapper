# WikiLinkMapper
Creating a link map from Wikipedia Links using level-order traversal.

# v1 specs 

Non-Graphical Map

Prompt Order:
1. User specifies core subject desired
2. ~~User toggles all or no links per page~~
3. User specifiies depth
4. Execution

General:
1. Writes Links to file(s)
2. Several link revisions may be needed
3. Use ~~regex for finding links~~ Parsing Function
4. Ability for user to filter out types of links?
5. Check previously visited links to prevent looping between old articles
6. May have to utilize a db for #5 when tree depth gets large
TODO:
1. Generalize Parsing function
2. End parsing at 'id=mw-navigation' -- acheived with recursive behaivior within parsing function when it is generalized to select a match to the latter. 

