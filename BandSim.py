# BandSim!
# 12/15/17-1/24/18
# Ian Anderson
# A game about rhythm and timing with preset or random mode
# imports
import pygame
import numpy
import random
# colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BRASS_GOLD = (216, 164, 73)
BRASS_SILVER = (213, 214, 216)
BRASS_BRONZE = (173, 120, 81)
# note pitch and length constants
NOTE_LENGTHS = {"WholeNote": 1, "HalfNote": 2, "QuarterNote": 4, "EighthNote": 8, "SixteenthNote": 16}
NOTE_PITCHES = {"C4": 262, "Db4": 277, "D4": 294, "Eb4": 311, "E4": 330, "F4": 349, "Gb4": 370, "G4": 392, "Ab4": 415
                , "A4": 440, "Bb4": 466, "B4": 494, "C5": 523, "Db5": 554, "D5": 587, "Eb5": 622, "E5": 659, "F5": 698
                , "Gb5": 740, "G5": 784, "Ab5": 831, "A5": 880, "Bb5": 932, "B5": 988, "C6": 1047}
TRUMPET_FINGERINGS_CONCERT = {"C3": 13, "Db3": 23, "D3": 12, "Eb3": 1, "E3": 2, "F3": 0, "Gb3": 23, "G3": 12, "Ab3": 1
                              , "A3": 2, "Bb3": 0, "B3": 12, "C4": 1, "Db4": 2, "D4": 0, "Eb4": 1, "E4": 2, "F4": 0
                              , "Gb4": 23, "G4": 12, "Ab4": 1, "A4": 2, "Bb4": 0, "B4": 12, "C5": 1}
HORN_FINGERINGS_CONCERT = {"C3": 0, "Db3": 23, "D3": 12, "Eb3": 1, "E3": 2, "F3": 0, "Gb3": 12, "G3": 1, "Ab3": 2
                              , "A3": 0, "Bb3": 1, "B3": 2, "C4": 0, "Db4": 23, "D4": 12, "Eb4": 1, "E4": 2, "F4": 0
                              , "Gb4": 12, "G4": 1, "Ab4": 2, "A4": 0, "Bb4": 1, "B4": 2, "C5": 0}
# the preset song, shown with its four voices
SONG_VOICE1_PITCH = ["E5", "D5", "E5", "D5",
                     "C5", "D5", "C5", "B4",
                     "A4", "C5", "G4", "A4",
                     "F4", "G4", "A4", "B4",
                     "C5", "D5", "E5", "D5",
                     "C5", "B4", "A4", "G4",
                     "A4", "E5", "C5", "D5",
                     "A4", "D5", "C5", "E5"]
SONG_VOICE1_LENGTH = ["QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote"]
SONG_VOICE2_PITCH = ["D5", "E5", "C5", "A4",
                     "F4", "E4", "D4", "C5",
                     "B4", "C5", "D5", "E5",
                     "D5", "C5", "D4", "B4",
                     "G4", "A4", "B4", "C5",
                     "D5", "D4", "G4", "A4",
                     "B4", "C5", "D5", "E5",
                     "D4", "E4", "F4", "G4"]
SONG_VOICE2_LENGTH = ["QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote"]
SONG_VOICE3_PITCH = ["D4", "F4", "D5", "B4",
                     "A4", "G4", "F4", "E4",
                     "D4", "E4", "F4", "G4",
                     "E5", "D5", "C5", "B4",
                     "D5", "C5", "E4", "F4",
                     "B4", "C5", "D4", "D5",
                     "D5", "B4", "C5", "D5",
                     "D5", "G4", "F4", "E4"]
SONG_VOICE3_LENGTH = ["QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote"]
SONG_VOICE4_PITCH = ["A4", "B4", "C5", "D5",
                     "G4", "F4", "E4", "D4",
                     "D5", "E5", "C5", "B4",
                     "C5", "B4", "A4", "F4",
                     "G4", "F4", "E4", "D5",
                     "D4", "E4", "B4", "A4",
                     "G4", "F4", "D5", "E4",
                     "E5", "D5", "D4", "E4"]
SONG_VOICE4_LENGTH = ["QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote",
                      "QuarterNote", "QuarterNote", "QuarterNote", "QuarterNote"]
# random length and pitches
POSSIBLE_PITCHES = ["E5", "D5", "C5", "B4", "A4", "G4", "F4", "E4", "D4"]
POSSIBLE_LENGTH = ["WholeNote", "HalfNote", "QuarterNote", "EighthNote", "SixteenthNote"]


