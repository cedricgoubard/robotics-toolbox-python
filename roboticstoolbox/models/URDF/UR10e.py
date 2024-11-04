#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.Robot import Robot


class UR10e(Robot):
    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "ur_e_description/urdf/ur10e.xacro"
        )

        super().__init__(
            links,
            name=name.upper(),
            manufacturer="Universal Robotics",
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.qr = np.array([np.pi, 0, 0, 0, np.pi / 2, 0])
        self.qz = np.zeros(6)

        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover

    robot = UR10e()
    print(robot)
