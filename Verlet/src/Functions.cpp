#include "Functions.h"
#include <unistd.h>
using namespace std;
using namespace Erhan;

double distance(Point p1, Point p2) {
	return sqrt(pow(p1.posx - p2.posx, 2) + pow(p1.posy - p2.posy, 2));
}

void constraint(Point &point) {
	if (point.posy > (double) Screen::HEIGHT * (100 - hPercent) / 100) {
		point.oldPosx += friction * (point.posx - point.oldPosx);
	}
	if (point.posy > (double) Screen::HEIGHT * (100 - hPercent) / 100) {
		point.oldPosy = 2 * (double) Screen::HEIGHT * (100 - hPercent) / 100 - point.oldPosy;
		point.posy = 2 * (double) Screen::HEIGHT * (100 - hPercent) / 100 - point.posy;
		point.oldPosy += (1 - bounciness) * (point.posy - point.oldPosy);
	}
	if (point.posx > (double) Screen::WIDTH * (100 - wPercent) / 100) {
		point.oldPosx = 2 * (double) Screen::WIDTH * (100 - wPercent) / 100 - point.oldPosx;
		point.posx = 2 * (double) Screen::WIDTH * (100 - wPercent) / 100 - point.posx;
		point.oldPosx += (1 - bounciness) * (point.posx - point.oldPosx);
	}
	if (point.posx < (double) Screen::WIDTH * wPercent / 100) {
		point.oldPosx = 2 * (double) Screen::WIDTH * wPercent / 100 - point.oldPosx;
		point.posx = 2 * (double) Screen::WIDTH * wPercent / 100 - point.posx;
		point.oldPosx += (1 - bounciness) * (point.posx - point.oldPosx);
	}
	if (point.posy < (double) Screen::HEIGHT * hPercent / 100) {
		point.oldPosy = 2 * (double) Screen::HEIGHT * hPercent / 100 - point.oldPosy;
		point.posy = 2 * (double) Screen::HEIGHT * hPercent / 100 - point.posy;
		point.oldPosy += (1 - bounciness) * (point.posy - point.oldPosy);
	}
}

void solveCollisons(vector<Point> &point) {
	for (int i = 0; i < point.size(); i++) {
		for (int j = 0; j < point.size(); j++) {
			if (j == i) {
				continue;
			}
			if (distance(point[i], point[j]) < point[i].radius * 2) {
				double C = (2 * point[i].radius - distance(point[i], point[j])) / (2 * distance(point[i], point[j]));
				if (!point[i].pinned) {
					point[i].posx += (point[i].posx - point[j].posx) * C;
					point[i].posy += (point[i].posy - point[j].posy) * C;
				}
				if (!point[j].pinned) {
					point[j].posx -= (point[i].posx - point[j].posx) * C;
					point[j].posy -= (point[i].posy - point[j].posy) * C;
				}
			}
		}
	}

	for (int i = 0; i < point.size(); i++) {
		constraint(point[i]);
	}
}

void applySticks(vector<Stick> &stick) {
	for (int i = 0; i < stick.size(); i++) {

		if (stick[i].tearable && distance(*stick[i].p1, *stick[i].p2) > stick[i].lenght * stick[i].tearval) {
			stick[i].tear = true;
		}
		if (!stick[i].tear) {
			stick[i].applyForce();
		}
	}
}

void drawSticks(vector<Stick> stick, Screen screen) {
	for (int i = 0; i < stick.size(); i++) {
		if (!stick[i].tear) {
			stick[i].drawStick(screen);
		}
	}
}

void drawPoints(vector<Point> point) {
	for (int i = 0; i < point.size(); i++) {
		point[i].draw();
	}
}

void updatePoints(vector<Point> &point) {
	for (int i = 0; i < point.size(); i++) {
		if (!point[i].pinned) {
			point[i].update(dt);
		}
	}
}

