# Writing MakeShift Templates
Writing a new template for MakeShift requires an idea, a little creativity, and understanding the simple MakeShift syntax. You can write a template in your favorite text editor, like Notepad++, Sublime Text, or directly into the [lab](lab.html) editor. So pop open your favorite editor and let's get started with an example.

## The Idea
The first thing you need for a new MakeShift template is an idea of what you want to create. Are you naming a new location? Coming up with a new character? Listing the items inside a treasure chest? 

Let's pretend I'm the dungeon master for a Dungeons & Dragons group. We're on a quest that will bring the group out to a series of seaside beaches to find clues and investigate a crime. I want each beach to have a spooky name to go with the tone of the adventure. MakeShift would be perfect for helping to come up with a bunch of names for our haunted beaches.

## The Syntax
Let's start our MakeShift template with two ideas that are blatantly stolen from other media. We'll write `beach` as the first line of our template, followed by the two names we're borrowing from elsewhere, each on its own line and indented with a tab.
```
beach
    The Banshee Bay
    Twilight Tides
```
Our template right now is saying that a `beach` is defined as either `The Banshee Bay` or `Twilight Tides`. There's a 50% chance of either one.

Let's expand those two options. We'll take out words that represent something very specific and replace them with more general placeholders. In this case, a banshee is a sort of monster in our D&D world. We'll replace the word 'banshee' in our template with the `{monster}` placeholder. 
```
beach
    The {monster} Bay
    Twilight Tides
```

Great! Now let's pick some spooky-sounding monsters that could get plugged in here. We'll add a new entry for `monster` with a couple options below it:
```
beach
    The {monster} Bay
    Twilight Tides

monster
    Banshee
    Spirit
    Phantom
    Wraith
```

Now, whenever we encounter the `{monster}` placeholder, we'll pick an option from the `monster` list. We could still get "The Banshee Bay," but we might also get "The Sprit Bay," "The Phantom Bay," or "The Wraith Bay."

Let's add some more placeholders. The word 'bay' is just a natural feature, and the word 'tides' is too. Let's replace those with a `{natural_feature}` placeholder. While we're at it, let's add a list of a few `natural_feature` choices.
```
beach
    The {monster} {natural_feature}
    Twilight {natural_feature}

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
```

The word 'Twilight' isn't really an adjective here, but that's ok, we're going to say it is one anyway so we can replace it with another placeholder:
```
beach
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

Great! We've expanded the possibilities for our beach names by using placeholders and lists. Based on this template, a beach name will follow two general formats:
1. The word 'The', followed by a monster and then a natural feature
2. An adjective followed by a natural feature

Those formats then pull random options from our three lists.

With just a couple lines and some fun adjectives, we have a template that can create about 40 random names for our haunted beaches.