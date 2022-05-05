import RPi.GPIO as gpio
import time


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
leds = [ 21, 20, 16, 12, 7, 8, 25, 24 ]
comp = 4
troyka = 17
Vref = 3.3
bit = 8 #разрядность

gpio.setmode( gpio.BCM )
gpio.setup( dac, gpio.OUT, initial=gpio.LOW )
gpio.setup( leds, gpio.OUT, initial=gpio.LOW )
gpio.setup( troyka, gpio.OUT, initial=gpio.HIGH )
gpio.setup( comp, gpio.IN )


def decimal2binary( value ):
    return [int(bit) for bit in bin( value ) [2:].zfill( bit )]

def adc():
    retvalue = 0
    decVtest = 0
    for testbit in reversed( range( bit ) ):
        decVtest = retvalue + 2 ** testbit
        gpio.output( dac, decimal2binary( decVtest ) )
        time.sleep( 0.0001 )
        compsignal = gpio.input( comp )

        if compsignal == 1: #если значение на ЦАП не больше исследуемого
            retvalue += 2 ** testbit

    return retvalue


try:
    while True:
        decVfind = adc()
        binVfind = decimal2binary( decVfind )

        volume = round( decVfind / ( 2 ** bit ) * bit ) #"громкость "
        gpio.output( leds[:volume], 1 )
        gpio.output( leds[volume:], 0 )

        print('decimal V = {}'.format( decVfind ))
        print('binary V = {}'.format( binVfind ))
        print('V = {}'.format( decVfind / ( 2 ** bit ) * Vref ))
        print( '' )
        #time.sleep( 1 )


finally:
    gpio.output( dac + leds + [troyka], 0 )
    gpio.cleanup()