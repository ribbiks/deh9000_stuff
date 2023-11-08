from deh9000 import *

# thanks to fraggle, deh9000 is rad
# thanks to esselfortium, many parts of this script were adapted from kdikdizd-deh.py

mobjinfo[MT_KEEN].clear_states()       # commander keen
mobjinfo[MT_WOLFSS].clear_states()     # wolfenstein ss
mobjinfo[MT_BOSSSPIT].clear_states()   # bossbrain spawner
mobjinfo[MT_BOSSTARGET].clear_states() # bossbrain spawn spot
mobjinfo[MT_SPAWNSHOT].clear_states()  # bossbrain spawn cube
mobjinfo[MT_SPAWNFIRE].clear_states()  # bossbrain spawn fire
#
#weaponinfo[wp_chainsaw].clear_states() # chainsaw
#
#mobjinfo[MT_MISC32].clear_states()     # tall green column    COL1   X
#mobjinfo[MT_MISC33].clear_states()     # short green column   COL2   X
#mobjinfo[MT_MISC34].clear_states()     # tall red column      COL3   X
#mobjinfo[MT_MISC35].clear_states()     # short red column     COL4   X
#mobjinfo[MT_MISC36].clear_states()     # column with skull    COL6   X  yes COL5 / COL6 sprite names are ordered backwards
#mobjinfo[MT_MISC37].clear_states()     # coolumn with heart   COL5   X
#
# blocking hanging decorations
#
#mobjinfo[MT_MISC51].clear_states()     # swaying body         GOR1   X
#mobjinfo[MT_MISC52].clear_states()     # hanging arms out     GOR2   X
#mobjinfo[MT_MISC53].clear_states()     # one-legged body      GOR3   X
#mobjinfo[MT_MISC54].clear_states()     # hanging torso        GOR4   X
#mobjinfo[MT_MISC55].clear_states()     # hanging leg          GOR5   X
#mobjinfo[MT_MISC65].clear_states()     # dead lost soul              X
#
# some state salvaging courtesy of deh9000's reclaim.py
states[S_FATSHOTX1].nextstate = S_EXPLODE2
states[S_SMOKE2].nextstate = S_PUFF2
mobjinfo[MT_IFOG].spawnstate = S_TFOG4

# relocate mastermind to dead lost soul thingid
#
m = mobjinfo[MT_MISC65]
m.spawnhealth = 3000
m.speed = 12
m.radius = 128 * FRACUNIT
m.height = 100 * FRACUNIT
m.damage = 0
m.reactiontime = 8
m.painchance = 40
m.mass = 1000
m.flags = (MF_SOLID | MF_SHOOTABLE | MF_COUNTKILL)
m.seesound = 45
m.attacksound = 2
m.painsound = 26
m.deathsound = 69
m.activesound = 77
#
# use the ss sprites for greencyb
#
m.update(states.parse("""
  Spawn:
    SSWV AB 10 A_Look
    Loop
  See:
    SSWV A 3 A_Hoof
    SSWV ABBCC 3 A_Chase
    SSWV D 3 A_Metal
    SSWV D 3 A_Chase
    Loop
  Missile:
    SSWV E 6 A_FaceTarget
    SSWV F 12 A_CyberAttack
    SSWV E 12 A_FaceTarget
    SSWV F 12 A_CyberAttack
    SSWV E 12 A_FaceTarget
    SSWV F 12 A_CyberAttack
    Goto See
  Pain:
    SSWV G 10 A_Pain
    Goto See
  Death:
    SSWV H 10
    SSWV I 10 A_Scream
    SSWV JKL 10
    SSWV M 10 A_Fall
    SSWV NO 10
    SSWV P 30
    SSWV P -1 A_BossDeath
    Stop
"""))
#
# point mastermind states to greencyb
#
m2 = mobjinfo[MT_SPIDER]
m2.spawnhealth = 1000
m2.speed = 16
m2.radius = 40 * FRACUNIT
m2.height = 110 * FRACUNIT
m2.damage = 0
m2.reactiontime = 8
m2.painchance = 20
m2.mass = 1000
m2.flags = (MF_SOLID | MF_SHOOTABLE | MF_COUNTKILL)
m2.seesound = 44
m2.attacksound = 0
m2.painsound = 26
m2.deathsound = 68
m2.activesound = 77
m2.spawnstate = m.spawnstate
m2.seestate = m.seestate
m2.painstate = m.painstate
m2.meleestate = m.meleestate
m2.missilestate = m.missilestate
m2.deathstate = m.deathstate
m2.xdeathstate = m.xdeathstate
m2.raisestate = m.raisestate
#
# manually reassign dead lost soul state pointers back to mastermind
#
m.spawnstate = 601   # spawn
m.seestate = 603     # walk
m.painstate = 619    # pain
m.meleestate = 0     # melee
m.missilestate = 615 # attack
m.deathstate = 621   # death
m.xdeathstate = 0    # explode
m.raisestate = 0     # raise

