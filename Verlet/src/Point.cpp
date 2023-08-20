#include "Point.h"
#include "Screen.h"
using namespace std;

namespace Erhan {

Point::Point(double posx, double posy, int radius, int color, bool pinned, Screen screen) :
		radius(radius), color(color), posx(posx), posy(posy), oldPosx(posx), oldPosy(posy), accx(0), accy(0), pinned(pinned), screen(screen) {
}

Point::Point(double posx, double posy, double oldPosx, double oldPosy, int radius, int color, bool pinned, Screen screen) :
		radius(radius), color(color), posx(posx), posy(posy), oldPosx(oldPosx), oldPosy(oldPosy), accx(0), accy(0), pinned(pinned), screen(
				screen) {
}

void Point::update(double dt) {
	accy += gravity;
	double velx = posx - oldPosx;
	double vely = posy - oldPosy;
	oldPosx = posx;
	oldPosy = posy;
	posx = posx + velx + accx * dt * dt;
	posy = posy + vely + accy * dt * dt;
	accy=0;
}

void Point::draw() {
	screen.drawCircle(posx, posy, radius, color);
}

}
