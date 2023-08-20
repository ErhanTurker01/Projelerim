/*
 * Stick.cpp
 *
 *  Created on: Apr 6, 2023
 *      Author: erhanturker
 */

#include "Stick.h"

namespace Erhan {
double distance(Point p1, Point p2) {
	return sqrt(pow(p1.posx - p2.posx, 2) + pow(p1.posy - p2.posy, 2));
}
Stick::Stick(Point *p1, Point *p2, double bounce, int color, bool tearable, double tearval) :
		p1(p1), p2(p2), bounce(bounce), color(color), tearable(tearable), tearval(tearval) {
	lenght = distance(*p1, *p2);
	tear = false;
}

void Stick::applyForce() {
	double dx = p2->posx - p1->posx;
	double dy = p2->posy - p1->posy;
	double dist = sqrt(dx * dx + dy * dy);
	double diff = lenght - dist;
	double percent = (diff / dist) / 2;
	double offSetX = dx * percent;
	double offSetY = dy * percent;
	double bounc = bounce * 10;
	if (bounc != 10) {
		bounc = (pow(3, bounc) - 1) / pow(3, bounc);
	} else {
		bounc /= 10;
	}
	if (!p2->pinned) {
		p2->posx += offSetX * (1 - bounc);
		p2->posy += offSetY * (1 - bounc);
	}
	if (!p1->pinned) {
		p1->posx -= offSetX * (1 - bounc);
		p1->posy -= offSetY * (1 - bounc);
	}
}

void Stick::drawStick(Screen screen) {
	double x1 = p1->posx;
	double x2 = p2->posx;
	double y1 = p1->posy;
	double y2 = p2->posy;

	const bool steep = (fabs(y2 - y1) > fabs(x2 - x1));
	if (steep) {
		std::swap(x1, y1);
		std::swap(x2, y2);
	}

	if (x1 > x2) {
		std::swap(x1, x2);
		std::swap(y1, y2);
	}

	const float dx = x2 - x1;
	const float dy = fabs(y2 - y1);

	float error = dx / 2.0f;
	const int ystep = (y1 < y2) ? 1 : -1;
	int y = (int) y1;

	const int maxX = (int) x2;

	for (int x = (int) x1; x < maxX; x++) {
		if (steep) {
			screen.setPixel(y, x, color);
		} else {
			screen.setPixel(x, y, color);
		}

		error -= dy;
		if (error < 0) {
			y += ystep;
			error += dx;
		}
	}
}

}
