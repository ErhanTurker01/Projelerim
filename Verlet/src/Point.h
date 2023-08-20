/*
 * Points.h
 *
 *  Created on: Apr 5, 2023
 *      Author: erhanturker
 */

#ifndef POINT_H_
#define POINT_H_
#include "Screen.h"
namespace Erhan {

class Point {
public:
	const static int gravity = 10;
	int radius;
	int color;
	double posx;
	double posy;
	double oldPosx;
	double oldPosy;
	double accx;
	double accy;
	bool pinned;
	Screen screen;
	Point(double posx, double posy, double oldPosx, double oldPosy, int radius, int color, bool pinned, Screen screen);
	Point(double posx, double posy, int radius, int color, bool pinned, Screen screen);
	void update(double dt);
	void draw();

};

} /* namespace Erhan */

#endif /* POINT_H_ */