##### chandelier 1
#####
####m = mobjinfo[MT_MISC32]
####m.radius = 16 * FRACUNIT
####m.flags = (MF_SPAWNCEILING | MF_NOGRAVITY)
####m.spawnhealth = 10000
####m.height = 64 * FRACUNIT
####m.mass = 1000
####m.update(states.parse("""
####  Spawn:
####    COL1 ABC 4 Bright
####    Loop
####"""))

# I changed my mind, the gray chandelier is ugly, lets use its frames for a soulsphere recolor instead
# -- btw, this one doesn't count towards item% because I'm using it in randomizers
# -- since this is free I'm also going to use COL1 as a blank sprite, since COL1 was causing problems (possible deh9000 bug?)
#
m = mobjinfo[MT_MISC32]
m.radius = 20 * FRACUNIT
m.height = 16 * FRACUNIT
m.flags = MF_SPECIAL
m.mass = 1000
m.update(states.parse("""
  Spawn:
    SOUL EFGHGF 6 Bright
    Loop
"""))

# chandelier 2
#
m = mobjinfo[MT_MISC33]
m.radius = 16 * FRACUNIT
m.flags = (MF_SPAWNCEILING | MF_NOGRAVITY)
m.spawnhealth = 10000
m.height = 64 * FRACUNIT
m.mass = 1000
m.update(states.parse("""
  Spawn:
    COL2 ABC 4 Bright
    Loop
"""))

# chandelier 3 (destructible --> drops soulsphere)
#
m = mobjinfo[MT_MISC34]
m.radius = 16 * FRACUNIT
m.flags = (MF_SPAWNCEILING | MF_NOGRAVITY | MF_SHOOTABLE | MF_NOBLOOD)
m.spawnhealth = 1
m.height = 64 * FRACUNIT
m.mass = 1000
m.update(states.parse("""
  Spawn:
    COL3 ABC 4 Bright
    Loop
  Death:
    COL3 D 24 Bright
    Stop
"""))

# hexen candle 1
#
m = mobjinfo[MT_MISC54]
m.radius = 16 * FRACUNIT
m.flags = (MF_SHOOTABLE | MF_NOBLOOD)
m.spawnhealth = 1
m.height = 42 * FRACUNIT
m.mass = 1000
m.update(states.parse("""
  Spawn:
    COL4 ABC 4 Bright
    Loop
  Death:
    COL4 D 20
    COL4 D -1
    Stop
"""))

# hexen candle 2
#
m = mobjinfo[MT_MISC55]
m.radius = 16 * FRACUNIT
m.flags = (MF_SHOOTABLE | MF_NOBLOOD)
m.spawnhealth = 1
m.height = 42 * FRACUNIT
m.mass = 1000
m.update(states.parse("""
  Spawn:
    COL4 ABC 4 Bright
    Loop
  Death:
    COL4 D 20
    COL4 D -1
    Stop
"""))

