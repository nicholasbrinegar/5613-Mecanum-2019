#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    MecanumDrive class.
'''

import wpilib
from wpilib.drive import MecanumDrive

class MyRobot(wpilib.SampleRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    frontLeftChannel = 2
    rearLeftChannel = 3
    frontRightChannel = 1
    rearRightChannel = 0

    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        '''Robot initialization function'''
        self.frontLeftMotor = wpilib.Spark(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.Spark(self.rearLeftChannel)
        self.frontRightMotor = wpilib.Spark(self.frontRightChannel)
        self.rearRightMotor = wpilib.Spark(self.rearRightChannel)

        # invert the left side motors
        self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
        self.rearLeftMotor.setInverted(True)

        self.drive = MecanumDrive(self.frontLeftMotor,
                                  self.rearLeftMotor,
                                  self.frontRightMotor,
                                  self.rearRightMotor)

        self.drive.setExpiration(0.1)

        self.stick = wpilib.Joystick(self.joystickChannel)

    def operatorControl(self):
        '''Runs the motors with Mecanum drive.'''

        self.drive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            # Use the joystick X axis for lateral movement, Y axis for forward movement, and Throttle axis for rotation.
            # This sample does not use field-oriented drive, so the gyro input is set to zero.
            self.drive.driveCartesian(self.stick.getX(),
                                      self.stick.getY(),
                                      self.stick.getThrottle(), 0);
                                                 #Changed "Z" value to "Throttle" value to control turning on the robot
            wpilib.Timer.delay(0.005)  # wait 5ms to avoid hogging CPU cycles


if __name__ == '__main__':
    wpilib.run(MyRobot)
