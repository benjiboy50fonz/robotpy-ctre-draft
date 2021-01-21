#!/usr/bin/env python3

import wpilib
import ctre


class MyRobot(wpilib.IterativeRobot):
    """
        This is a short sample program demonstrating how to use the basic throttle
        mode of the TalonSRX
    """

    def robotInit(self):
        # Initialie the CANCoder device, as well as the 
        # configuration for it. 
        self.cancoder = ctre.CANCoder(1)
        self.cancoderConfiguration = ctre.CANCoderConfiguration()

        # Creates a joystick for test purposes. 
        self.joystick = wpilib.Joystick(0)
        
        # This variable allows us to print one response at a time. 
        self.pressed = False

        # Configures the CANCoder to return 0-360 degrees, instead of
        # -180-180 degrees, when returning absolute position. Also,
        # set the unit string to degrees.
        self.cancoderConfiguration.absoluteSensorRange = \
            ctre.AbsoluteSensorRange.Unsigned_0_to_360
            
        self.cancoderConfiguration.unitString = \
            "Degrees"
        
        # Loads the configuration. Default units are degrees!
        self.cancoder.configAllSettings(self.cancoderConfiguration)

    def teleopInit(self):
        # Clears any sticky faults on the CANCoder upon enable.
        self.cancoder.clearStickyFaults()

    def teleopPeriodic(self):
        # Prints the values that the CANCoder can return
        # upon the press of a button, ID 1 to be exact. 
        if self.pressed and not self.joystick.getRawButton(1):
            self.pressed = False
            
        if self.joystick.getRawButton(1) and not self.pressed:
            print(
            '       Time Stamp: ' + str(self.cancoder.getLastTimestamp()) + '\n    CANCoder Data: \n\n' + '    Abs. Position: ' + 
            str(self.cancoder.getAbsolutePosition()) + '\n' + '            Units: ' + self.cancoder.getLastUnitString() + '\n' + 
            '      Bus Voltage: ' + str(self.cancoder.getBusVoltage()) +       '\n' + ' Firmware Version: ' + 
            str(self.cancoder.getFirmwareVersion()) +  '\n' + ' Mag. Field Strng: ' + str(self.cancoder.getMagnetFieldStrength()) + 
            '\n' + 'Relative Position: ' + str(self.cancoder.getPosition()) + '\n' + '         Velocity: ' + str(self.cancoder.getVelocity()) + 
            '\n'
                )
            self.pressed = True
                

if __name__ == "__main__":
    wpilib.run(MyRobot)