# swap zombieman <---> MT_MISC54
#
# this could've been done way more elegantly but I don't care
#
(mobjinfo[MT_MISC54].doomednum,    mobjinfo[MT_POSSESSED].doomednum)    = (mobjinfo[MT_POSSESSED].doomednum,    mobjinfo[MT_MISC54].doomednum)
(mobjinfo[MT_MISC54].spawnstate,   mobjinfo[MT_POSSESSED].spawnstate)   = (mobjinfo[MT_POSSESSED].spawnstate,   mobjinfo[MT_MISC54].spawnstate)
(mobjinfo[MT_MISC54].spawnhealth,  mobjinfo[MT_POSSESSED].spawnhealth)  = (mobjinfo[MT_POSSESSED].spawnhealth,  mobjinfo[MT_MISC54].spawnhealth)
(mobjinfo[MT_MISC54].seestate,     mobjinfo[MT_POSSESSED].seestate)     = (mobjinfo[MT_POSSESSED].seestate,     mobjinfo[MT_MISC54].seestate)
(mobjinfo[MT_MISC54].seesound,     mobjinfo[MT_POSSESSED].seesound)     = (mobjinfo[MT_POSSESSED].seesound,     mobjinfo[MT_MISC54].seesound)
(mobjinfo[MT_MISC54].reactiontime, mobjinfo[MT_POSSESSED].reactiontime) = (mobjinfo[MT_POSSESSED].reactiontime, mobjinfo[MT_MISC54].reactiontime)
(mobjinfo[MT_MISC54].attacksound,  mobjinfo[MT_POSSESSED].attacksound)  = (mobjinfo[MT_POSSESSED].attacksound,  mobjinfo[MT_MISC54].attacksound)
(mobjinfo[MT_MISC54].painstate,    mobjinfo[MT_POSSESSED].painstate)    = (mobjinfo[MT_POSSESSED].painstate,    mobjinfo[MT_MISC54].painstate)
(mobjinfo[MT_MISC54].painchance,   mobjinfo[MT_POSSESSED].painchance)   = (mobjinfo[MT_POSSESSED].painchance,   mobjinfo[MT_MISC54].painchance)
(mobjinfo[MT_MISC54].painsound,    mobjinfo[MT_POSSESSED].painsound)    = (mobjinfo[MT_POSSESSED].painsound,    mobjinfo[MT_MISC54].painsound)
(mobjinfo[MT_MISC54].meleestate,   mobjinfo[MT_POSSESSED].meleestate)   = (mobjinfo[MT_POSSESSED].meleestate,   mobjinfo[MT_MISC54].meleestate)
(mobjinfo[MT_MISC54].missilestate, mobjinfo[MT_POSSESSED].missilestate) = (mobjinfo[MT_POSSESSED].missilestate, mobjinfo[MT_MISC54].missilestate)
(mobjinfo[MT_MISC54].deathstate,   mobjinfo[MT_POSSESSED].deathstate)   = (mobjinfo[MT_POSSESSED].deathstate,   mobjinfo[MT_MISC54].deathstate)
(mobjinfo[MT_MISC54].xdeathstate,  mobjinfo[MT_POSSESSED].xdeathstate)  = (mobjinfo[MT_POSSESSED].xdeathstate,  mobjinfo[MT_MISC54].xdeathstate)
(mobjinfo[MT_MISC54].deathsound,   mobjinfo[MT_POSSESSED].deathsound)   = (mobjinfo[MT_POSSESSED].deathsound,   mobjinfo[MT_MISC54].deathsound)
(mobjinfo[MT_MISC54].speed,        mobjinfo[MT_POSSESSED].speed)        = (mobjinfo[MT_POSSESSED].speed,        mobjinfo[MT_MISC54].speed)
(mobjinfo[MT_MISC54].radius,       mobjinfo[MT_POSSESSED].radius)       = (mobjinfo[MT_POSSESSED].radius,       mobjinfo[MT_MISC54].radius)
(mobjinfo[MT_MISC54].height,       mobjinfo[MT_POSSESSED].height)       = (mobjinfo[MT_POSSESSED].height,       mobjinfo[MT_MISC54].height)
(mobjinfo[MT_MISC54].mass,         mobjinfo[MT_POSSESSED].mass)         = (mobjinfo[MT_POSSESSED].mass,         mobjinfo[MT_MISC54].mass)
(mobjinfo[MT_MISC54].damage,       mobjinfo[MT_POSSESSED].damage)       = (mobjinfo[MT_POSSESSED].damage,       mobjinfo[MT_MISC54].damage)
(mobjinfo[MT_MISC54].activesound,  mobjinfo[MT_POSSESSED].activesound)  = (mobjinfo[MT_POSSESSED].activesound,  mobjinfo[MT_MISC54].activesound)
(mobjinfo[MT_MISC54].flags,        mobjinfo[MT_POSSESSED].flags)        = (mobjinfo[MT_POSSESSED].flags,        mobjinfo[MT_MISC54].flags)
(mobjinfo[MT_MISC54].raisestate,   mobjinfo[MT_POSSESSED].raisestate)   = (mobjinfo[MT_POSSESSED].raisestate,   mobjinfo[MT_MISC54].raisestate)

