$fn = 50;


difference() {
	union() {
		hull() {
			cylinder(h = 9, r = 5);
			cylinder(h = 9, r = 5);
			cylinder(h = 9, r = 5);
			cylinder(h = 9, r = 5);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						linear_extrude(height = 4.7500000000) {
							polygon(points = [[5.7892500000, 0.0000000000], [2.8946250000, 5.0136375689], [-2.8946250000, 5.0136375689], [-5.7892500000, 0.0000000000], [-2.8946250000, -5.0136375689], [2.8946250000, -5.0136375689]]);
						}
					}
					union();
				}
			}
		}
	}
}