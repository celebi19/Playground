
import schemdraw
import schemdraw.elements as elm



with schemdraw.Drawing(file='my_circuit10.svg') as d:
    d += elm.Resistor().right().label("R1")
    d += elm.Resistor().right().label("R2")
    d += elm.Line().down()
    d += elm.BatteryCell().left().label("V dc")
    d += elm.Line().left()
    d += elm.Line().up()
    

                                     
                                