# swap sergeant <---> MT_MISC55
#
(mobjinfo[MT_MISC55].doomednum,    mobjinfo[MT_SHOTGUY].doomednum)    = (mobjinfo[MT_SHOTGUY].doomednum,    mobjinfo[MT_MISC55].doomednum)
(mobjinfo[MT_MISC55].spawnstate,   mobjinfo[MT_SHOTGUY].spawnstate)   = (mobjinfo[MT_SHOTGUY].spawnstate,   mobjinfo[MT_MISC55].spawnstate)
(mobjinfo[MT_MISC55].spawnhealth,  mobjinfo[MT_SHOTGUY].spawnhealth)  = (mobjinfo[MT_SHOTGUY].spawnhealth,  mobjinfo[MT_MISC55].spawnhealth)
(mobjinfo[MT_MISC55].seestate,     mobjinfo[MT_SHOTGUY].seestate)     = (mobjinfo[MT_SHOTGUY].seestate,     mobjinfo[MT_MISC55].seestate)
(mobjinfo[MT_MISC55].seesound,     mobjinfo[MT_SHOTGUY].seesound)     = (mobjinfo[MT_SHOTGUY].seesound,     mobjinfo[MT_MISC55].seesound)
(mobjinfo[MT_MISC55].reactiontime, mobjinfo[MT_SHOTGUY].reactiontime) = (mobjinfo[MT_SHOTGUY].reactiontime, mobjinfo[MT_MISC55].reactiontime)
(mobjinfo[MT_MISC55].attacksound,  mobjinfo[MT_SHOTGUY].attacksound)  = (mobjinfo[MT_SHOTGUY].attacksound,  mobjinfo[MT_MISC55].attacksound)
(mobjinfo[MT_MISC55].painstate,    mobjinfo[MT_SHOTGUY].painstate)    = (mobjinfo[MT_SHOTGUY].painstate,    mobjinfo[MT_MISC55].painstate)
(mobjinfo[MT_MISC55].painchance,   mobjinfo[MT_SHOTGUY].painchance)   = (mobjinfo[MT_SHOTGUY].painchance,   mobjinfo[MT_MISC55].painchance)
(mobjinfo[MT_MISC55].painsound,    mobjinfo[MT_SHOTGUY].painsound)    = (mobjinfo[MT_SHOTGUY].painsound,    mobjinfo[MT_MISC55].painsound)
(mobjinfo[MT_MISC55].meleestate,   mobjinfo[MT_SHOTGUY].meleestate)   = (mobjinfo[MT_SHOTGUY].meleestate,   mobjinfo[MT_MISC55].meleestate)
(mobjinfo[MT_MISC55].missilestate, mobjinfo[MT_SHOTGUY].missilestate) = (mobjinfo[MT_SHOTGUY].missilestate, mobjinfo[MT_MISC55].missilestate)
(mobjinfo[MT_MISC55].deathstate,   mobjinfo[MT_SHOTGUY].deathstate)   = (mobjinfo[MT_SHOTGUY].deathstate,   mobjinfo[MT_MISC55].deathstate)
(mobjinfo[MT_MISC55].xdeathstate,  mobjinfo[MT_SHOTGUY].xdeathstate)  = (mobjinfo[MT_SHOTGUY].xdeathstate,  mobjinfo[MT_MISC55].xdeathstate)
(mobjinfo[MT_MISC55].deathsound,   mobjinfo[MT_SHOTGUY].deathsound)   = (mobjinfo[MT_SHOTGUY].deathsound,   mobjinfo[MT_MISC55].deathsound)
(mobjinfo[MT_MISC55].speed,        mobjinfo[MT_SHOTGUY].speed)        = (mobjinfo[MT_SHOTGUY].speed,        mobjinfo[MT_MISC55].speed)
(mobjinfo[MT_MISC55].radius,       mobjinfo[MT_SHOTGUY].radius)       = (mobjinfo[MT_SHOTGUY].radius,       mobjinfo[MT_MISC55].radius)
(mobjinfo[MT_MISC55].height,       mobjinfo[MT_SHOTGUY].height)       = (mobjinfo[MT_SHOTGUY].height,       mobjinfo[MT_MISC55].height)
(mobjinfo[MT_MISC55].mass,         mobjinfo[MT_SHOTGUY].mass)         = (mobjinfo[MT_SHOTGUY].mass,         mobjinfo[MT_MISC55].mass)
(mobjinfo[MT_MISC55].damage,       mobjinfo[MT_SHOTGUY].damage)       = (mobjinfo[MT_SHOTGUY].damage,       mobjinfo[MT_MISC55].damage)
(mobjinfo[MT_MISC55].activesound,  mobjinfo[MT_SHOTGUY].activesound)  = (mobjinfo[MT_SHOTGUY].activesound,  mobjinfo[MT_MISC55].activesound)
(mobjinfo[MT_MISC55].flags,        mobjinfo[MT_SHOTGUY].flags)        = (mobjinfo[MT_SHOTGUY].flags,        mobjinfo[MT_MISC55].flags)
(mobjinfo[MT_MISC55].raisestate,   mobjinfo[MT_SHOTGUY].raisestate)   = (mobjinfo[MT_SHOTGUY].raisestate,   mobjinfo[MT_MISC55].raisestate)

