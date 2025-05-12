def on_button_pressed_a():
    global reading, voltage, Tvoltage, decimal, percentage
    reading = pins.analog_read_pin(DigitalPin.P0)
    voltage = Math.round(reading * 3300 / 1023)
    Tvoltage = voltage / 1000
    decimal = Tvoltage / 3
    percentage = Math.round(decimal * 100)
    basic.show_string("" + str(percentage) + "%")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global dial, moisture
    dial = fwdSensors.dial1.fwd_position()
    moisture = moisture + dial
    basic.show_string("Moisture Level:" + str(moisture))
input.on_button_pressed(Button.B, on_button_pressed_b)

dial = 0
percentage = 0
decimal = 0
Tvoltage = 0
voltage = 0
reading = 0
moisture = 0
moisture = 20

def on_every_interval():
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    fwdSensors.led_ring.fwd_set_all_pixels_colour(0x000000)
    fwdSensors.led_ring.fwd_set_pixel_colour(0, 0xff0000)
    while fwdSensors.soil_moisture1.fwd_is_moisture_level_past_threshold(moisture, fwdSensors.ThresholdDirection.UNDER):
        fwdSensors.led_ring.fwd_rotate(1)
        fwdMotors.pump.fwd_timed_run(500)
        basic.pause(1000)
    fwdSensors.led_ring.fwd_set_all_pixels_colour(0x00ff00)
loops.every_interval(120000, on_every_interval)
