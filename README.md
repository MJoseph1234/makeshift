# MakeShift
A tool for making your own procedurally generated { text | characters | settings | worlds | anything }.

### What is this?
`MakeShift` is designed to help { storytellers | authors | dungeon masters | people like you } find inspiration for creating settings and characters. `MakeShift` allows creators to write a template for whatever it is they want to make, and then (using the power of \**computers*\*) procedurally generate something brand new based on that template.

It works kind of like a MadLib, except you have complete control over the list of options, and you can even nest one MadLib inside another for extra variety. The computer then uses the options you define to fill in all the blanks.

This repository contains two things: 
1. A little mini-language and syntax for writing a template
2. A python script to compile your template and run it to create something new

#### what..?
Procedural Generation is a way of having a computer create a random, never-before-seen *thing* by combining computer-powered randomness with a set of human-created guidelines. `MakeShift` makes it easy for programmers and non-programmers to write those human-created guidelines, and then run them through a computer-powered generator to see what comes out.

For example, let's say our Dungeons & Dragons group is going on a quest that will bring them out to a seaside town to investigate a crime. To add some flavor, we want to give some of the nearby beaches a spooky name. A simple `MakeShift` template for a haunted beach might look like this:
```
Beach
    The {monster} {natural_feature}
    {adjective} {natural_feature}

monster
    Banshee
    Spirit
    Phantom
    Wraith

natural_feature
    Bay
    Coast
    Coastline
    Seashore
    Waters

adjective
    Wailing
    Twilight
    Shadowed
    Ghostly
```
Running this template through a `MakeShift` parser will randomly generate a some haunted beach names that we can send our adventurers through. Some of my favorites are:
- Twilight Tides
- The Banshee Bay
- Ghostly Coast  

With just a couple lines and some fun adjectives, we have a simple `MakeShift` example can create about 40 random names for our haunted beach. A little time and creativity to expand this template can allow limitless randomly generated options.

### How can I use it?
Great question! There's a few things you can do:

Want to write your own template file? There's a tutorial for writing files in progress here. There's a more thorough look at the grammar and fancy things you can do here.

Want to run a template you wrote? You'll have to download the python script and run it from the cli, using some steps here

Want to generate a thing using the vast library we've created? Go here

### How does it work?
Files look like this!  
Running the file looks like this!