# swap chaingunner <---> tall red column
#
(mobjinfo[MT_MISC34].doomednum,    mobjinfo[MT_CHAINGUY].doomednum)    = (mobjinfo[MT_CHAINGUY].doomednum,    mobjinfo[MT_MISC34].doomednum)
(mobjinfo[MT_MISC34].spawnstate,   mobjinfo[MT_CHAINGUY].spawnstate)   = (mobjinfo[MT_CHAINGUY].spawnstate,   mobjinfo[MT_MISC34].spawnstate)
(mobjinfo[MT_MISC34].spawnhealth,  mobjinfo[MT_CHAINGUY].spawnhealth)  = (mobjinfo[MT_CHAINGUY].spawnhealth,  mobjinfo[MT_MISC34].spawnhealth)
(mobjinfo[MT_MISC34].seestate,     mobjinfo[MT_CHAINGUY].seestate)     = (mobjinfo[MT_CHAINGUY].seestate,     mobjinfo[MT_MISC34].seestate)
(mobjinfo[MT_MISC34].seesound,     mobjinfo[MT_CHAINGUY].seesound)     = (mobjinfo[MT_CHAINGUY].seesound,     mobjinfo[MT_MISC34].seesound)
(mobjinfo[MT_MISC34].reactiontime, mobjinfo[MT_CHAINGUY].reactiontime) = (mobjinfo[MT_CHAINGUY].reactiontime, mobjinfo[MT_MISC34].reactiontime)
(mobjinfo[MT_MISC34].attacksound,  mobjinfo[MT_CHAINGUY].attacksound)  = (mobjinfo[MT_CHAINGUY].attacksound,  mobjinfo[MT_MISC34].attacksound)
(mobjinfo[MT_MISC34].painstate,    mobjinfo[MT_CHAINGUY].painstate)    = (mobjinfo[MT_CHAINGUY].painstate,    mobjinfo[MT_MISC34].painstate)
(mobjinfo[MT_MISC34].painchance,   mobjinfo[MT_CHAINGUY].painchance)   = (mobjinfo[MT_CHAINGUY].painchance,   mobjinfo[MT_MISC34].painchance)
(mobjinfo[MT_MISC34].painsound,    mobjinfo[MT_CHAINGUY].painsound)    = (mobjinfo[MT_CHAINGUY].painsound,    mobjinfo[MT_MISC34].painsound)
(mobjinfo[MT_MISC34].meleestate,   mobjinfo[MT_CHAINGUY].meleestate)   = (mobjinfo[MT_CHAINGUY].meleestate,   mobjinfo[MT_MISC34].meleestate)
(mobjinfo[MT_MISC34].missilestate, mobjinfo[MT_CHAINGUY].missilestate) = (mobjinfo[MT_CHAINGUY].missilestate, mobjinfo[MT_MISC34].missilestate)
(mobjinfo[MT_MISC34].deathstate,   mobjinfo[MT_CHAINGUY].deathstate)   = (mobjinfo[MT_CHAINGUY].deathstate,   mobjinfo[MT_MISC34].deathstate)
(mobjinfo[MT_MISC34].xdeathstate,  mobjinfo[MT_CHAINGUY].xdeathstate)  = (mobjinfo[MT_CHAINGUY].xdeathstate,  mobjinfo[MT_MISC34].xdeathstate)
(mobjinfo[MT_MISC34].deathsound,   mobjinfo[MT_CHAINGUY].deathsound)   = (mobjinfo[MT_CHAINGUY].deathsound,   mobjinfo[MT_MISC34].deathsound)
(mobjinfo[MT_MISC34].speed,        mobjinfo[MT_CHAINGUY].speed)        = (mobjinfo[MT_CHAINGUY].speed,        mobjinfo[MT_MISC34].speed)
(mobjinfo[MT_MISC34].radius,       mobjinfo[MT_CHAINGUY].radius)       = (mobjinfo[MT_CHAINGUY].radius,       mobjinfo[MT_MISC34].radius)
(mobjinfo[MT_MISC34].height,       mobjinfo[MT_CHAINGUY].height)       = (mobjinfo[MT_CHAINGUY].height,       mobjinfo[MT_MISC34].height)
(mobjinfo[MT_MISC34].mass,         mobjinfo[MT_CHAINGUY].mass)         = (mobjinfo[MT_CHAINGUY].mass,         mobjinfo[MT_MISC34].mass)
(mobjinfo[MT_MISC34].damage,       mobjinfo[MT_CHAINGUY].damage)       = (mobjinfo[MT_CHAINGUY].damage,       mobjinfo[MT_MISC34].damage)
(mobjinfo[MT_MISC34].activesound,  mobjinfo[MT_CHAINGUY].activesound)  = (mobjinfo[MT_CHAINGUY].activesound,  mobjinfo[MT_MISC34].activesound)
(mobjinfo[MT_MISC34].flags,        mobjinfo[MT_CHAINGUY].flags)        = (mobjinfo[MT_CHAINGUY].flags,        mobjinfo[MT_MISC34].flags)
(mobjinfo[MT_MISC34].raisestate,   mobjinfo[MT_CHAINGUY].raisestate)   = (mobjinfo[MT_CHAINGUY].raisestate,   mobjinfo[MT_MISC34].raisestate)

