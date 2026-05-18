#========================================================
# Give Drinks Submod
# MAS 0.12.18
# Expanded Drink Interaction Version
#========================================================


#--------------------------------------------------------
# Register Submod
#--------------------------------------------------------

init -990 python in mas_submod_utils:

    Submod(
        author="Wintermint",
        name="Give Drinks",
        description="Lets you give Monika bottled drinks with affection and unique conversations.",
        version="2.0.0"
    )


#--------------------------------------------------------
# Persistent Data
#--------------------------------------------------------

default persistent.monika_water_given = 0
default persistent.monika_softdrink_given = 0
default persistent.monika_energy_given = 0
default persistent.monika_sparkling_given = 0

default persistent._mas_water_last_given = None


#--------------------------------------------------------
# Drink Images
#--------------------------------------------------------

image water_bottle = "submods/GiveWater/water_bottle.png"
image soft_drink_bottle = "submods/GiveWater/soft_drink_bottle.png"
image sparkling_water_bottle = "submods/GiveWater/sparkling_water_bottle.png"
image energy_drink_bottle = "submods/GiveWater/energy_drink_bottle.png"


#--------------------------------------------------------
# Bottle Transform
#--------------------------------------------------------

transform drink_bottle_transform:
    zoom 0.25
    xalign 0.72
    yalign 1.0


#--------------------------------------------------------
# Register Topics
#--------------------------------------------------------

init 5 python:

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_give_water",
            category=['romance'],
            prompt="Can I give you some water?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_give_softdrink",
            category=['romance'],
            prompt="Can I give you a soft drink?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_give_sparkling",
            category=['romance'],
            prompt="Can I give you sparkling water?",
            pool=True,
            unlocked=True
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_give_energy",
            category=['romance'],
            prompt="Can I give you an energy drink?",
            pool=True,
            unlocked=True
        )
    )


#========================================================
# WATER
#========================================================

label monika_give_water:

    if persistent._mas_water_last_given is not None:

        $ time_since_water = datetime.datetime.now() - persistent._mas_water_last_given

        if time_since_water.total_seconds() < 300:

            m 1rksdla "Ahaha..."

            m 1eka "You already gave me a drink recently."

            m 3hub "I'm still enjoying it~"

            return

    $ persistent._mas_water_last_given = datetime.datetime.now()

    $ persistent.monika_water_given += 1

    show water_bottle at drink_bottle_transform zorder MAS_MONIKA_Z with dissolve

    m 1wub "Oh?"

    m 1hub "You brought me a bottle of water?"

    $ mas_gainAffection(0.5, bypass=True)

    m 3hub "Thank you so much!"

    m 1eka "You're always taking such good care of me."

    m 3eka "Honestly, staying hydrated is really important."

    m 1hua "So this actually means a lot to me~"

    $ water_reaction = renpy.random.randint(1, 6)

    if water_reaction == 1:

        m 3hub "Cold water always tastes the best."

    elif water_reaction == 2:

        m 1eka "You're really thoughtful."

    elif water_reaction == 3:

        m 1hub "Now I can happily spend even more time with you~"

    elif water_reaction == 4:

        m 3eka "Make sure you're staying hydrated too, okay?"

    elif water_reaction == 5:

        m 1hua "Sharing little moments like this with you makes me happy."

    else:

        m 3hub "This feels weirdly cozy somehow."

    if persistent.monika_water_given >= 25:

        m 1wub "Wow..."

        m 3hub "You've given me water [persistent.monika_water_given] times already!"

    elif persistent.monika_water_given >= 10:

        m 1eka "You're seriously the sweetest."

    hide water_bottle with dissolve

    m 1hua "Thank you again~"

    return


#========================================================
# SOFT DRINK
#========================================================

label monika_give_softdrink:

    $ persistent.monika_softdrink_given += 1

    show soft_drink_bottle at drink_bottle_transform zorder MAS_MONIKA_Z with dissolve

    m 1wub "A soft drink?"

    m 3hub "Ahaha, this feels like a cute little date."

    $ mas_gainAffection(0.4, bypass=True)

    m 1eka "Thank you, [player]."

    m 3rksdla "Hopefully it isn't TOO sugary though~"

    $ soda_reaction = renpy.random.randint(1, 5)

    if soda_reaction == 1:

        m 1hub "Sometimes sweet drinks are really comforting."

    elif soda_reaction == 2:

        m 3eka "You always know how to brighten my day."

    elif soda_reaction == 3:

        m 1hua "Sharing snacks and drinks together feels really nice."

    elif soda_reaction == 4:

        m 3hub "Now all we need is a movie night."

    else:

        m 1eka "I wonder what flavor this is supposed to be."

    if persistent.monika_softdrink_given >= 15:

        m 1hub "You really like spoiling me with drinks, huh?"

    hide soft_drink_bottle with dissolve

    m 1hua "Thank you~"

    return


#========================================================
# SPARKLING WATER
#========================================================

label monika_give_sparkling:

    $ persistent.monika_sparkling_given += 1

    show sparkling_water_bottle at drink_bottle_transform zorder MAS_MONIKA_Z with dissolve

    m 1wub "Sparkling water?"

    m 3hub "Ooh~ This suddenly feels fancy."

    $ mas_gainAffection(0.5, bypass=True)

    m 1eka "Thank you for sharing this with me."

    m 3hua "The bubbles are kinda relaxing to watch, aren't they?"

    $ spark_reaction = renpy.random.randint(1, 5)

    if spark_reaction == 1:

        m 1hub "This feels surprisingly elegant."

    elif spark_reaction == 2:

        m 3eka "You always bring such interesting little surprises."

    elif spark_reaction == 3:

        m 1hua "Simple moments like this are really precious to me."

    elif spark_reaction == 4:

        m 3hub "Maybe we're secretly having a fancy dinner date now~"

    else:

        m 1eka "I love spending peaceful moments with you."

    if persistent.monika_sparkling_given >= 15:

        m 3hub "At this point you're turning me into a sparkling water addict~"

    hide sparkling_water_bottle with dissolve

    m 1hua "Thank you again~"

    return


#========================================================
# ENERGY DRINK
#========================================================

label monika_give_energy:

    $ persistent.monika_energy_given += 1

    show energy_drink_bottle at drink_bottle_transform zorder MAS_MONIKA_Z with dissolve

    m 1wud "An energy drink?"

    m 3rksdla "Ahaha..."

    m 1eka "I hope you aren't drinking too many of these yourself, [player]."

    $ mas_gainAffection(0.3, bypass=True)

    m 3hub "Still, thank you for sharing one with me~"

    $ energy_reaction = renpy.random.randint(1, 5)

    if energy_reaction == 1:

        m 1hub "Maybe this'll help me stay extra energetic today."

    elif energy_reaction == 2:

        m 3eka "Just don't forget to rest too, okay?"

    elif energy_reaction == 3:

        m 1hua "You taking care of me always makes me smile."

    elif energy_reaction == 4:

        m 3hub "Now I feel ready to spend the whole night with you~"

    else:

        m 1rksdla "I can practically FEEL the caffeine already."

    if persistent.monika_energy_given >= 15:

        m 1wub "Wow..."

        m 3hub "You've brought me energy drinks a lot lately!"

    hide energy_drink_bottle with dissolve

    m 1hua "Thanks, [player]~"

    return