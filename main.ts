input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    reading = pins.analogReadPin(DigitalPin.P0)
    voltage = Math.round(reading * 3300 / 1023)
    Tvoltage = voltage / 1000
    decimal = Tvoltage / 3
    percentage = Math.round(decimal * 100)
    basic.showString("" + ("" + percentage) + "%")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    dial = fwdSensors.dial1.fwdPosition()
    moisture = moisture + dial
    basic.showString("Moisture Level:" + ("" + moisture))
})
let dial = 0
let percentage = 0
let decimal = 0
let Tvoltage = 0
let voltage = 0
let reading = 0
let moisture = 0
moisture = 20
loops.everyInterval(120000, function on_every_interval() {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    fwdSensors.ledRing.fwdSetAllPixelsColour(0x000000)
    fwdSensors.ledRing.fwdSetPixelColour(0, 0xff0000)
    while (fwdSensors.soilMoisture1.fwdIsMoistureLevelPastThreshold(moisture, fwdSensors.ThresholdDirection.Under)) {
        fwdSensors.ledRing.fwdRotate(1)
        fwdMotors.pump.fwdTimedRun(500)
        basic.pause(1000)
    }
    fwdSensors.ledRing.fwdSetAllPixelsColour(0x00ff00)
})