# recoup normal clip / shotgun / chaingunner items (using hanging gore thingids)
prev_object_name = mobjinfo[MT_MISC51].object_name
prev_doomednum   = mobjinfo[MT_MISC51].doomednum
mobjinfo[MT_MISC51].copy_from(mobjinfo[MT_CLIP])
mobjinfo[MT_MISC51].object_name = prev_object_name
mobjinfo[MT_MISC51].doomednum   = prev_doomednum
#
prev_object_name = mobjinfo[MT_MISC52].object_name
prev_doomednum   = mobjinfo[MT_MISC52].doomednum
mobjinfo[MT_MISC52].copy_from(mobjinfo[MT_SHOTGUN])
mobjinfo[MT_MISC52].object_name = prev_object_name
mobjinfo[MT_MISC52].doomednum   = prev_doomednum
#
prev_object_name = mobjinfo[MT_MISC53].object_name
prev_doomednum   = mobjinfo[MT_MISC53].doomednum
mobjinfo[MT_MISC53].copy_from(mobjinfo[MT_CHAINGUN])
mobjinfo[MT_MISC53].object_name = prev_object_name
mobjinfo[MT_MISC53].doomednum   = prev_doomednum

# ammo clip --> mystery pickup #1
#
m = mobjinfo[MT_CLIP]
m.update(states.parse("""
  Spawn:
    STIM B 2 Bright
    BON1 E 2 Bright
    MEDI C 2 Bright
    BON2 F 2 Bright
    Loop
"""))