def noteMoveSpeedCalc():
    """Calculates note movement speed based on bpm"""
    noteMoveSpeedGen = 3*(bpm/60)
    for length in NOTE_LENGTHS:
        NOTE_LENGTHS[length] = (60000 / bpm) / NOTE_LENGTHS[length]
    for length in NOTE_LENGTHS:
        NOTE_LENGTHS[length] = int(NOTE_LENGTHS[length])
    for length in NOTE_LENGTHS:
        print(NOTE_LENGTHS[length])
    return noteMoveSpeedGen

def userSelect():
    """User selects a choice."""
    user_choice = input()
    return user_choice
def noteDrawer(NotePitch, NoteType, Xcoord, Ycoord, Xscalar):
    """Draws notes."""
    if NoteType is "WholeNote":
        if NotePitch is "E5":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 7), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "D5":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 25), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 32), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "C5":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 50), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 57), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "B4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 75), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 82), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "A4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 100), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 107), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "G4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 125), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 132), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "F4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 150), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 157), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "E4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 175), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 182), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "D4":
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 200), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 207), (Xcoord - 50, Ycoord - 55)], 21)
    elif NoteType is "HalfNote":
        if NotePitch is "E5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 60)], [(Xcoord + 50 + Xscalar), (Ycoord + 40)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 7), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "D5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 35)], [(Xcoord + 50 + Xscalar), (Ycoord + 65)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 25), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 32), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "C5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 10)], [(Xcoord + 50 + Xscalar), (Ycoord + 90)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 50), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 57), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "B4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 15)], [(Xcoord + 50 + Xscalar), (Ycoord + 115)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 75), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 82), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "A4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 40)], [(Xcoord + 50 + Xscalar), (Ycoord + 140)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 100), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 107), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "G4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 65)], [(Xcoord + 50 + Xscalar), (Ycoord + 165)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 125), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 132), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "F4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 90)], [(Xcoord + 50 + Xscalar), (Ycoord + 190)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 150), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 157), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "E4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 115)], [(Xcoord + 50 + Xscalar), (Ycoord + 215)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 175), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 182), (Xcoord - 50, Ycoord - 55)], 21)
        elif NotePitch is "D4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 140)], [(Xcoord + 50 + Xscalar), (Ycoord + 240)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 200), (Xcoord - 37, Ycoord - 42)], 0)
            pygame.draw.ellipse(screen, WHITE, [(Xcoord + 7 + Xscalar, Ycoord + 207), (Xcoord - 50, Ycoord - 55)], 21)
    elif NoteType is "QuarterNote":
        if NotePitch is "E5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 60)], [(Xcoord + 50 + Xscalar), (Ycoord + 40)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "D5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 35)], [(Xcoord + 50 + Xscalar), (Ycoord + 65)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 25), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "C5":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord - 10)], [(Xcoord + 50 + Xscalar), (Ycoord + 90)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 50), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "B4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 15)], [(Xcoord + 50 + Xscalar), (Ycoord + 115)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 75), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "A4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 40)], [(Xcoord + 50 + Xscalar), (Ycoord + 140)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 100), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "G4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 65)], [(Xcoord + 50 + Xscalar), (Ycoord + 165)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 125), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "F4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 90)], [(Xcoord + 50 + Xscalar), (Ycoord + 190)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 150), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "E4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 115)], [(Xcoord + 50 + Xscalar), (Ycoord + 215)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 175), (Xcoord - 37, Ycoord - 42)], 0)
        elif NotePitch is "D4":
            pygame.draw.line(screen, BLACK, [(Xcoord + 50 + Xscalar), (Ycoord + 140)], [(Xcoord + 50 + Xscalar), (Ycoord + 240)], 10)
            pygame.draw.ellipse(screen, BLACK, [(Xcoord + Xscalar, Ycoord + 200), (Xcoord - 37, Ycoord - 42)], 0)
    elif NoteType is "EighthNote":
        print()
    elif NoteType is "SixteenthNote":
        print()
def noteMover(NotePitch, NoteType, baseNoteX, baseNoteY, noteStartPos):
    """Moves notes."""
    global gameType
    global totalNotes
    global totalNotesSpeed
    global noteGot
    global score
    score = 0

    if noteStartPos > 0:
        noteDrawer(NotePitch, NoteType, baseNoteX, baseNoteY, noteStartPos)
        pygame.time.delay(2)
    if pygame.key.get_focused() is True:
        keyPress = pygame.key.get_pressed()
        if 0 <= noteStartPos <= 25:
            print(pygame.key.get_mods())
            if NoteType is "D4":
                if keyPress == pygame.K_1:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "E4":
                if event.key == pygame.K_2:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "F4":
                if event.key == pygame.K_3:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "G4":
                if event.key == pygame.K_4:
                    noteGot = True1
                else:
                    noteGot = False
            elif NoteType is "A4":
                if event.key == pygame.K_5:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "B4":
                if event.key == pygame.K_6:
                    noteGot = True
                else:
                    noteGot = FalseBB
            elif NoteType is "C5":
                if event.key == pygame.K_7:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "D5":
                if event.key == pygame.K_8:
                    noteGot = True
                else:
                    noteGot = False
            elif NoteType is "E5":
                if event.key == pygame.K_9:
                    noteGot = True
                else:
                    noteGot = False
    else:
        noteGot = False
    pygame.event.poll()
    if noteStartPos <= 0:
        if gameType is "Main":
            totalNotes -= 1
        if gameType is "Random":
            totalNotes += 1
            totalNotesSpeed += 1
        if noteGot is True:
            score += 1
        if noteGot is False:
            score -= 1
        if noteGot is None:
            print()
        # note playing
        localWave = pygame.sndarray.make_sound(sineWaveGen(NOTE_PITCHES.get(NotePitch)))
        localWave.play(-1)
        pygame.time.delay(1000)
        localWave.stop()
    return noteStartPos
