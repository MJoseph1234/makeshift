---
layout: page
title: About
---

# About

MakeShift started as a tool to assist dungeon masters and game masters playing games like Dungeons & Dragons. I wanted a quick an easy way to come up with ideas when my players would ask questions like *"What's the name of the local tavern or inn?"* 

With MakeShift, if I don't already have a name prepared, I can use
```bash
> makeshift inn.txt -c 10
```
to come up with ten quick ideas for my tavern name. 

The code originally worked by abusing [Python f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) when writing templates. I wanted something more flexible so friends - who might not be as familiar with Python - could write their own templates. Templates as text files using indents and curly brackets seemed like a simple, readable choice. 

## Inspiration
MakeShift follows on the heels of existing generator tools like:
 - [Perchance](https://perchance.org/welcome)
 - [Ortiel's RandomGen](https://orteil.dashnet.org/randomgen/?do=create)
 - [Rant](https://rant-lang.org/)