# shotgun --> mystery pickup #2
#
m = mobjinfo[MT_SHOTGUN]
m.update(states.parse("""
  Spawn:
    CLIP B 2 Bright
    SHEL B 2 Bright
    ROCK C 2 Bright
    SHEL C 2 Bright
    Loop
"""))

# chaingun --> soulsphere
#
mobjinfo[MT_CHAINGUN].spawnstate = mobjinfo[MT_MISC12].spawnstate

# short red col --> ambient vile noise
#
m = mobjinfo[MT_MISC35]
m.spawnhealth = 1000
m.speed = 0
m.radius = 1 * FRACUNIT
m.height = 32 * FRACUNIT
m.damage = 0
m.reactiontime = 8
m.painchance = 0
m.mass = 1000
m.flags = 0
m.seesound = 0
m.attacksound = 0
m.painsound = 0
m.deathsound = 0
m.activesound = 80
m.update(states.parse("""
  Spawn:
    COL1 A 10 A_Look
    Loop
  See:
    COL1 A 2 A_Chase
    Loop
  Pain:
    COL1 A 10
    Goto See
  Death:
    COL1 A 10
    Stop
"""))

# column with heart --> rng timing blocker
#
m = mobjinfo[MT_MISC36]
m.radius = 60 * FRACUNIT
m.update(states.parse("""
  Spawn:
    COL6 A 256 Bright
    Stop
"""))

# coolumn with skull --> uniform timing blocker
#
m = mobjinfo[MT_MISC37]
m.radius = 60 * FRACUNIT
m.update(states.parse("""
  Spawn:
    COL5 A 1 Bright
    COL5 A 127 Bright
    Stop
"""))

# zerk glowing animation
#
m = mobjinfo[MT_MISC13]
m.update(states.parse("""
  Spawn:
    PSTR AB 8
    PSTR C 8 Bright
    PSTR B 8
    Loop
"""))

# replace keen with flame spirit
#
m = mobjinfo[MT_KEEN]
m.flags = 0
m.spawnhealth = 10000
m.height = 32 * FRACUNIT
m.mass = 1000
m.update(states.parse("""
  Spawn:
    KEEN ABCDEFGHIJKLM 5 Bright
    Loop
"""))

# weapon stuff
#
ammodata[am_clip].clipammo = 20
ammodata[am_clip].maxammo  = 300
####ammodata[am_misl].clipammo = 2

weaponinfo[wp_plasma].ammo = am_clip

miscdata.initial_health = 100
miscdata.initial_bullets = 50

# replace fist with axe
#
w = weaponinfo[wp_fist]
w.clear_states()
w.update(states.parse("""
  Ready:
    PUNG A 1 Bright A_WeaponReady
    Loop
  Deselect:
    PUNG A 1 Bright A_Lower
    Loop
  Select:
    PUNG A 1 Bright A_Raise
    Loop
  Fire:
    PUNG BC 1 Bright
    COL1 A 4 Bright
  Hold:
    PUNG D 2 Bright
    PUNG E 2 Bright
    PUNG F 0 Bright A_Punch
    PUNG F 0 Bright A_Punch
    PUNG F 2 Bright A_Punch
    PUNG GH 2 Bright
    COL1 A 12 Bright
    COL1 A 0 Bright A_ReFire
    PUNG CB 2 Bright
    Goto Ready
"""))

