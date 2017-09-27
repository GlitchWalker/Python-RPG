# Python-RPG
My first Python game

As this is a more complex project, I'm going to start off more closely following the course than creating my own, umm, "tweaks" as I did for what was to become the Vulgar Calculator.

Instead, I'm going to start making bigger changes once I have finished it and have a working prototype.

My first big change/deviation from the course was implementing a "Charge" type of magic. This was because it was still likely the enemy could kill the player, and I felt confident enough to deviate from the course video and try implementing my own thing. This type includes the spell "Pray", which increases MP by about 30. I'm considering including an "MP Gamble" magic as part of this type, which gambles 50 MP for a 50/50 chance to refill the entire MP gauge. I might wait a while before doing this though.

The second big difference was how I decided to display the character stat bars, compared to the original. I preferred having a "line of underscores" between each character, so it is easier to read and neater (as it has the effect of having a line between each character). There are also some minor differences in terminoligy, both in status text and my own code, to make it more my own and have it read how I want it to

For example, whereas "item.prop" is used for the amount an item might heal/damage, I chose to use "item.dmg". This meant it was consistent with "magic.dmg", which both is the amount of damage magic will do as well as the amount of health/MP it heals by.
