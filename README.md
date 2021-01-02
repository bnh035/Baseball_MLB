# Pitch Data Glossary

**type**: B - Ball, S - Strike, X - In Play

**x, y**: The horizontal and vertical location the pitch crosses home plate.

**start_speed**: the pitch speed in mph(3D) @ y0.

**end_speed**: the pitch speed measured at home plate.

**sz_top**: distance from the ground to the top of the stikezone in feet.

**sz_bot**:distance from the ground to the bottom of the strikezone in feet.

**pfx_x**: horizontal movement in, measured at y=40ft regardless of y0.

**pfx_z**: vertical movement in inches, measured at y=40ft regardless of y0.

**px**: the left/right distance in feet from the middle of the plate. Right from the catchers perspective is positive.

**pz**: the height of the pitch in feet as it crosses home plate.

**x0, y0, z0**: the initial x, y, z position.

**vx0, vy0, vz0**: the initial pitch velocity.

**ax, ay, az**: initial acceleration of the pitch.

**break_y**: the distance from y0 that the pitch deviates from a straight line between the initial point and the point it crosses the front of home plate.

**break_angle**: the angle in degrees from vertical to straight that the pitch deviates from a straight line from the release point.

**break_length**: the greatest distance from the pitch to a straight line between the release point and the point it crosses the front of home plate.

**sv_id**: most probable pitch type according to a NN-classification algorithm.

**type_confidence**: weight of the output node corresponding to the most probable pitch_type. This value is multiplied by 1.5 if the pitch is known by MLBAM to be in the pitchers repertoire.