##### redirect chainsaw states to fist
#####
####w2 = weaponinfo[wp_chainsaw]
####w2.upstate = w.upstate        # select
####w2.downstate = w.downstate    # deselect
####w2.readystate = w.readystate  # bob
####w2.atkstate = w.atkstate      # fire
####w2.flashstate = w.flashstate  # muzzle flash

# ^^ no longer needed since we're not cannibalizing chainsaw anymore

# remove flash from pistol, clean up visuals for green pistol gfx
#
states[S_PISTOL4].frame = 3
states[S_PISTOLFLASH].sprite = 138  # COL1, aka blank
states[S_PISTOLFLASH].frame  = 0
states[S_PISTOLFLASH].action = None # remove lightup

# make bossbrain silent and have it end level immediately when killed
#
states[S_BRAIN_PAIN].action = None
states[S_BRAIN_DIE1].action = A_BrainDie

# reduce candle decoration width, because reasons
#
m = mobjinfo[MT_MISC49]
m.radius = 8 * FRACUNIT

# make zerk not count towards item% because I'm using it in randomizers
m = mobjinfo[MT_MISC13]
m.flags = MF_SPECIAL

# make blood splats noclipping so they don't teleport
# - this was an issue when disposing of unused enemies
m = mobjinfo[MT_BLOOD]
m.flags = (MF_NOBLOCKMAP | MF_NOCLIP)

# strings
#
strings.GOTBERSERK = "Axe powered up!"
strings.GOTCLIP    = "Picked up an energy cell."
strings.GOTCLIPBOX = "Picked up an energy cell pack."
####strings.GOTROCKET  = "Picked up 2 rockets."
####strings.GOTROCKBOX = "Picked up a box of 10 rockets."
strings.GOTCELL    = "Picked up a BFG cell."
strings.GOTCELLBOX = "Picked up a BFG cell pack."
#
strings.GOTBLUECARD = "Picked up a green keycard."
strings.GOTBLUESKUL = "Picked up a green skull."
strings.GOTREDCARD  = "Picked up a red keycard."
strings.GOTREDSKULL = "Picked up a red skull."
strings.GOTYELWCARD = "Picked up an orange keycard."
strings.GOTYELWSKUL = "Picked up an orange skull."
strings.PD_BLUES    = "You need a green skull to open this"
strings.PD_BLUEC    = "You need a green card to open this"
strings.PD_BLUEK    = "You need a green key to open this"
strings.PD_BLUEO    = "You need a green key to activate this"
strings.PD_REDS     = "You need a red skull to open this"
strings.PD_REDC     = "You need a red card to open this"
strings.PD_REDK     = "You need a red key to open this"
strings.PD_REDO     = "You need a red key to activate this"
strings.PD_YELLOWS  = "You need an orange skull to open this"
strings.PD_YELLOWC  = "You need an orange card to open this"
strings.PD_YELLOWK  = "You need an orange key to open this"
strings.PD_YELLOWO  = "You need an orange key to activate this"

'''
[STRINGS]
GOTBERSERK = Axe powered up!
GOTCLIP = Picked up an energy cell.
GOTCLIPBOX = Picked up an energy cell pack.
GOTCELL = Picked up a BFG cell.
GOTCELLBOX = Picked up a BFG cell pack.
GOTBLUECARD = Picked up a green keycard.
GOTBLUESKUL = Picked up a green skull.
GOTREDCARD = Picked up a red keycard.
GOTREDSKULL = Picked up a red skull.
GOTYELWCARD = Picked up an orange keycard.
GOTYELWSKUL = Picked up an orange skull.
PD_BLUES = You need a green skull to open this
PD_BLUEC = You need a green card to open this
PD_BLUEK = You need a green key to open this
PD_BLUEO = You need a green key to activate this
PD_REDS = You need a red skull to open this
PD_REDC = You need a red card to open this
PD_REDK = You need a red key to open this
PD_REDO = You need a red key to activate this
PD_YELLOWS = You need an orange skull to open this
PD_YELLOWC = You need an orange card to open this
PD_YELLOWK = You need an orange key to open this
PD_YELLOWO = You need an orange key to activate this
'''

dehfile.save("ww5.deh")

print(len(dehfile.free_states()))
