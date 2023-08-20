#ifndef STICK_H_
#define STICK_H_
#include "Point.h"

namespace Erhan {

class Stick {
public:
	Point *p1;
	Point *p2;
	double bounce;
	double lenght;
	int color;
	bool tear;
	bool tearable;
	double tearval;
	Stick(Point *p1, Point *p2, double bounce, int color, bool tearable, double tearval);
	void drawStick(Screen screen);
	void applyForce();
};

} /* namespace Erhan */

#endif /* STICK_H_ */
