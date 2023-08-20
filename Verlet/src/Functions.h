#ifndef FUNCTIONS_H_
#define FUNCTIONS_H_


#include <iostream>
#include <vector>
#include "Screen.h"
#include "Point.h"
#include "Stick.h"

using namespace std;
using namespace Erhan;

const double dt = 0.1;
const double bounciness = 0.7;
const double friction = 0.4;
const int wPercent = 5;
const int hPercent = 5;


void drawPoints(vector<Point> point);
void updatePoints(vector<Point> &point);
void drawSticks(vector<Stick> stick, Screen screen);
void applySticks(vector<Stick> &stick);
void solveCollisons(vector<Point> &point);
void constraint(Point &point);
double distance(Point p1, Point p2);
void checkClick(vector<Point> point);



void cupSim();
void bouncyBallSim();




#endif
