$fn = 50;


difference() {
	union() {
		hull() {
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
		}
	}
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						linear_extrude(height = 2.2500000000) {
							polygon(points = [[3.3370000000, 0.0000000000], [1.6685000000, 2.8899267724], [-1.6685000000, 2.8899267724], [-3.3370000000, 0.0000000000], [-1.6685000000, -2.8899267724], [1.6685000000, -2.8899267724]]);
						}
					}
					union();
				}
			}
		}
	}
}