def barLineDrawMover(barStartPos):
    """Draws and moves barlines."""
    global gameType
    global totalMeasures
    if barStartPos > 100:
        pygame.draw.line(screen, BLACK, (barStartPos, 50), (barStartPos, 350), 5)
    if barStartPos <= 100:
        if gameType is "Main":
            totalMeasures -= 1
        elif gameType is "Random":
            totalMeasures += 1
    return barStartPos
def staffDrawer():
    """Draws staff."""
    staffCount = 0
    staffX = 100
    staffY = 100
    while staffCount != 5:
        pygame.draw.line(screen, BLACK, (50, staffY), (850, staffY), 5)
        staffY += 50
        staffCount += 1
    staffCount = 0
    while staffCount != 2:
        pygame.draw.line(screen, BLACK, (staffX, 50), (staffX, 350), 5)
        staffX += 60
        staffCount += 1
def sineWaveGen(hz):
    """Generate sine wave for playback."""
    realTime = numpy.linspace(0, 1, 44100)
    waveForm = (numpy.sin(2 * numpy.pi * hz * realTime) * 10000).astype(numpy.int16)
    return waveForm
def titleScreen():
    """Draws title screen."""
    screen.fill(WHITE)
def noteSelector(noteLineNum):
    """Advances note."""
    global SONG_VOICE1_PITCH
    global SONG_VOICE2_PITCH
    global SONG_VOICE3_PITCH
    global SONG_VOICE4_PITCH
    if SONG_VOICE1_PITCH[0] is "END":
        print("GAME END")
    else:
        if noteLineNum is 1:
            nextNote = SONG_VOICE1_PITCH[0]
            del SONG_VOICE1_PITCH[0]
        elif noteLineNum is 2:
            nextNote = SONG_VOICE2_PITCH[0]
            del SONG_VOICE2_PITCH[0]
        elif noteLineNum is 3:
            nextNote = SONG_VOICE2_PITCH[0]
            del SONG_VOICE2_PITCH[0]
        elif noteLineNum is 4:
            nextNote = SONG_VOICE2_PITCH[0]
            del SONG_VOICE2_PITCH[0]
    return nextNote
TotalTime = 0
# selection of game mode
gameType = "Main"
# bpm = int(input("Enter your BPM that you want the song to play"))
bpm = 60
noteGot = None
# totalNotes = int(input("Enter the amount of notes you want to play"))
# counting up or down
if gameType is "Main":
    totalNotes = 128
    totalMeasures = 32
elif gameType is "Random":
    totalNotes = 0
    totalMeasures = 0
    totalNotesSpeed = 0


# TimeSigTop = int(input("Enter the top number for your time signature."))
# TimeSigBottom = int(input("Enter the bottom number for your time signature."))
# TimeSigTopStr = str(TimeSigTop)
# TimeSigBottomStr = str(TimeSigBottom
TimeSigTopStr = "4"
TimeSigBottomStr = "4"
baseNoteX = 98
baseNoteY = 98
# initial note speed
noteMoveSpeed = noteMoveSpeedCalc()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BandSim 1.0")
# initializing pygame font and mixer
pygame.font.init()
pygame.mixer.init(44100, -16, 1, 1024)
clock = pygame.time.Clock()
done = False
# base note positions
noteStartPos = 798
noteStartPos2 = 600
noteStartPos3 = 402
noteStartPos4 = 198
barStartPos = 1035
# generating text
gameFont = pygame.font.SysFont("arial", 50)
largeFont = pygame.font.SysFont("arial", 125)
BPMStr = str(bpm)
BPMDisplay = gameFont.render(BPMStr, 0, BLACK)
BPMWords = gameFont.render("BPM", 0, BLACK)
TimeSigTopDisplay = largeFont.render(TimeSigTopStr, 0, BLACK)
TimeSigBottomDisplay = largeFont.render(TimeSigBottomStr, 0, BLACK)
# preset notes for main or random notes for random
if gameType is "Main":
    NotesLeftText = gameFont.render("Notes Left - ", 0, BLACK)
    MeasuresLeftText = gameFont.render("Measures Left - ", 0, BLACK)
    rightNowNote1 = "D4"
    rightNowLength1 = "QuarterNote"
    rightNowNote2 = "E4"
    rightNowLength2 = "QuarterNote"
    rightNowNote3 = "F4"
    rightNowLength3 = "QuarterNote"
    rightNowNote4 = "G4"
    rightNowLength4 = "QuarterNote"