void bouncyBallSim() {
	Screen screen(0x000000FF);
	if (screen.init() == false) {
		screen.close();
		exit(1);
	}
	int ballCount = 200;
	vector<Point> point(0, Point(Screen::WIDTH / 2, Screen::HEIGHT / 2, 10, 0xFFFFFFFF, true, screen));
	point.reserve(1000);
	for (int i = 0; i <= ballCount; i++) {
		point.push_back(
				Point(Screen::WIDTH / 2 + ballCount / 2 * point[0].radius * cos(i * 2 * M_PI / ballCount),
						Screen::HEIGHT / 2 + ballCount / 2 * point[0].radius * sin(i * 2 * M_PI / ballCount), 2, 0xFFFFFFFF, false,
						screen));
	}
	vector<Stick> stick(0, Stick(&point[0], &point[1], 0.5, 0xFFFFFFFF, false, 1.2));
	for (int i = 0; i < point.size(); i++) {
		for (int j = 0; j < point.size(); j++) {
			if (j == i) {
				continue;
			}
			stick.push_back(Stick(&point[i], &point[j], 0.8, 0xFFFFFFFF, false, 2));
		}
	}
	SDL_Event event;
	Point *selectedPoint;
	double xs, ys;
	bool selected = false;
	bool done = false;
	while (!done) {
		SDL_PollEvent(&event);
		if (event.type == SDL_QUIT) {
			done = true;
		}
		if (event.type == SDL_KEYDOWN) {
			if (event.key.keysym.sym == SDLK_w) {
				for (int i = 0; i < point.size(); i++) {
					point[i].posy -= 1;
				}
			}
			if (event.key.keysym.sym == SDLK_s) {
				for (int i = 0; i < point.size(); i++) {
					point[i].posy += 1;
				}
			}
			if (event.key.keysym.sym == SDLK_d) {
				for (int i = 0; i < point.size(); i++) {
					point[i].posx += 1;
				}
			}
			if (event.key.keysym.sym == SDLK_a) {
				for (int i = 0; i < point.size(); i++) {
					point[i].posx -= 1;
				}
			}
		}

		if (event.type == SDL_MOUSEBUTTONDOWN && selected) {
			selected = false;
			selectedPoint = NULL;
			goto jump;
		}
		if (event.type == SDL_MOUSEBUTTONDOWN) {
			if (event.button.button == SDL_BUTTON_LEFT) {
				int x, y;
				SDL_GetGlobalMouseState(&x, &y);
				for (int i = 0; i < point.size(); i++) {
					if (sqrt(pow(point[i].posx - x, 2) + pow(point[i].posy - y, 2)) < point[i].radius) {
						selectedPoint = &point[i];
						selected = true;
						xs = point[i].posx - x;
						ys = point[i].posy - y;
						break;
					}
				}
			}
		}
		if (selected && selectedPoint != NULL) {
			int x, y;
			SDL_GetGlobalMouseState(&x, &y);
			selectedPoint->posx = x + xs;
			selectedPoint->posy = y + ys;
		}
		jump: updatePoints(point);
		solveCollisons(point);
		applySticks(stick);

		screen.drawRectangle((double) Screen::WIDTH * wPercent / 100 - point[0].radius,
				(double) Screen::HEIGHT * hPercent / 100 - point[0].radius,
				(double) Screen::WIDTH * (100 - 2 * wPercent) / 100 + point[0].radius * 2,
				(double) Screen::HEIGHT * (100 - 2 * hPercent) / 100 + point[0].radius * 2, 0x555555FF);
		drawPoints(point);
		screen.update();
	}
	screen.close();
}

void cupSim() {
	Screen screen(0x000000FF);
	if (screen.init() == false) {
		screen.close();
		exit(1);
	}
	vector<Point> point(0, Point(Screen::WIDTH / 2, Screen::HEIGHT / 2, 10, 0xFFFFFFFF, true, screen));
	point.reserve(1000);
	for (int i = 0; i < 10; i++) {
		if (i == 0) {
			point.push_back(Point(Screen::WIDTH / 2 + 30 * i - 180, Screen::HEIGHT / 2, 12, 0xFFFFFFFF, true, screen));
		} else if (i == 9) {
			point.push_back(Point(Screen::WIDTH / 2 + 30 * i - 180, Screen::HEIGHT / 2, 12, 0xFFFFFFFF, true, screen));
		} else {
			point.push_back(Point(Screen::WIDTH / 2 + 30 * i - 180, Screen::HEIGHT / 2, 12, 0xFFFFFFFF, false, screen));
		}

	}
	vector<Stick> stick(0, Stick(&point[0], &point[1], 0, 0xFFFFFFFF, true, 1.2));
	for (int i = 0; i < 10; i++) {
		if (i != 9) {
			stick.push_back(Stick(&point[i], &point[i + 1], 0.2, 0xFFFFFFFF, true, 1.5));
		}
	}

	bool done = false;
	int tick = SDL_GetTicks();
	while (!done) {
		if (!screen.processEvents()) {
			done = true;
		}

		updatePoints(point);
		for (int i = 0; i < 5; i++) {
			solveCollisons(point);
			applySticks(stick);
		}

		if (SDL_GetTicks() - tick > 300) {
			tick = SDL_GetTicks();
			point.push_back(Point(Screen::WIDTH / 2, 100, Screen::WIDTH / 2, 100 - 10, 12, 0xFFF00FFF, false, screen));
		}

		screen.drawRectangle((double) Screen::WIDTH * wPercent / 100 - point[0].radius,
				(double) Screen::HEIGHT * hPercent / 100 - point[0].radius,
				(double) Screen::WIDTH * (100 - 2 * wPercent) / 100 + point[0].radius * 2,
				(double) Screen::HEIGHT * (100 - 2 * hPercent) / 100 + point[0].radius * 2, 0x555555FF);
		drawSticks(stick, screen);
		drawPoints(point);

		screen.update();
	}
	screen.close();
}