elif gameType is "Random":
    NotesLeftText = gameFont.render("Notes Done - ", 0, BLACK)
    MeasuresLeftText = gameFont.render("Measures Done - ", 0, BLACK)
    rightNowNote1 = random.choice(POSSIBLE_PITCHES)
    rightNowLength1 = "QuarterNote"
    rightNowNote2 = random.choice(POSSIBLE_PITCHES)
    rightNowLength2 = "QuarterNote"
    rightNowNote3 = random.choice(POSSIBLE_PITCHES)
    rightNowLength3 = "QuarterNote"
    rightNowNote4 = random.choice(POSSIBLE_PITCHES)
    rightNowLength4 = "QuarterNote"
notePos1Num = 0
notePos2Num = 0
notePos3Num = 0
notePos4Num = 0
barNum = 0
speedFix = 98
# minor fix for faster gameplay
if bpm is 120:
    speedFix = 96
while not done:
    # --- Main event loop322221
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    timeNow = clock.tick(60)
    SecondTime = timeNow / 1000
    SecondTime = int(SecondTime)
    TotalTime += timeNow / 1000
    screen.fill(WHITE)
    NotesLeftStr = str(totalNotes)
    MeasuresLeftStr = str(totalMeasures)
    # Drawing Staff
    staffDrawer()
    # generate notes left text based on actual number
    NotesLeftNum = gameFont.render(NotesLeftStr, 0, BLACK)
    MeasuresLeftNum = gameFont.render(MeasuresLeftStr, 0, BLACK)
    screen.blit(BPMDisplay, (110, 50))
    screen.blit(BPMWords, (165, 50))
    screen.blit(NotesLeftText, (200, 400))
    screen.blit(NotesLeftNum, (425, 400))
    screen.blit(MeasuresLeftText, (200, 450))
    screen.blit(MeasuresLeftNum, (500, 450))
    screen.blit(TimeSigTopDisplay, (50, 80))
    screen.blit(TimeSigBottomDisplay, (50, 180))
    # bar movement with reset
    barStartPos = barLineDrawMover(barStartPos)
    barStartPos -= noteMoveSpeed
    if barStartPos <= speedFix:
        barStartPos = 895
    # first note movement
    noteMover(rightNowNote1, rightNowLength1, baseNoteX, baseNoteY, noteStartPos)
    noteStartPos -= noteMoveSpeed
    if noteStartPos <= -1:
        noteStartPos = 798
        if gameType is "Main":
            rightNowNote1 = noteSelector(1)
        elif gameType is "Random":
            rightNowNote1 = random.choice(POSSIBLE_PITCHES)
        notePos1Num += 1
    # second note movement
    noteStartPos2 = noteMover(rightNowNote2, rightNowLength2, baseNoteX, baseNoteY, noteStartPos2)
    noteStartPos2 -= noteMoveSpeed
    if noteStartPos2 <= -1:
        noteStartPos2 = 798
        if gameType is "Main":
            rightNowNote2 = noteSelector(2)
        elif gameType is "Random":
            rightNowNote2 = random.choice(POSSIBLE_PITCHES)
        notePos2Num += 1
    # third note movement
    noteStartPos3 = noteMover(rightNowNote3, rightNowLength3, baseNoteX, baseNoteY, noteStartPos3)
    noteStartPos3 -= noteMoveSpeed
    if noteStartPos3 <= -1:
        noteStartPos3 = 798
        if gameType is "Main":
            rightNowNote3 = noteSelector(3)
        elif gameType is "Random":
            rightNowNote3 = random.choice(POSSIBLE_PITCHES)
        notePos3Num += 1
    # fourth note movement
    noteStartPos4 = noteMover(rightNowNote4, rightNowLength4, baseNoteX, baseNoteY, noteStartPos4)
    noteStartPos4 -= noteMoveSpeed
    if noteStartPos4 <= -1:
        noteStartPos4 = 798
        if gameType is "Main":
            rightNowNote4 = noteSelector(4)
        elif gameType is "Random":
            rightNowNote4 = random.choice(POSSIBLE_PITCHES)
        notePos4Num += 1



    # noteDrawer("B3", baseNoteX + 25, baseNoteY + 25)
    pygame.display.flip()
    # testing code
    # print(SecondTime)
    # print(TotalTime)



